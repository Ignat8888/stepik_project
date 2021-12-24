from .base_page import BasePage
from .locators  import BasePageLocators, \
					   BasketPageLocators


class BasketPage(BasePage):

	def __init__(self, *args, **kwargs):
		super(BasketPage, self).__init__(*args, **kwargs)
	
	def should_be_empty_basket(self):
		basket_button = self.find(*BasePageLocators.BASKET_BUTTON)
		basket_button.click()
		assert self.is_not_element_present(*BasketPageLocators.ITEMS_FORM), \
		"Items form is presented, but should not be"
		assert self.is_element_present(*BasketPageLocators.MESSAGE_OF_EMPTY_BASKET)

