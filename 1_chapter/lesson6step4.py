from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/simple_form_find_task.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Kamilla")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Tazieva")
    input3 = browser.find_element(By.CSS_SELECTOR, ".form-control.city")
    input3.send_keys("Kazan")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()