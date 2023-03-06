import time
import allure
from pages.checkbox_page import CheckboxPage
from pages.main_page import MainPage
from pages.elements_page import ElementPage


@allure.description("Test ritm task")
def test_ritm_task(browser):

    link = "https://demoqa.com/"
    browser.maximize_window()

    print("\nGo to elements page")
    mp = MainPage(browser, link)
    mp.open()
    mp.go_to_elements_page()

    print("\nGo to checkbox page")
    ep = ElementPage(browser, link)
    ep.go_to_checkbox_page()

    cp = CheckboxPage(browser, link)
    cp.choose_word_file()

    print("\nEnd test ritm task")
    time.sleep(3)
