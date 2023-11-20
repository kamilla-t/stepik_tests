from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Открываем страницу
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

# Сумма заданных чисел
x_element = browser.find_element(By.ID, "num1")
x = int(x_element.text)

y_element = browser.find_element(By.ID, "num2")
y = int(y_element.text)

sum = x + y


# Выбрать в выпадающем списке значение равное расчитанной сумме
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(sum))


button = browser.find_element(By.XPATH, "//button[@type=\"submit\"]")
button.click()

#выход
time.sleep(15)
browser.quit()





