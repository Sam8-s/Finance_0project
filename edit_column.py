from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class edit_column:
    @staticmethod
    def save_columns(driver, wait):
        try:
            save_btn = wait.until(EC.element_to_be_clickable((
                By.XPATH, '//button[@type="submit" and contains(text(), "Save columns")]'
            )))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_btn)
            driver.execute_script("arguments[0].click();", save_btn)
            # print("💾 Columns saved successfully.")
        except Exception as e:
            print("❌ Failed to save columns.")
            print(f"   Error: {e}")

    @staticmethod
    def clear_selected_columns(driver, wait):
        try:
            # print("🔍 Starting to clear selected columns...")
            while True:
                try:
                    close_btn = wait.until(EC.presence_of_element_located((
                        By.CSS_SELECTOR, '#manage-menu li button.button-plain'
                    )))
                except:
                    print("🧼 All columns cleared.")
                    break

                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", close_btn)
                driver.execute_script("arguments[0].click();", close_btn)
                # print("❌ Removed one column")
        except Exception as e:
            print("❌ Error while clearing selected columns")
            print(f"   Error: {e}")

    @staticmethod
    def get_label_batches(parameters_dict, batch_size=13):
        for tab_name, categories in parameters_dict.items():
            all_labels = categories.get("Recent", []) + \
                         categories.get("Preceding", []) + \
                         categories.get("Historical", [])
            for i in range(0, len(all_labels), batch_size):
                yield tab_name, all_labels[i:i + batch_size]

    @staticmethod
    def select_named_checkboxes(tab_name, label_list, driver, wait):
        try:
            tab_button = wait.until(EC.element_to_be_clickable((
                By.XPATH, f'//button[contains(text(), "{tab_name}")]'
            )))
            driver.execute_script("arguments[0].click();", tab_button)
            # print(f"\n📘 Switched to '{tab_name}' tab")

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
                        driver.execute_script("arguments[0].click();", input_element)
                        selected += 1
                        # print(f"✅ Selected: {label_text}")
                        if selected >= len(label_list):
                            break
                except Exception as e:
                    print(f"⚠️ Could not click checkbox for: {label_element.text} — {e}")

            if selected == 0:
                print("⚠️ No matching checkboxes were selected.")
        except Exception as e:
            print(f"❌ Failed to select checkboxes in '{tab_name}' tab: {e}")
