from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class MainPage(Base):
    """ Класс содержащий локаторы и методы для Главной страницы"""

    url = 'https://eksmo.ru/'

    # Locators

    catalog_button = '//a[@class="cmenu__link menu2__link1"]'
    catalog_section = '(//a[@class="mega-menu__link "])[27]'

    # Getters

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_catalog_section(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_section)))

    # Actions

    def move_to_catalog_button(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_catalog_button()).perform()
        print('Move to computers section')

    def click_catalog_section(self):
        self.get_catalog_section().click()
        print('Click catalog section')

    # Methods

    def select_catalog_section(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.move_to_catalog_button()
        self.click_catalog_section()
