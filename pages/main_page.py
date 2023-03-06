from selenium.webdriver.common.by import By
from utilities.logger import Logger
import allure
from base.base_class import BaseClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BaseClass):

    # Locators
    elements_card = "//h5[text()='Elements']"

    # Getters
    def get_elements_card(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.elements_card)))

    # Actions
    def click_elements_card(self):
        self.get_elements_card().click()
        print("Click elements_card")

    # Metods
    def go_to_elements_page(self):
        """Go to elements_page"""
        with allure.step("go_to_elements_page"):
            Logger.add_start_step(method="go_to_elements_page")
            self.browser.execute_script("window.scrollBy(0, 300);")  #пришлось сделать скролл, на моем разрешении подвал закрывал локатор
            self.click_elements_card()
            Logger.add_end_step(url=self.browser.current_url, method="go_to_elements_page")
