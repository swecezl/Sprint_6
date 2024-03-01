from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION = By.XPATH, "//*[contains(@class, 'accordion__item')]"
    ANSWER = By.XPATH, "//*[contains(@class, 'accordion__panel') and not(@hidden)]"
    FAQ = By.XPATH, '//*[@class="accordion"]'
    SCOOTER_LOGO = By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR > img:nth-child(1)"
    YANDEX_LOGO = By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI > img:nth-child(1)"
    HOME_HEADER = By.XPATH, "//*[@id='root']/div/div/div[2]/div[4]/text()[1]"
    YANDEX_SEARCHBAR = By.XPATH, "/html/body/form/input[1]"
    HOW_IT_WORKS = By.XPATH, "/html/body/div/div/div/div[4]/div[1]"
