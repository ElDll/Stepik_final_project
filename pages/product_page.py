from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_the_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def we_have_message_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_name = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME).text
        assert message_name == product_name, "Incorrect name"


    def we_have_message_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text
        assert message_price == product_price, "Incorrect price"