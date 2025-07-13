from screener_0 import screener_0
from edit_column import edit_column
from screener_data import screener_data
from Data import job_data
import pandas as pd

def run_scraper():
    bot = screener_0()
    main_df = pd.DataFrame()

    try:
        bot.login()
        bot.go_to_watchlist()
        #bot.click_edit_columns_button()

        for tab, batch in edit_column.get_label_batches(job_data.parameters, batch_size=13):
            bot.click_edit_columns_button()
            print(f"\n🔄 Processing batch from tab: {tab} -> {batch[:2]} ...")

            # Clear previous 13 parameters
            edit_column.clear_selected_columns(bot.driver, bot.wait)

            # Select new 13 checkboxes
            edit_column.select_named_checkboxes(tab, batch, bot.driver, bot.wait)

            # Save selected columns
            edit_column.save_columns(bot.driver, bot.wait)

            # Extract table data
            df = screener_data.copy_table_data(bot.driver, bot.wait)

            if df is not None and not df.empty:
                if main_df.empty:
                    main_df = df
                else:
                    # Merge without overwriting existing values
                    main_df = pd.merge(main_df, df, on='Name', how='outer', suffixes=('', '_new'))

                    for col in df.columns:
                        if col == 'Name' or col not in main_df.columns:
                            continue
                        if col + '_new' in main_df.columns:
                            main_df[col] = main_df[col].combine_first(main_df[col + '_new'])
                            main_df.drop(columns=[col + '_new'], inplace=True)

        # Save final result
        main_df.to_excel("screener_combined_output.xlsx", index=False)
        print("✅ All data saved to screener_combined_output.xlsx")

    finally:
        print("🎉 Script completed.")
        # bot.driver.quit()  # Uncomment if you want to close browser automatically

if __name__ == "__main__":
    run_scraper()
