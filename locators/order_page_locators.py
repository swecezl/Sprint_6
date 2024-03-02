from selenium.webdriver.common.by import By


class OrderPageLocators:
    #страница ввода данных пользователя
    HEADER_ORDER_BUTTON = By.XPATH, "//*[@class='Button_Button__ra12g']"
    BIG_ORDER_BUTTON = By.XPATH, "//*[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"
    NAME = By.XPATH, "//*[@placeholder='* Имя']"
    LASTNAME = By.XPATH, "//*[@placeholder='* Фамилия']"
    ADDRESS = By.XPATH, "//*[@placeholder='* Адрес: куда привезти заказ']"
    STATIONS_FIELD = By.XPATH, "//*[@placeholder='* Станция метро']"
    STATION_DROPDOWN = By.XPATH, "//*[contains(@class, 'select-search__select')]/ul/li"
    INPUT_PHONE_NUMBER = By.XPATH, "//*[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT_OR_ORDER_BUTTON = By.XPATH, "//*[@class='Button_Button__ra12g Button_Middle__1CSJM']"

    #страница ввода информации об аренда
    CALENDAR = By.XPATH, "//*[@class='react-datepicker']"
    DATE_FIELD = By.XPATH, "//*[@placeholder='* Когда привезти самокат']"
    RENT_DROPDOWN_MENU = By.XPATH, "//*[@class='Dropdown-placeholder']"
    RENT_DROPDOWN_OPTION_1_DAY = By.XPATH, "(//*[@class='Dropdown-option'])[1]"
    RENT_DROPDOWN_OPTION_3_DAYS = By.XPATH, "(//*[@class='Dropdown-option'])[3]"
    BLACK_SCOOTER = By.XPATH, "//*[@id='black']"
    GREY_SCOOTER = By.XPATH, "//*[@id='grey']"
    COMMENT_FILED = By.XPATH, "//*[@placeholder='Комментарий для курьера']"
    CONFIRM_ORDER_WINDOW = By.XPATH, "//*[@class='Order_Modal__YZ-d3']"
    CONFIRM_ORDER_BUTTON = By.XPATH, "//*[text()='Да']"
    SUCCESS_ORDER_WINDOW = By.XPATH, "//*[contains(class, 'Order_ModalHeader')]"
    CHECK_STATUS_BUTTON = By.XPATH, "//*[text()='Посмотреть статус']"

    #страница созданного заказа
    CANCEL_ORDER_BUTTON = By.XPATH, "//*[contains(@class, 'Track_OrderInfo')]/button[text()='Отменить заказ']"