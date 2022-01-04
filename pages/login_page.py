from .base_page import BasePage
from .locators  import LoginPageLocators


class LoginPage(BasePage):


	def go_to_login_page(self):
		pass

	def should_be_login_page(self):
		self.should_be_login_url()
		self.should_be_login_form()
		self.should_be_register_form()

	def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
		assert "login" in self.browser.current_url

	def should_be_login_form(self):
		# реализуйте проверку, что есть форма логина
		assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
			"Login form is not presented"

	def should_be_register_form(self):
		# реализуйте проверку, что есть форма регистрации на странице
		assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
			"Register form is not presented"
			
	def register_new_user(self, email, password):
		email_input = self.find(*LoginPageLocators.REG_EMAIL_INPUT)
		email_input.send_keys(email)
		pwd_input = self.find(*LoginPageLocators.REG_PWD_INPUT)
		pwd_input.send_keys(password)
		pwd_conf_input = self.find(*LoginPageLocators.REG_CONF_PWD_INPUT)
		pwd_conf_input.send_keys(password)
		reg_button = self.find(*LoginPageLocators.REG_BUTTON)
		reg_button.click()
		self.should_be_authorized_user()
		
		
