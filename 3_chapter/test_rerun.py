# # Плагины и перезапуск тестов
# pip install pytest-rerunfailures

# "--reruns n", где n — это количество перезапусков
# параметр "--tb=line" чтобы сократить лог с результатами теста

# pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")