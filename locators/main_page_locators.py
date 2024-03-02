from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION = By.XPATH, "//*[contains(@class, 'accordion__item')]"
    ANSWER = By.XPATH, "//*[contains(@class, 'accordion__panel') and not(@hidden)]"
    FAQ = By.XPATH, '//*[@class="accordion"]'
    SCOOTER_LOGO = By.XPATH, "//*[@alt='Scooter']"
    YANDEX_LOGO = By.XPATH, "//*[@alt='Yandex']"
    HOW_IT_WORKS = By.XPATH, "//*[text()='Как это работает']"
