import pytest
from .pages.product_page import ProductPage

@pytest.mark.skip
@pytest.mark.parametrize('promo', ["0",
                                   "1",
                      pytest.param("10", marks=pytest.mark.xfail)])
def test_guest_can_add_product_to_basket(browser, promo):
	link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_add_product_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = "https://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
	page = ProductPage(browser, link)
	page.open()
	page.should_not_be_success_message_after_adding_product()
	
	
def test_guest_cant_see_success_message(browser):
	link = "https://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
	page = ProductPage(browser, link)
	page.open()
	page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
	link = "https://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_disappeared_after_adding_product()
	
