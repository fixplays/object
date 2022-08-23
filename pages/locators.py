from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inv")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CLASS_NAME, "icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_BUTTON = (By.ID, "login_link")
    EMAIL_INPUT = (By.NAME, "registration-email")
    PASSWORD_INPUT = (By.NAME, "registration-password1")
    REPEAT_PASSWORD_INPUT = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    ADDING_SUCCESS = (By.CSS_SELECTOR, "div.alert-success")
    ALERT_ADDED_TO_BASKET = (By.CSS_SELECTOR,
                           "#messages>div:first-child .alertinner strong")
    ALERT_BASKET_STATUS = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")
    PRICE_VALUE = (By.CLASS_NAME, "price_color")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")


class BasketPageLocators:
    BASKET_ELEMENT = (By.CLASS_NAME, "basket-items")
    BASKET_EMPTY_TEXT_ELEMENT = (By.CSS_SELECTOR, "div#content_inner > p")
