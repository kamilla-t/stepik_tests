# Маркировка тестов часть 1

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope = "function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser")
    browser.quit()

class TestMainPage1():
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

# запуск
# pytest -s -v -m smoke test_fixture8.py

# Как же регистрировать метки?
# Создайте файл pytest.ini в корневой директории вашего тестового проекта и добавьте в файл следующие строки:

# [pytest]
# markers =
#     smoke: marker for smoke tests
#     regression: marker for regression tests
