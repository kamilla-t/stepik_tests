from ctypes.wintypes import SERVICE_STATUS_HANDLE
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    browser = webdriver.Chrome(options=options)
    browser.get('https://google.com')
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestMainPage1():

    @pytest.mark.parametrize('link', [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1" 
    ])
    def test_login_page(self, browser, link):
        browser.get(link)

        login_button = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.ID, "ember33")))
        login_button.click()

        login_email = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.ID, "id_login_email")))
        login_email.send_keys("your login")

        login_password = browser.find_element(By.ID, "id_login_password")
        login_password.send_keys("your password")

        button_sign_in = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()=\"Войти\"]")))
        button_sign_in.click()

        input = WebDriverWait(browser, 70).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".attempt textarea")))
        answer = math.log(int(time.time()- 1.8))
        input.send_keys(answer) 

        button_send = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class=\"submit-submission\"]")))
        button_send.click() 

        correct_answer_elt = WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.XPATH, "//p[@class=\"smart-hints__hint\"]")))
        correct_answer = correct_answer_elt.text
        assert correct_answer != "Correct!"

#The owls are not what they seem! OvO


