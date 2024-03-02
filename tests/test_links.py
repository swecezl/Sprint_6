import pytest
from data import *
from pages.main_page import MainPage
import allure


class TestLinks:

    @allure.title('Проверяем переход на главную страницу через клик по лого')
    @allure.description('Нажимаем на иконку логотипа со страницы создания заказа')
    def test_open_main_page_from_order_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.order_page_url)
        main_page.open_main_page_by_logo()
        current_how_it_works_text = main_page.check_home_text()
        assert TextData.how_it_works_text == current_how_it_works_text and driver.current_url == Urls.main_page_url, f'Успешно перешли на главную страницу'

    @allure.title('Проверяем переход на страниу Дзена через клик по лого')
    @allure.description('Нажимаем на иконку логотипа с главной страницы')
    def test_yandex_page_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.main_page_url)
        main_page.open_yandex_page_by_logo()
        main_page.wait_for_new_tab(2)
        assert driver.current_url == Urls.main_page_url, f'Успешно перешли на страницу Дзена'
