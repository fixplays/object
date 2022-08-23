from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Wrong URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is not Presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register Form is not Presented"

    def register_new_user(self, email: str, password: str) -> None:
        self.browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(
            email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(
            password)
        self.browser.find_element(
            *LoginPageLocators.REPEAT_PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
