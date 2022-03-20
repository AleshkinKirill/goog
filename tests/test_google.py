from utils.allure import allure_step


def test_google(pages):

    with allure_step("Перейти в гугл"):
        pages.google_page.open()

    with allure_step("Перейти в калькулятор"):
        pages.go_to_calcul.go_to_calcul()

    with allure_step("Произвести расчет"):
        pages.PageCalcul.do_calcul()