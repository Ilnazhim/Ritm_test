from selenium.webdriver.common.by import By
from utilities.logger import Logger
import allure
from base.base_class import BaseClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckboxPage(BaseClass):

    # Locators
    home_dir = "//button[@class='rct-collapse rct-collapse-btn']"
    downloads_dir = "//li[3]//button[@class='rct-collapse rct-collapse-btn']"
    word_file = "//span[contains(text(), 'Word')]"
    success_message = "//span[@class='text-success']"

    # Getters
    def get_home_dir(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.home_dir)))

    def get_downloads_dir(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.downloads_dir)))

    def get_word_file(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_file)))

    def get_success_message(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.success_message)))

    # Actions
    def click_home_dir(self):
        self.get_home_dir().click()
        print("Click home_dir")

    def click_downloads_dir(self):
        self.get_downloads_dir().click()
        print("Click downloads_dir")

    def click_word_file(self):
        self.get_word_file().click()
        print("Choose word_file")

    # Metods
    def choose_word_file(self):
        """Choose_word_file"""
        with allure.step("choose_word_file"):
            Logger.add_start_step(method="choose_word_file")
            self.click_home_dir()
            self.click_downloads_dir()
            self.click_word_file()
            assert self.get_success_message().text == "wordFile", f"message {self.get_success_message().text}  is not correct"
            Logger.add_end_step(url=self.browser.current_url, method="choose_word_file")
