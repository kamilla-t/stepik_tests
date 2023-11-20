from selenium import webdriver
from selenium.webdriver.common.by import By
import math 
import time

link = "https://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CLASS_NAME, "trollface")
button.click()

new_window = browser.window_handles[1]
first_window = browser.window_handles[0]

browser.switch_to.window(new_window)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

input = browser.find_element(By.ID, "answer")
input.send_keys(y)

submit_button = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
submit_button.click()

time.sleep(10)
browser.quit()


