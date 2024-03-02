import pytest
import allure
from data import *
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверка выпадающего списка вопросов-ответов в разделе "Вопросы о важном"')
    @allure.description('На главной странице переходим к разделу "Вопросы о важном", поочередно нажимаем на вопросы при разворачивании выполняется отображение соответствующего текста')
    @pytest.mark.parametrize(
        "index,text", Answers.ANSWERS_LIST)
    def test_click_on_question_and_get_answer_text(self, driver, index, text):
        main_page = MainPage(driver)
        main_page.open_page(Urls.main_page_url)
        main_page.scroll_to_element(MainPageLocators.FAQ)
        main_page.click_question(index)
        answer = main_page.get_answer_text()
        assert answer == text, f'Ответ на вопрос {index} соответствуют соответствует требованиям'