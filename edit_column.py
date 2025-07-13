from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
class edit_column:
    @staticmethod
    def save_columns(driver, wait):
        try:
            # Wait for button with correct case-sensitive text
            save_btn = wait.until(EC.element_to_be_clickable((
                By.XPATH, '//button[@type="submit" and contains(text(), "Save columns")]'
            )))

            # Scroll and click
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_btn)
            time.sleep(0.3)
            save_btn.click()
            print("💾 Columns saved successfully.")

        except Exception as e:
            print("❌ Failed to save columns.")
            print(f"   Error: {e}")

    def clear_selected_columns(driver, wait):
        try:
            print("🔍 Starting to clear selected columns...")

            while True:
                # Find the first available close button (X) inside #manage-menu
                try:
                    close_btn = wait.until(EC.presence_of_element_located((
                        By.CSS_SELECTOR, '#manage-menu li button.button-plain'
                    )))
                except:
                    print("🧼 All columns cleared.")
                    break

                # Scroll and click the first 'X' button
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", close_btn)
                time.sleep(0.2)
                driver.execute_script("arguments[0].click();", close_btn)
                print("❌ Removed one column")

                time.sleep(0.3)  # Wait for DOM to update

        except Exception as e:
            print("❌ Error while clearing selected columns")
            print(f"   Error: {e}")

    def get_label_batches(parameters_dict, batch_size=13):
        """
        Yields (tab_name, batch_labels) for each group of 13.
        Each batch is a list of labels from recent + preceding + historical.
        """
        for tab_name, categories in parameters_dict.items():
            all_labels = categories.get("Recent", []) + \
                        categories.get("Preceding", []) + \
                        categories.get("Historical", [])
            
            for i in range(0, len(all_labels), batch_size):
                yield tab_name, all_labels[i:i + batch_size]

    def select_named_checkboxes(tab_name, label_list, driver, wait):
        """
        Switches to the specified tab (Annual P&L, Quarter PL, etc.)
        and selects checkboxes matching the provided label_list (max 13).
        """
        try:
            # Click the tab
            tab_button = wait.until(EC.element_to_be_clickable((
                By.XPATH, f'//button[contains(text(), "{tab_name}")]'
            )))
            driver.execute_script("arguments[0].click();", tab_button)
            print(f"\n📘 Switched to '{tab_name}' tab")
            time.sleep(1.5)

            # Locate main container
            container = wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, 'div.flex-grow'
            )))

            checkboxes = container.find_elements(By.XPATH, './/label')

            selected = 0
            for label_element in checkboxes:
                try:
                    label_text = label_element.text.strip()
                    input_element = label_element.find_element(By.XPATH, './/input[@type="checkbox"]')

                    if label_text in label_list and not input_element.is_selected():
                        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", input_element)
                        time.sleep(0.1)
                        driver.execute_script("arguments[0].click();", input_element)
                        selected += 1
                        print(f"✅ Selected: {label_text}")

                        if selected >= len(label_list):
                            break
                except Exception as e:
                    print(f"⚠️ Could not click checkbox for: {label_element.text} — {e}")

            if selected == 0:
                print("⚠️ No matching checkboxes were selected.")
        except Exception as e:
            print(f"❌ Failed to select checkboxes in '{tab_name}' tab: {e}")

    # def select_ratios_in_tabs(tab_names, max_checkboxes=13, driver=None, wait=None):
        
    #     try:
    #         # Click the tab
    #         tab_button = wait.until(EC.element_to_be_clickable((
    #             By.XPATH, f'//button[contains(text(), "{tab_names}")]'
    #         )))
    #         driver.execute_script("arguments[0].click();", tab_button)
    #         print(f"\n📘 Switched to '{tab_names}' tab")
    #         time.sleep(1.5)

    #             # Find the main container
    #         container = wait.until(EC.presence_of_element_located((
    #             By.CSS_SELECTOR, 'div.flex-grow'
    #         )))

    #             # Select checkboxes under this container (visible only)
    #         checkboxes = container.find_elements(By.XPATH, './/input[@type="checkbox" and not(@disabled)]')

    #         print(f"🧩 Found {len(checkboxes)} checkboxes in '{tab_names}' section. Selecting up to {max_checkboxes}...")

    #         selected = 0
    #         for i, checkbox in enumerate(checkboxes):
    #             if selected >= max_checkboxes:
    #                 break
    #             try:
    #                 driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
    #                 time.sleep(0.2)
    #                 if not checkbox.is_selected():
    #                     driver.execute_script("arguments[0].click();", checkbox)
    #                     label = checkbox.get_attribute("value")
    #                     print(f"✅ Checked box {selected + 1}: {label}")
    #                     selected += 1
    #             except Exception as click_error:
    #                 print(f"⚠️ Could not click checkbox {i + 1}: {click_error}")
    #     except Exception as e:
    #         print(f"❌ Error in {tab_names} section:\n   {e}")

