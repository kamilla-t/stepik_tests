from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

# говорим Selenium проверять в течение 12 секунд, пока текст не будет равен
price =  WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)

# assert "100$" in price.text
button_book = browser.find_element(By.ID, "book")
button_book.click()

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


