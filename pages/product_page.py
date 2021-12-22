import time
from .base_page import BasePage
from .locators  import ProductPageLocators, \
                       BasePageLocators, \
                       BasketPageLocators

class ProductPage(BasePage):
	
	def should_be_add_product_to_basket(self):
	
		product_name = self.find(*ProductPageLocators.PRODUCT_NAME)
		product_name_text = product_name.text
		
		product_price = self.find(*ProductPageLocators.PRODUCT_PRICE)
		product_price_text = product_price.text
	
		add_button = self.find(*ProductPageLocators.ADD_PRODUCT_BUTTON)
		add_button.click()
		self.solve_quiz_and_get_code()
		
		time.sleep(10)
		
		busket_button = self.find(*BasePageLocators.BASKET_BUTTON)
		busket_button.click()
		
		first_item_name = self.find(*BasketPageLocators.FIRST_ITEM_NAME)
		first_item_name_text = first_item_name.text
		
		total_cost = self.find(*BasketPageLocators.TOTAL_COST)
		total_cost_value = total_cost.text
		
		assert (product_name_text  == first_item_name_text) and \
		       (product_price_text == total_cost_value)
		
		       
	def should_not_be_success_message_after_adding_product(self):
		add_button = self.find(*ProductPageLocators.ADD_PRODUCT_BUTTON)
		add_button.click()
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
		"Success message is presented, but should not be"
    
    
	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
		"Success message is presented, but should not be"
    

	def should_be_disappeared_after_adding_product(self):
		add_button = self.find(*ProductPageLocators.ADD_PRODUCT_BUTTON)
		add_button.click()
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
		"Success message is not disappeared, but should be disappeared"
       
       	
