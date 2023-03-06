import datetime


class BaseClass:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    """Metod open browser"""
    def open(self):
        self.browser.get(self.url)

    """Metod get current url"""
    def get_current_url(self):
        get_url = self.browser.current_url
        print("Current url " + get_url)

