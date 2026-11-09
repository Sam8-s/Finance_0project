from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException
import time
import pandas as pd
from edit_column import edit_column

import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

class screener_0:
    USERNAME = os.getenv("SCREENER_USERNAME")
    PASSWORD = os.getenv("SCREENER_PASSWORD")
    EDGEDRIVER_PATH = r"C:\edgedriver_win64\msedgedriver.exe"
    # STOCK_SYMBOL_TO_NAME = {
    #     "TATAMOTORS": "Tata Motors",
    #     "IRFC": "Indian Railway Finance"
    # }

    def __init__(self):
        self.options = EdgeOptions()
        self.options.add_argument("--headless=new")  # Headless mode
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Edge(
            service=EdgeService(self.EDGEDRIVER_PATH),
            options=self.options
        )
        self.wait = WebDriverWait(self.driver, 5)


    def login(self):
        self.driver.get("https://www.screener.in/login/")
        self.wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(self.USERNAME)
        self.wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(self.PASSWORD + Keys.RETURN)
        self.wait.until(EC.any_of(
            EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Core Watchlist")]')),
            EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "WATCHLIST VIEW")]'))
        ))

    def go_to_watchlist(self):
        self.driver.get("https://www.screener.in/watchlist/8596015/")

    def click_edit_columns_button(self):
        try:
            edit_btn = self.wait.until(EC.element_to_be_clickable((
                By.XPATH, '//a[contains(@href, "/user/columns") and contains(., "Edit Columns")]'
            )))
            self.driver.execute_script("arguments[0].click();", edit_btn)
        except Exception as e:
            print("Error clicking edit columns button:", e)

    def add_companies(self, stock_list):
        for stock in stock_list:
            try:
                input_box = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="eg. Infosys"]')))
                input_box.clear()
                input_box.send_keys(stock)
                time.sleep(0.3)
                input_box.send_keys(Keys.ARROW_DOWN)
                input_box.send_keys(Keys.RETURN)
                time.sleep(0.3)
            except Exception as e:
                print("Error adding company:", e)

        try:
            done_btn = self.wait.until(EC.element_to_be_clickable((
                By.XPATH, '//div[contains(@class, "modal-content")]//button[text()="DONE"]'
            )))
            done_btn.click()
        except TimeoutException as e:
            print("Done button timeout:", e)

    def delete_companies(self, stock_symbol_list):
        try:
            self.open_add_company_page()
            time.sleep(0.5)

            for symbol in stock_symbol_list:
                stock_text = self.STOCK_SYMBOL_TO_NAME.get(symbol.upper(), symbol)

                try:
                    stock_label = self.wait.until(EC.presence_of_element_located((
                        By.XPATH, f'//div[contains(@class, "modal-content")]//div[contains(text(), "{stock_text}")]'
                    )))
                    delete_icon = stock_label.find_element(By.XPATH, './/ancestor::div[contains(@class, "flex")][1]//button')
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", delete_icon)
                    time.sleep(0.2)
                    self.driver.execute_script("arguments[0].click();", delete_icon)
                    time.sleep(0.2)
                except Exception as e:
                    print(f"Error deleting company {stock_text}:", e)

            try:
                done_btn = self.wait.until(EC.element_to_be_clickable((
                    By.XPATH, '//div[contains(@class, "modal-content")]//button[text()="DONE"]'
                )))
                self.driver.execute_script("arguments[0].click();", done_btn)
            except Exception as e:
                print("Done button click error in delete_companies:", e)

        except Exception as e:
            print("Error in delete_companies:", e)

    def open_add_company_page(self):
        xpath = "//a[contains(normalize-space(), 'Companies')]"
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
        except Exception as e:
            print("Error opening add company page:", e)

    def click_import_companies_button(self):
        xpath = "//a[contains(normalize-space(), 'Import Companies')]"
        try:
            element = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
        except Exception as e:
            print("Error clicking import companies button:", e)

    def paste_companies_and_import(self, companies_list):
        try:
            companies_text = "\n".join(companies_list.values())
            textarea = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "id_names"))
            )
            textarea.clear()
            textarea.send_keys(companies_text)

            import_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Import']"))
            )
            import_button.click()
        except Exception as e:
            print("Error pasting companies and importing:", e)

    def click_import_button(self):
        xpath = "//button[@type='submit' and contains(@class, 'button-primary') and contains(@class, 'margin-top-12') and normalize-space(text())='Import']"
        try:
            button = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
            try:
                button.click()
            except:
                self.driver.execute_script("arguments[0].click();", button)
        except Exception as e:
            print("Error clicking final import button:", e)

    def click_undo_last_import(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//a[normalize-space(text())='Undo last import']"))
            )
            element.click()
        except Exception as e:
            print("Error clicking undo last import:", e)

    def click_confirm_undo(self):
        try:
            button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Confirm Undo') and @class='red']"))
            )
            button.click()
        except Exception as e:
            print("Error clicking confirm undo:", e)

    def handle_watchlist_cleanup(self):
        while True:
            try:
                trash_buttons = self.driver.find_elements(By.CSS_SELECTOR, "ul.no-style li button.red")
                if not trash_buttons:
                    break

                btn = trash_buttons[0]
                self.driver.execute_script("arguments[0].click();", btn)
                time.sleep(0.5)

            except StaleElementReferenceException:
                continue
            except Exception as e:
                print("Error during watchlist cleanup:", e)
                break

        try:
            done_button = self.driver.find_element(By.CSS_SELECTOR, "a.button.button-primary[href*='/watchlist/']")
            self.driver.execute_script("arguments[0].click();", done_button)
        except Exception as e:
            print("Error clicking done in watchlist cleanup:", e)
