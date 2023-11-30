from selenium import webdriver
from selenium.webdriver.common.by import By  

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
    
    
# вызов Google Chrome
# pytest -s -v --browser_name=chrome test_parser.py
    
# вызов Mozilla
# pytest -s -v --browser_name=firefox test_parser.py