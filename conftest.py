import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

def pytest_addoption(parser):
	parser.addoption("--language"    , action="store", default = "fr")
	parser.addoption("--browser_name", action="store", default = "chrome")
	

@pytest.fixture(scope="function")	
def browser(request):
	
	browser_name = request.config.getoption("browser_name")
	language     = request.config.getoption("language")
	
	if browser_name == "chrome": 
		options = Options()
		options.add_experimental_option(
			'prefs', 
			{'intl.accept_languages': language}
		)
		
		browser = webdriver.Chrome(options=options) 
	    
	     
	if browser_name == "firefox":
	
		fp = webdriver.FirefoxProfile()
		fp.set_preference("intl.accept_languages", language)
		
		browser = webdriver.Firefox(firefox_profile=fp)
	
	yield browser
	
	time.sleep(2)
	browser.quit() 
