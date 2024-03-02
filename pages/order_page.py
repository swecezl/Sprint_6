from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import allure


class OrderPage(BasePage):

    @allure.step('Кликаем на кнопку "Заказать" в хедере страницы')
    def click_header_order_button(self):
        self.driver.find_element(*OrderPageLocators.HEADER_ORDER_BUTTON).click()

    @allure.step('Кликаем на кнопку "Заказать" под блоком "Как это работает"')
    def click_big_order_button(self):
        self.scroll_to_element(OrderPageLocators.BIG_ORDER_BUTTON)
        self.find_element_with_wait(*OrderPageLocators.BIG_ORDER_BUTTON)
        self.click_element(*OrderPageLocators.BIG_ORDER_BUTTON)

    @allure.step('Вводим имя')
    def input_name(self, name):
        self.find_element_with_wait(*OrderPageLocators.NAME).send_keys(name)

    @allure.step('Вводим фамилию')
    def input_lastname(self, lastname):
        self.find_element_with_wait(*OrderPageLocators.LASTNAME).send_keys(lastname)

    @allure.step('Вводим адрес')
    def input_address(self, address):
        self.find_element_with_wait(*OrderPageLocators.ADDRESS).send_keys(address)

    @allure.step('Выбираем станцию метро')
    def set_station(self, station):
        self.find_element_with_wait(*OrderPageLocators.STATIONS_FIELD).send_keys(station)
        self.find_element_with_wait(*OrderPageLocators.STATION_DROPDOWN).click()

    @allure.step('Вводим номер телефона')
    def input_phone_number(self, phone_number):
        self.find_element_with_wait(*OrderPageLocators.INPUT_PHONE_NUMBER).send_keys(phone_number)

    @allure.step('Нажимаем на кнопку перехода к следующему этапу заказа')
    def click_next_or_order_button(self):
        self.find_element_with_wait(*OrderPageLocators.NEXT_OR_ORDER_BUTTON).click()

    def input_creds(self, test_user_1):
        self.click_header_order_button()
        self.input_name(test_user_1.get('name'))
        self.input_lastname(test_user_1.get('lastname'))
        self.input_address(test_user_1.get('address'))
        self.set_station(test_user_1.get('station'))
        self.input_phone_number(test_user_1.get('phone_number'))
        self.click_next_or_order_button()

    @allure.step('Указываем дату')
    def set_date(self, date):
        self.find_element_with_wait(*OrderPageLocators.DATE_FIELD).send_keys(date)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.CALENDAR))
        self.find_element_with_wait(*OrderPageLocators.DATE_FIELD).send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element(OrderPageLocators.CALENDAR))

    @allure.step('Открываем выпадающее меню со сроком действия аренды')
    def open_rent_period(self):
        self.click_element(*OrderPageLocators.RENT_DROPDOWN_MENU)

    @allure.step('Выбираем цвет самоката')
    def set_scooter(self, color):
        self.click_element(*color)

    @allure.step('Выбираем период аренды')
    def set_rent_period(self, period):
        self.click_element(*period)

    @allure.step('Вводим комментарий к заказу')
    def input_rent_comment(self, comment):
        self.find_element_with_wait(*OrderPageLocators.COMMENT_FILED).send_keys(comment)

    @allure.step('Подтверждаем заказ')
    def confirm_order(self):
        self.find_element_with_wait(*OrderPageLocators.CONFIRM_ORDER_WINDOW)
        self.click_element(*OrderPageLocators.CONFIRM_ORDER_BUTTON)
        self.click_element(*OrderPageLocators.CHECK_STATUS_BUTTON)

    def check_order_status(self):
        self.find_element_with_wait(*OrderPageLocators.CANCEL_ORDER_BUTTON)

    def input_rent_info(self, date, rent_info):
        color_checkbox = {"black": OrderPageLocators.BLACK_SCOOTER, "grey": OrderPageLocators.GREY_SCOOTER}
        day_period = {'one': OrderPageLocators.RENT_DROPDOWN_OPTION_1_DAY,
                      'three': OrderPageLocators.RENT_DROPDOWN_OPTION_3_DAYS}
        self.set_date(date)
        self.open_rent_period()
        self.set_rent_period(day_period.get(rent_info.get('day')))
        self.set_scooter(color_checkbox.get(rent_info.get('color')))
        self.input_rent_comment(rent_info.get('comment'))
        self.click_next_or_order_button()

    def complete_order(self):
        self.confirm_order()
        self.check_order_status()

    def cancel_order_text(self):
        return self.get_element_text(OrderPageLocators.CANCEL_ORDER_BUTTON)
