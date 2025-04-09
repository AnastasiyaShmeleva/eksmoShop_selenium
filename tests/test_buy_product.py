import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.checkout_page import CheckoutPage
from pages.main_page import MainPage


def test_buy_product(set_up):
    """Тест по покупке товаров включает:
         в себя фильтрацию и сортировку каталога, выбор товара, авторизацию."""

    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['pageLoadStrategy'] = 'eager'
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.page_load_strategy = 'eager'
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    # Переходим в раздел каталога энциклопедии
    mp = MainPage(driver)
    mp.select_catalog_section()

    # Фильтруем раздел по наличию, цене, серии. Сортируем по цене
    cp = CatalogPage(driver)
    cp.filter_catalog()
    cp.sort_result()

    # Добавляем товары в корзину
    product_1, product_2 = cp.select_products()

    time.sleep(2)

    # Проверяем добавленные товары
    crp = CartPage(driver)
    crp.product_data(product_1, product_2)

    # Переходим на страницу оформления и авторизуемся
    chp = CheckoutPage(driver)
    chp.authorization()

    # Проверяем итоговую стоимость
    chp.check_data(product_1, product_2)

    time.sleep(5)

    driver.quit()
