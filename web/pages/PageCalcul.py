from web.driver.web_element import Element
from web.pages.base import BasePage


class calcul(BasePage):
    class Elements:
        number_1 = Element("//tr//div[@jsname='N10B9']")
        multiplication = Element("//div[@jsname='YovRWb']")
        number_2 = Element("//tr//div[@jsname='lVjWed']")
        minus = Element("//div[@jsname='pPHzQc']")
        number_3 = Element("//div[@jsname='KN1kY']")
        plus = Element("//div[@jsname='XSr6wc']")
        equals = Element("//div[@jsname='Pt8tGc']")
        expression = Element("//span[text()='1 × 2 - 3 + 1 =']")
        result = Element("//span[text()='0']")

    def is_loaded(self):
        Element("//body").wait_visible()
        return True

    def do_calcul(self):
        self.Elements.number_1.click()
        self.Elements.multiplication.click()
        self.Elements.number_2.click()
        self.Elements.minus.click()
        self.Elements.number_3.click()
        self.Elements.plus.click()
        self.Elements.number_1.click()
        self.Elements.equals.click()
        self.Elements.expression.wait_visible()
        self.Elements.result.wait_visible()