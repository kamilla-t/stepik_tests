from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.locators import LoginPageLocators

#класс MainPage делаем наследником класса BasePage
class MainPage(BasePage):

    # def go_to_login_page(self):
    #     login_link = self.browser.find_element(By.CSS_SELECTOR, "#registration_link")
    #     login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login link is not presented"


    # def should_be_login_link(self):
    #     assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"