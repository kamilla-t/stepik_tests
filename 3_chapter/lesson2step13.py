from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestReg(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        input1 = browser.find_element(By.CLASS_NAME, "first")
        input1.send_keys("Kamilla")

        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder =\"Input your last name\"]")
        input2.send_keys("Tazieva")

        input3 = browser.find_element(By.CLASS_NAME, "third")
        input3.send_keys("kamilla-tazieva@mail.ru")

        button = browser.find_element(By.CLASS_NAME, "btn")
        button.click()


        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Everything is correct")
        browser.quit()

    def test_reg2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        input_name = browser.find_element(By.CLASS_NAME, "first")
        input_name.send_keys("Kamilla")

        input_email = browser.find_element(By.CLASS_NAME, "third")
        input_email.send_keys("kamilla-tazieva@mail.ru")

        input_phone = browser.find_element(By.CSS_SELECTOR, "[placeholder = \"Input your phone\"]")
        input_phone.send_keys("0223279833")

        input_address = browser.find_element(By.CLASS_NAME, "second")
        input_address.send_keys("Kazan")

        button_submit = browser.find_element(By.CLASS_NAME, "btn-")
        button_submit.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Everything is correct")
        browser.quit()
    
if __name__ == "__main__":
    unittest.main()
