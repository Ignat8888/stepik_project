import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page  import BasketPage
from .pages.login_page   import LoginPage

@pytest.mark.skip
@pytest.mark.parametrize('promo', ["0",
                                   "1",
                      pytest.param("10", marks=pytest.mark.xfail)])
def test_guest_can_add_product_to_basket(browser, promo):
	link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_add_product_to_basket()


@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = "https://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
	page = ProductPage(browser, link)
	page.open()
	page.should_not_be_success_message_after_adding_product()
	
	
@pytest.mark.skip	
def test_guest_cant_see_success_message(browser):
	link = "https://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
	page = ProductPage(browser, link)
	page.open()
	page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
	link = "https://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_disappeared_after_adding_product()
	

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()
	
@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_go_to_login_page()
	

@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
	page = BasketPage(browser, link)
	page.open()
	page.should_be_empty_basket()	



class TestUserAddToBasketFromProductPage():

	@pytest.fixture(scope="function")
	def setup(self, browser):
		link = "https://selenium1py.pythonanywhere.com/accounts/login/"
		email      = str(time.time()) + "@fakemail.org"
		password   = "qqkdlv1934"
		print(f"\nSetup: new email is {email}")
		print(f"Setup: new password is {password}")
		page = LoginPage(browser, link)
		page.open()
		page.register_new_user(email, password)

	
	def test_user_cant_see_success_message(self, browser, setup):
		link = "https://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
		page = ProductPage(browser, link)
		page.open()
		page.should_not_be_success_message()
		
		

	def test_user_can_add_product_to_basket(self, browser, setup):
		link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
		page = ProductPage(browser, link)
		page.open()
		page.should_be_add_product_to_basket()
	
