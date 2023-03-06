from selenium.webdriver.common.by import By
from utilities.logger import Logger
import allure
from base.base_class import BaseClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ElementPage(BaseClass):

    # Locators
    menu_check_box = "//span[text()='Check Box']"

    # Getters
    def get_menu_check_box(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_check_box)))

    # Actions
    def click_menu_check_box(self):
        self.get_menu_check_box().click()
        print("Click menu_checkbox")

    # Metods
    def go_to_checkbox_page(self):
        """Go to check_box_page"""
        with allure.step("go_to_checkbox_page"):
            Logger.add_start_step(method="go_to_checkbox_page")
            self.click_menu_check_box()
            Logger.add_end_step(url=self.browser.current_url, method="go_to_checkbox_page")
