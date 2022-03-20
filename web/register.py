# Инициализатор страниц(page объектов)
# Каждую новую страницу нужно будет обязательно тут проинициализировать

from web.driver.base import BaseWebDriver
from web.pages.PageGoogle import google
from web.pages.PageCalcul import calcul
from web.pages.go_to_calcul import calcul_page


class Pages:
    browser: BaseWebDriver
    google_page: google
    PageCalcul: calcul
    go_to_calcul: calcul_page

    @classmethod
    def init(cls, browser: BaseWebDriver):
        cls.browser = browser
        cls.google_page = google(browser)
        cls.PageCalcul = calcul(browser)
        cls.go_to_calcul = calcul_page(browser)


pages = Pages()
