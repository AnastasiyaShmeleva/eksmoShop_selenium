import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class CatalogPage(Base):
    """ Класс содержащий локаторы и методы для страницы Каталога"""

    # Locators

    popup_age = '//button[@class="popup18__btn popup18__btn_y btn btn_border btn_uc"]'
    cookie_button = '//div[@class="cookie-accept__btn btn btn_small btn_full-width btn_orange"]'
    popular_checkbox_1 = '(//span[@class="checkbox__button checkbox__button_no-bg"])[2]'
    popular_checkbox_2 = '(//span[@class="checkbox__button checkbox__button_no-bg"])[3]'
    availability_checkbox = '(//span[@class="checkbox__button checkbox__button_no-bg"])[4]'
    price_min = '(//input[@name="priceMin"])[2]'
    price_max = '(//input[@name="priceMax"])[2]'
    search_bar_series = '(//input[@class="finder__input"])[4]'
    series_checkbox_1 = '(//div[@class="finder__result-item"])[1]'
    close_button = '//div[@class="finder__close finder__close_showed"]'
    series_checkbox_2 = '(//span[@class="checkbox__button checkbox__button_no-bg"])[36]'
    apply_button = '//a[@class="btn btn_small btn_orange btn_full-width menu-left__filter-submit"]'

    sort_button = '//div[@class="link-drop-down link-drop-down_no-style filter-formats__link-drop-down"]'
    sort_by_price = '(//div[@class="drop-down__item ajs "])[1]'

    product_name_1 = '(//div[@class="book__name"])[1]'
    product_name_2 = '(//div[@class="book__name"])[2]'
    product_price_1 = '(//span[@class="book__price-cur"])[1]'
    product_price_2 = '(//span[@class="book__price-cur"])[2]'
    product_button_1 = '(//button[@class="b24-btn _small _block"])[1]'
    product_button_2 = '(//button[@class="b24-btn _small _block"])[2]'
    basket_button = '//span[@class="book24-widget-basket-mini__counter count"]'

    # Getters

    def get_cookie_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cookie_button)))

    def get_popular_checkbox_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.popular_checkbox_1)))

    def get_popular_checkbox_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.popular_checkbox_2)))

    def get_availability_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.availability_checkbox)))

    def get_price_min(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.price_min)))

    def get_price_max(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_max)))

    def get_search_bar_series(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.search_bar_series)))

    def get_series_checkbox_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.series_checkbox_1)))

    def get_close_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.close_button)))

    def get_series_checkbox_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.series_checkbox_2)))

    def get_apply_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.apply_button)))

    def get_sort_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.sort_button)))

    def get_sort_by_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.sort_by_price)))

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

    def get_product_button_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_button_1)))

    def get_product_button_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_button_2)))

    def get_basket_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.basket_button)))

    # Actions

    def click_cookie_button(self):
        self.get_cookie_button().click()
        print('Click cookie button')

    def click_popular_checkbox_1(self):
        self.get_popular_checkbox_1().click()
        print('Click popular checkbox 1')

    def click_popular_checkbox_2(self):
        self.get_popular_checkbox_2().click()
        print('Click popular checkbox 2')

    def click_availability_checkbox(self):
        self.get_availability_checkbox().click()
        print('Click availability checkbox')

    def input_price_min(self):
        for _ in range(5):
            self.get_price_min().send_keys(Keys.ARROW_UP)
        print('Input price min')

    def input_price_max(self):
        self.get_price_max().send_keys('2000')
        print('Input price max')

    def input_search_bar_series(self):
        self.get_search_bar_series().send_keys('энциклопедии')
        print('Input search bar series')

    def click_series_checkbox_1(self):
        self.get_series_checkbox_1().click()
        print('Click series checkbox 1')

    def click_close_button(self):
        self.get_close_button().click()
        print('Click close button')

    def click_series_checkbox_2(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_series_checkbox_2()).click().perform()
        print('Click series checkbox 2')

    def click_apply_button(self):
        self.get_apply_button().click()
        print('Click apply button')

    def move_to_sort_button(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_sort_button()).perform()
        print('Move to sort button')

    def click_sort_by_price(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_sort_by_price()).click().perform()
        print('Click sort by price')

    def get_product_data_1(self):
        name = self.get_product_name_1().text
        price = self.convert_to_number(self.get_product_price_1())
        print(f'Name product 1: {name}')
        print(f'Price product 1: {price}')

        return [name, price]

    def get_product_data_2(self):
        name = self.get_product_name_2().text
        price = self.convert_to_number(self.get_product_price_2())
        print(f'Name product 2: {name}')
        print(f'Price product 2: {price}')

        return [name, price]

    def click_product_button_1(self):
        self.get_product_button_1().click()
        print('Click product button 1')

    def click_product_button_2(self):
        self.get_product_button_2().click()
        print('Click product button 2')

    def click_basket_button(self):
        self.get_basket_button().click()
        print('Click basket button')

    # Methods

    def filter_catalog(self):
        self.get_current_url()
        self.assert_url('https://eksmo.ru/deti-i-roditeli/detskie-entsiklopedii/')
        self.click_popular_checkbox_1()
        self.click_popular_checkbox_2()
        self.driver.execute_script("window.scrollTo(0, 300);")
        self.click_availability_checkbox()
        self.input_price_min()
        self.input_price_max()
        self.driver.execute_script("window.scrollTo(0, 1300);")
        time.sleep(2)
        self.input_search_bar_series()
        self.click_series_checkbox_1()
        time.sleep(2)
        self.click_series_checkbox_2()
        self.click_cookie_button()
        self.click_apply_button()

    def sort_result(self):
        self.move_to_sort_button()
        time.sleep(2)
        self.click_sort_by_price()

    def select_products(self):
        product_1 = self.get_product_data_1()
        product_2 = self.get_product_data_2()
        self.click_product_button_1()
        time.sleep(2)
        self.click_product_button_2()
        self.click_basket_button()

        return product_1, product_2
