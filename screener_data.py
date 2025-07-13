from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
class screener_data:
    @staticmethod
    def copy_table_data(driver, wait):
        try:
            # Wait for table body to load
            table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table tbody')))
            rows = table.find_elements(By.TAG_NAME, 'tr')
            print(f"📄 Found {len(rows)} rows in table.")

            # Get column headers
            headers = driver.find_elements(By.CSS_SELECTOR, 'table thead tr th')
            header_names = [header.text.strip() for header in headers if header.text.strip() != '']

            print(f"🧾 Headers detected: {header_names}")

            data = []
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, 'td')
                row_data = [cell.text.strip() for cell in cells if cell.text.strip() != '']

                if len(row_data) != len(header_names):
                    print(f"⚠️ Skipping row due to mismatch: {row_data}")
                    continue

                data.append(dict(zip(header_names, row_data)))

            df = pd.DataFrame(data)
            print("✅ Table data extracted successfully.")
            return df

        except Exception as e:
            print(f"❌ Failed to extract table data:\n{e}")
            return None
