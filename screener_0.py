from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
from edit_column import edit_column 

class screener_0:
    # === User Config ===
    USERNAME = "d.samyu2626@gmail.com"
    PASSWORD = "ammu2006"
    CHROMEDRIVER_PATH = r"C:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    STOCKS_TO_ADD = ["TATAMOTORS", "IRFC"]
    STOCK_SYMBOL_TO_NAME = {
        "TATAMOTORS": "Tata Motors",
        "IRFC": "Indian Railway Finance"
    }

    def __init__(self):
        # === Setup Driver ===
        self.options = Options()
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(self.CHROMEDRIVER_PATH), options=self.options)
        self.wait = WebDriverWait(self.driver, 15)

    def login(self):
        self.driver.get("https://www.screener.in/login/")
        self.wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(self.USERNAME)
        self.wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(self.PASSWORD + Keys.RETURN)
        
        # Wait for login to complete
        self.wait.until(EC.any_of(
            EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Core Watchlist")]')),
            EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "WATCHLIST VIEW")]'))
        ))
        print("✅ Logged in successfully")
    def go_to_watchlist(self):
        self.driver.get("https://www.screener.in/watchlist/8596015/")
        print("✅ Navigated to watchlist")

    def click_edit_columns_button(self):
        try:
            # Wait for the <a> tag with proper href and text
            edit_btn = self.wait.until(EC.element_to_be_clickable((
                By.XPATH, '//a[contains(@href, "/user/columns") and contains(., "Edit Columns")]'
            )))
            self.driver.execute_script("arguments[0].click();", edit_btn)
            print("🛠️ Clicked EDIT COLUMNS button.")
        except Exception as e:
            print("❌ Failed to click EDIT COLUMNS.")
            print(f"   Error: {e}")
            print(f"   Error: {e}")

    def open_add_company_page(self):
        try:
            # Click the vertical three-dot menu button
            menu_button = self.wait.until(EC.element_to_be_clickable((
                By.XPATH, '//button[.//*[local-name()="svg"][@stroke="currentColor"]]'
            )))
            self.driver.execute_script("arguments[0].click();", menu_button)
            print("☰ Opened menu")

            # Correct XPath: combine class and text in one condition
            companies_option = self.wait.until(EC.element_to_be_clickable((
                By.XPATH, '//a[contains(@class, "button") and contains(text(), "Companies")]'
            )))
            self.driver.execute_script("arguments[0].click();", companies_option)
            print("✅ Clicked COMPANIES from menu")

            self.wait.until(EC.presence_of_element_located((
                By.XPATH, '//h2[contains(text(), "Add companies to Core Watchlist")]'
            )))
            print("✅ Companies modal is now open")
        except Exception as e:
            print("❌ Failed to open Add Companies modal")
            print(f"   Error: {e}")
            self.driver.save_screenshot("companies_open_fail.png")
            self.driver.save_screenshot("companies_open_fail.png")
    def add_companies(self, stock_list):
        for stock in stock_list:
            try:
                input_box = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="eg. Infosys"]')))
                input_box.clear()
                input_box.send_keys(stock)
                time.sleep(2)  # Wait for suggestions to appear

                # Press DOWN arrow to select the first suggestion, then RETURN
                input_box.send_keys(Keys.ARROW_DOWN)
                input_box.send_keys(Keys.RETURN)
                print(f"✅ Added {stock}")
                time.sleep(1)
            except Exception as e:
                print(f"❌ Failed to add {stock}: {e}")

        try:
            done_btn = self.wait.until(EC.element_to_be_clickable((
                By.XPATH, '//div[contains(@class, "modal-content")]//button[text()="DONE"]'
            )))
            done_btn.click()
            print("✅ Clicked DONE – companies added.")
        except TimeoutException:
            print("❌ DONE button not found")
            print("❌ DONE button not found")

    def delete_companies(self, stock_symbol_list):
        try:
            self.open_add_company_page()
            time.sleep(1)

            for symbol in stock_symbol_list:
                stock_text = self.STOCK_SYMBOL_TO_NAME.get(symbol.upper(), symbol)

                try:
                    # Find the full company name div
                    stock_label = self.wait.until(EC.presence_of_element_located((
                        By.XPATH, f'//div[contains(@class, "modal-content")]//div[contains(text(), "{stock_text}")]'
                    )))

                    # Get the delete (trash) icon button next to the stock
                    delete_icon = stock_label.find_element(
                        By.XPATH, './/ancestor::div[contains(@class, "flex")][1]//button'
                    )

                    # Scroll and click the delete button
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", delete_icon)
                    time.sleep(0.2)
                    self.driver.execute_script("arguments[0].click();", delete_icon)
                    print(f"🗑️ Deleted: {symbol}")
                    time.sleep(0.5)

                except Exception as e:
                    print(f"❌ Could not delete '{symbol}': {e}")

            # Click DONE to save changes
            try:
                done_btn = self.wait.until(EC.element_to_be_clickable((
                    By.XPATH, '//div[contains(@class, "modal-content")]//button[text()="DONE"]'
                )))
                self.driver.execute_script("arguments[0].click();", done_btn)
                print("✅ Saved changes after deletion")
            except:
                print("⚠️ DONE button not found or not clickable")

        except Exception as e:
            print(f"❌ Error in delete_companies(): {e}")
            print(f"❌ Error in delete_companies(): {e}")
        