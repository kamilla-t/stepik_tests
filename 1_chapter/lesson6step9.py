from selenium import webdriver
from selenium.webdriver.common.by import By
import time
    
link = "https://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.CLASS_NAME, "first")
input1.send_keys("Kamilla")

input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder =\"Input your last name\"]")
input2.send_keys("Tazieva")

input3 = browser.find_element(By.CLASS_NAME, "third")
input3.send_keys("kamilla.tazieva26@gmail.com")

button = browser.find_element(By.CLASS_NAME, "btn")
button.click()



# находим элемент, содержащий текст
welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Congratulations! You have successfully registered!" == welcome_text

time.sleep(30)
browser.quit()
