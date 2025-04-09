import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class CheckoutPage(Base):
    """ Класс содержащий локаторы и методы для страницы Оформления заказа"""

    # Locators

    email_button = '//div[@class="btn btn_border-bold btn_font-medium btn_full-width auth-form__link-mail"]'
    email = '//input[@name="USER_LOGIN"]'
    password = '//input[@name="USER_PASSWORD"]'
    login_button = '//button[@class="btn btn_orange btn_full-width btn_font-medium auth-form__submit"]'
    final_price = '(//span[@class="nobr"])[4]'

    # Getters

    def get_email_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.email_button)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_final_cost(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.final_price)))

    # Actions

    def click_email_button(self):
        self.get_email_button().click()
        print('Click email button')

    def input_email(self):
        self.get_email().send_keys('shmeleva.nastya98@mail.ru')
        print('Input email')

    def input_password(self):
        self.get_password().send_keys('2WFQuB@AmG9cFrz')
        print('Input password')

    def click_login_button(self):
        self.get_login_button().click()
        print('Click login button')

    def check_final_cost(self, product_1, product_2):
        self.check_total_price(product_1[1], product_2[1], self.get_final_cost())

    # Methods

    def authorization(self):
        self.get_current_url()
        self.assert_url('https://eksmo.ru/cart/#/personal/order/make')
        self.click_email_button()
        self.input_email()
        self.input_password()
        self.click_login_button()

    def check_data(self, product_1, product_2):
        time.sleep(2)
        self.check_final_cost(product_1, product_2)
        self.get_screenshot()
