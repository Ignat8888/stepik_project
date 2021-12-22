from selenium.webdriver.common.by import By

class BasePageLocators():
	TEXT_HTML     = (By.XPATH, "//*")
	#pageSource = self.find(*BasePageLocators.TEXT_HTML).get_attribute("outerHTML")
	#print(pageSource)
	BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class MainPageLocators():
	pass
	
class LoginPageLocators():
	LOGIN_FORM    = (By.CSS_SELECTOR, ".login_form") 
	REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
	
class ProductPageLocators():
	ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
	PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
	SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alertinner '][contains(text()[2],'был добавлен')]")
	
class BasketPageLocators():
	FIRST_ITEM_NAME = (By.CSS_SELECTOR, ".basket-items .col-sm-4 a")
	TOTAL_COST = (By.CSS_SELECTOR, "#basket_totals .align-right") 
