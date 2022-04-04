import pytest

from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
import time


#@pytest.mark.parametrize('number', ["0", "1", "2", "3", "4", "5", "6",
                                    #pytest.param("7", marks=pytest.mark.xfail(reason="maybe we fixed it")),
                                    #"8", "9"])
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.click_the_button()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.we_have_message_price()
    page.we_have_message_name()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_the_button()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_the_button()
    page.should_be_disappear_message()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.we_dont_have_items_in_basket()
    basket_page.should_we_have_empty_basket_message()

@pytest.mark.register
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(str(time.time()) + "@fakemail.org", "sswwssww1")
        browser.implicitly_wait(10)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        browser.implicitly_wait(10)
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()  # открываем страницу
        page.click_the_button()
        browser.implicitly_wait(3)
        page.we_have_message_price()
        page.we_have_message_name()