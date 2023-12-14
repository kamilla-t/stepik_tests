from selenium.webdriver.common.by import By
import time


def test_guest_should_see_button_add_to_card_pass(browser, request):
    user_language = request.config.getoption("language")
    link = f"http://selenium1py.pythonanywhere.com/{user_language}/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert button, 'no such button!'

# def test_guest_should_see_login_link_fail(browser):
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#magic_link")


# Плагины и перезапуск тестов
# pip install pytest-rerunfailures

# "--reruns n", где n — это количество перезапусков
# параметр "--tb=line" чтобы сократить лог с результатами теста

# pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py