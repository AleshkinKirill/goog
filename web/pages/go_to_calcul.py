from web.driver.web_element import Element
from web.pages.base import BasePage


class calcul_page(BasePage):
    class Elements:
        searchbar = Element("//input[@class='gLFyf gsfi']")
        search_button = Element("//div[@class='CqAVzb lJ9FBc']/center/input[@class='gNO89b']")

    def is_loaded(self):
        Element("//body").wait_visible()
        return True

    def go_to_calcul(self):
        self.Elements.searchbar.fill("калькулятор")
        self.Elements.search_button.click()