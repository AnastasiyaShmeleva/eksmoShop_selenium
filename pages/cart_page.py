from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class CartPage(Base):
    """ Класс содержащий локаторы и методы для страницы Корзины"""

    # Locators

    product_name_1 = '(//a[@class="basket-product-item__name-link smartLink"])[1]'
    product_name_2 = '(//a[@class="basket-product-item__name-link smartLink"])[2]'
    product_price_1 = '(//div[@class="product-prices-block__price _sale"])[1]'
    product_price_2 = '(//div[@class="product-prices-block__price _sale"])[2]'
    final_price = '(//span[@class="nobr"])[3]'
    checkout_button = '//button[@class="b24-btn _large _block"]'

    # Getters

    def get_product_name_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.product_name_1)))

    def get_product_name_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.product_name_2)))

    def get_product_price_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.product_price_1)))

    def get_product_price_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.product_price_2)))

    def get_final_cost(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.final_price)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.checkout_button)))

    # Actions

    def check_product_data_1(self, product_1):
        print('Check product data 1')
        self.check_product_data(self.get_product_name_1(), self.get_product_price_1(), product_1)

    def check_product_data_2(self, product_2):
        print('Check product data 2')
        self.check_product_data(self.get_product_name_2(), self.get_product_price_2(), product_2)

    def check_final_cost(self):
        price_1 = self.convert_to_number(self.get_product_price_1())
        price_2 = self.convert_to_number(self.get_product_price_2())

        self.check_total_price(price_1, price_2, self.get_final_cost())

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Click checkout button')

    # Methods

    def product_data(self, product_1, product_2):
        self.get_current_url()
        self.assert_url('https://eksmo.ru/cart/#/personal/cart')
        self.check_product_data_1(product_1)
        self.check_product_data_2(product_2)
        self.check_final_cost()
        self.click_checkout_button()
