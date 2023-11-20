from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.NAME, "firstname")
input1.send_keys("Kamilla")

input2 = browser.find_element(By.NAME, "lastname")
input2.send_keys("Tazieva")

input3 = browser.find_element(By.NAME, "email")
input3.send_keys("kotik.com")

# получаем путь к директории текущего исполняемого файла 
current_dir = os.path.abspath("C:\\main\\python_tests\\2_chapter")
# добавляем к этому пути имя файла 
file_path = os.path.join(current_dir, 'index.txt')
file_input = browser.find_element(By.ID, "file")
file_input.send_keys(file_path)

submit_button = browser.find_element(By.TAG_NAME, "button")
submit_button.click()

browser.quit()


