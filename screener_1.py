from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

class screener_1:
    @staticmethod
    def copy_table_data(driver, wait):
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.data-table")))
            # print("✅ Table loaded")

            # Step 1: Get all rows (including header row)
            rows = driver.find_elements(By.CSS_SELECTOR, "table.data-table tbody tr")
            # print(f"🔎 Total <tr> rows found: {len(rows)}")

            # Step 2: First row is headers (with <th>)
            header_ths = rows[0].find_elements(By.TAG_NAME, "th")[2:]  # skip S.No. and icon
            header_names = []
            header_names.append("Name")  # Ensure 'Name' is always included
            for th in header_ths:
                try:
                    a_tag = th.find_element(By.TAG_NAME, "a")
                    full_text = a_tag.text.strip().replace("\n", " ")
                    header_names.append(full_text)
                except:
                    header_names.append("Unnamed")
            # print("🧾 Extracted Headers:", header_names)

            # Step 3: Process data rows (skip first row)
            data = []
            for row in rows[1:]:
                tds = row.find_elements(By.TAG_NAME, "td")[2:]  # skip S.No. and icon
                row_data = [td.text.strip() for td in tds]

                # Adjust length
                if len(row_data) < len(header_names):
                    row_data += [''] * (len(header_names) - len(row_data))
                elif len(row_data) > len(header_names):
                    row_data = row_data[:len(header_names)]

                data.append(dict(zip(header_names, row_data)))

            # Step 4: Convert to DataFrame
            df = pd.DataFrame(data)
            
            # Drop rows where all columns except Name are blank
            df = df.loc[
                df.drop(columns=['Name']).astype(str)
                .apply(lambda row: row.str.strip().ne('').any(), axis=1)
            ].reset_index(drop=True)

            # Remove all-blank columns except Name
            for col in df.columns:
                if col == 'Name':
                    continue
                col_str = df[col].astype(str).str.strip()
                if not col_str.any():
                    df.drop(columns=[col], inplace=True)

            # print("✅ Final DataFrame:")
            # print(df.head())
            return df

        except Exception as e:
            print("❌ Error extracting table:", e)
            return None
