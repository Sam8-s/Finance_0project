from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import io

class screener_data:
    @staticmethod
    def copy_table_data(driver, wait):
        try:
            table_elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table.data-table, table')))
            table_html = table_elem.get_attribute('outerHTML')
            
            dfs = pd.read_html(io.StringIO(table_html))
            if not dfs:
                return None
                
            df = dfs[0]
            # Strip index artifacts and unnamed headers
            df = df.loc[:, ~df.columns.str.contains('^Unnamed|^S\\.No')]
            
            if 'Name' in df.columns:
                df['Name'] = df['Name'].astype(str).str.strip()
                
            return df
        except Exception as e:
            print(f"❌ Failed to extract table data: {e}")
            return None