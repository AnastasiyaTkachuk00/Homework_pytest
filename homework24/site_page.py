from base_page1 import BasePage
from selenium.webdriver.common.by import By


class SearchLocators:
    cart_button = (By.CSS_SELECTOR, '//div[@class = "shopping_cart"] /a')
    cart_message = (By.CSS_SELECTOR, '#center_column > p')
    sign_in_page = (By.CSS_SELECTOR, '//div[@class = "header_user_info"] /a')
    search_field = (By.CSS_SELECTOR, '#search_query_top')
    search_button = (By.CSS_SELECTOR, '#searchbox > button')
    contact_us_button = (By.CSS_SELECTOR, '#contact-link a')
    women_button = (By.CSS_SELECTOR, 'li.sfHover  > a')


class SearchHelper(BasePage):

    def click_on_the_cart(self):
        return self.find_element(SearchLocators.cart_button)

    def check_empty_cart_page(self):
        return self.find_element(SearchLocators.cart_message)

    def click_on_the_login_button(self):
        return self.find_element(SearchLocators.sign_in_page)

    def click_on_the_search_field(self):
        return self.find_element(SearchLocators.search_field)

    def click_on_the_search_button(self):
        return self.find_element(SearchLocators.search_button)

    def click_on_the_contact_us_button(self):
        return self.find_element(SearchLocators.contact_us_button)

    def click_on_the_women_button(self):
        return self.find_element(SearchLocators.women_button)
    
