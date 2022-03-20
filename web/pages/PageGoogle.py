from web.driver.web_element import Element
from web.pages.base import BasePage


class google(BasePage):
    url = "http://google.com"
    name = "Google"

    def is_loaded(self):
        Element("//body").wait_visible()
        return True
