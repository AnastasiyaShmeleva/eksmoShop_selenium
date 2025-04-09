import datetime


class Base:
    """ Базовый класс, содержащий универсальные методы """

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Метод проверки url"""

        get_url = self.driver.current_url
        print("current url " + get_url)

    def get_screenshot(self):
        """Создание скриншота"""

        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = "screenshot " + now_date + ".png"
        self.driver.save_screenshot(f"screen/{name_screenshot}")
        print("Скриншот выполнен")

    def assert_url(self, result):
        """Проверка корректности URL"""

        get_url = self.driver.current_url
        print(get_url)

        assert result == get_url
        print("Корректная URL")

    @staticmethod
    def convert_to_number(result):
        """Преобразование строки в число"""

        num = int(result.text.replace(' ', '').replace('р.', '').replace('₽', ''))
        print(num)

        return num

    def check_product_data(self, element_name, element_price, result):
        """Проверка названия и цены товара"""

        name = element_name.text
        price = self.convert_to_number(element_price)

        assert name == result[0], f'Неправильное имя товара: {name}. Ожидаем: {result[0]}'
        assert price == result[1], f'Неправильная цена товара: {price}. Ожидаем: {result[1]}'
        print('Имя и цена товара корректные')

    def check_total_price(self, price_1, price_2, total_price):
        """Проверка итоговой стоимости"""

        sum_price = price_1 + price_2

        final_price = self.convert_to_number(total_price)

        assert sum_price == final_price, (f'Неправильная стоимость! Сумма товаров: {sum_price}, '
                                          f'итоговая стоимость: {final_price}')
        print('Итоговая стоимость верна')
