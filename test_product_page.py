import pytest
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage



links = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
]

offer_link_template = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
offer_links = [f"{offer_link_template}{i}" for i in range(0, 10)]

product_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, faker):
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(faker.email(), faker.password())
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser) -> None:
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.add_to_basket(True)
        product_page.should_not_see_success_message_upon_opening_product_page()

    @pytest.mark.need_review
    @pytest.mark.parametrize("link", links)
    def test_user_can_add_product_to_basket(self, browser, link: str) -> None:
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket(True)
        product_page.should_be_present_in_basket()
        product_page.should_check_overall_cost()


@pytest.mark.need_review
@pytest.mark.parametrize("link", links)
def test_guest_can_add_product_to_basket(browser, link: str) -> None:
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket(True)
    product_page.should_be_present_in_basket()
    product_page.should_check_overall_cost()


@pytest.mark.skip
@pytest.mark.parametrize("link", offer_links)
def test_guest_can_add_product_to_basket_with_different_offer_numbers(
        browser, link: str) -> None:
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket(True)
    product_page.should_be_present_in_basket()
    product_page.should_check_overall_cost()


def test_guest_can_add_non_promo_product_to_basket(browser) -> None:
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_be_present_in_basket()
    product_page.should_check_overall_cost()


def test_guest_cant_see_success_message(browser) -> None:
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_not_see_success_message_upon_opening_product_page()


def test_guest_should_see_login_link_on_product_page(browser) -> None:
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser) -> None:
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser
                                                                 ) -> None:
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()
    basket_page.should_contain_empty_text()
