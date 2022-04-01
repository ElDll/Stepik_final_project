import pytest
from .pages.product_page import ProductPage
import time


@pytest.mark.parametrize('number', ["0", "1", "2", "3", "4", "5", "6",
                                    pytest.param("7", marks=pytest.mark.xfail(reason="maybe we fixed it")),
                                    "8", "9"])
def test_guest_can_add_product_to_basket(browser, number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.click_the_button()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.we_have_message_price()
    page.we_have_message_name()
