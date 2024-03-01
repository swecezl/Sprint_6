import pytest
import allure
from data import *
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Оформление заказа по кнопке "Заказать" в шапке страницы')
    @allure.description('Проверяем создание заказа и переход на страницу успешно созданного заказа')
    def test_order_flow_header_order_button(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.main_page_url)
        order_page.click_header_order_button()
        order_page.input_creds(Users.test_user_1)
        order_page.click_next_or_order_button()
        order_page.input_rent_info(date_today, RentInfo.test_user_1)
        order_page.complete_order()
        assert TextData.cancel_order_text in order_page.cancel_order_text(), f'Заказ успешно создан'

    @allure.title('Оформление заказа по большой копке "Заказать" в середине главной страницы')
    @allure.description('Проверяем создание заказа и переход на страницу успешно созданного заказа')
    def test_order_flow_big_order_button(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.main_page_url)
        order_page.click_big_order_button()
        order_page.input_creds(Users.test_user_2)
        order_page.click_next_or_order_button()
        order_page.input_rent_info(date_tomorrow, RentInfo.test_user_2)
        order_page.complete_order()
        assert TextData.cancel_order_text in order_page.cancel_order_text(), f'Заказ успешно создан'