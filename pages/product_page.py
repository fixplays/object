from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self, is_promo=False) -> None:
        self.browser.find_element(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET).click()

        if is_promo:
            self.solve_quiz_and_get_code()

    def should_be_present_in_basket(self) -> None:
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME), "Product name is not present"
        assert self.is_element_present(
            *ProductPageLocators.ALERT_ADDED_TO_BASKET
        ), "No alert that a product has been added to basket"
        alert_text = self.browser.find_element(
            *ProductPageLocators.ALERT_ADDED_TO_BASKET).text
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        assert product_name == alert_text, \
            f"The alert contains wrong product name: {alert_text} - {product_name}"

    def should_check_overall_cost(self) -> None:
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_PRICE), "Product price is not present"
        assert self.is_element_present(*ProductPageLocators.ALERT_ADDED_TO_BASKET
                                       ), "No alert with basket status"
        alert_text = self.browser.find_element(
            *ProductPageLocators.ALERT_BASKET_STATUS).text.split()[-1]
        product_cost = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        assert product_cost == alert_text, \
            f"Product cost in basket is not equal to the product cost {alert_text} != {product_cost}"

    def should_not_see_success_message_after_adding_to_basket(self) -> None:
        assert self.is_not_element_present(
            *ProductPageLocators.ADDING_SUCCESS
        ), "Success element is visible for an user"

    def should_not_see_success_message_upon_opening_product_page(self) -> None:
        assert self.is_not_element_present(
            *ProductPageLocators.ADDING_SUCCESS
        ), "Success element is visible for an user"

    def should_disappeared_success_message(self) -> None:
        assert self.is_disappeared(*ProductPageLocators.ADDING_SUCCESS
                                   ), "Success message has not disappeared"