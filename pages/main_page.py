from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure


class MainPage(BasePage):

    def get_questions(self):
        return self.driver.find_elements(*MainPageLocators.QUESTION)

    @allure.step('Кликаем на вопрос')
    def click_question(self, index):
        questions = self.get_questions()
        questions[index].click()

    @allure.step('Получаем ответ')
    def get_answer_text(self):
        return self.driver.find_element(*MainPageLocators.ANSWER).text

    @allure.step('Открываем главную страницу, нажав на логотип "Самокат"')
    def open_main_page_by_logo(self):
        self.click_element(*MainPageLocators.SCOOTER_LOGO)

    @allure.step('Открываем страницу Дзен, нажав на логотип "Яндекс"')
    def open_yandex_page_by_logo(self):
        self.click_element(*MainPageLocators.YANDEX_LOGO)

    @allure.step('Проверяем, что на главной странице есть элемент "Как это работает"')
    def check_home_text(self):
        self.scroll_to_element(MainPageLocators.HOW_IT_WORKS)
        return self.get_element_text(MainPageLocators.HOW_IT_WORKS)

    def wait_for_new_tab(self, number):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(number))
