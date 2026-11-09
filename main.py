from screener_0 import screener_0
from edit_column import edit_column
from screener_1 import screener_1
from Data import job_data
import pandas as pd
import time
from selenium.common.exceptions import InvalidSessionIdException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def merge_dataframes(main_df, new_df):
    def clean_names(df):
        df = df.copy()
        if 'Name' not in df.columns:
        #   print(f"❌ Skipping: 'Name' column missing in DataFrame. Columns: {df.columns.tolist()}")
            return pd.DataFrame()
        df['Name'] = df['Name'].astype(str).str.strip().str.upper()
        return df

    new_df = clean_names(new_df)
    main_df = clean_names(main_df)

    if new_df.empty:
        # print("⚠️ Skipping merge: Cleaned new_df is empty.")
        return main_df

    if main_df.empty:
        return new_df.copy()

    merged_df = pd.merge(main_df, new_df, on='Name', how='outer', suffixes=('', '_new'))

    for col in new_df.columns:
        if col == 'Name':
            continue
        new_col = col + '_new'
        if new_col in merged_df.columns:
            merged_df[col] = merged_df[col].combine_first(merged_df[new_col])
            merged_df.drop(columns=[new_col], inplace=True)

    return merged_df

def run_scraper(driver, wait, main_df):
    try:
        for tab, label_batch in edit_column.get_label_batches(job_data.parameters, batch_size=13):
            try:
                bot.click_edit_columns_button()
                # print(f"\nὐ4 Processing batch from tab: {tab} -> {label_batch[:2]} ...")

                edit_column.clear_selected_columns(driver, wait)
                edit_column.select_named_checkboxes(tab, label_batch, driver, wait)
                edit_column.save_columns(driver, wait)

                df = screener_1.copy_table_data(driver, wait)

                if df is not None and not df.empty:
                    if 'Name' not in df.columns:
                        print("❌ Skipping DataFrame: 'Name' column not found.")
                    else:
                        main_df = merge_dataframes(main_df, df)

            except InvalidSessionIdException:
                print("❌ WebDriver session expired. Exiting early.")
                break
            except WebDriverException as e:
                print(f"⚠️ WebDriver error encountered:")
                continue
            except Exception as e:
                print(f"⚠️ Unexpected error:")
                continue

    finally:
        # print("🎉 Batch scraping complete.")
        return main_df


# Main execution
if __name__ == "__main__":
    bot = screener_0()
    final_df = pd.DataFrame()

    bot.login()
    bot.go_to_watchlist()
    bot.open_add_company_page()
    bot.handle_watchlist_cleanup()

    all_batches = [job_data.batch_1, job_data.batch_2,job_data.batch_3, job_data.batch_4]
    # Add more batches as needed: job_data.batch_3, job_data.batch_4 ...

    for company_batch in all_batches:
        bot.open_add_company_page()
        bot.click_import_companies_button()
        # print(f"\n📅 Importing companies: {company_batch}")
        bot.paste_companies_and_import(company_batch)
        bot.click_import_button()

        final_df = run_scraper(bot.driver, bot.wait, final_df)
        # print(final_df)
        
        bot.open_add_company_page()
        bot.click_import_companies_button()
        bot.click_undo_last_import()
        bot.click_confirm_undo()
    final_df['Name'] = final_df['Name'].map(job_data.company_dict)    
    # Final save
    if not final_df.empty:
        final_df.to_excel("screener_combined_output.xlsx", index=False)
        print("✅ Data saved to screener_combined_output.xlsx")
    else:
        print("⚠️ No data collected to save.")
