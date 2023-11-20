from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# открываем браузер
link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

input = browser.find_element(By.ID, "answer")
input.send_keys(y)

checkbox = browser.find_element(By.CLASS_NAME, "form-check-input")
checkbox.click()

radiobutton = browser.find_element(By.CSS_SELECTOR, "[for = 'robotsRule']")
radiobutton.click()

submitButton = browser.find_element(By.XPATH, "//button[contains(text(), \"Submit\")]")
submitButton.click()

time.sleep(10)
browser.quit()



