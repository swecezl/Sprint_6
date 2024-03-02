from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure


class BasePage:

    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу {url}')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Прокручиваем страницу к элементу {locator}')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Нажимаем на элемент {locator}')
    def click_element(self, *locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()

    @allure.step('Ожидаем отображение элемента {locator}')
    def find_element_with_wait(self, *locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ищем текст в элементе {locator}')
    def get_element_text(self, locator):
        element = self.find_element_with_wait(*locator)
        return element.text
