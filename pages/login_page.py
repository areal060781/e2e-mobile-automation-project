from .base_page import BasePage
from conf.locators import LoginPageLocators


class LoginPage(BasePage):
    def set_email(self, email):
        email_input = self.driver.find_element(*LoginPageLocators.EMAIL_INPUT)
        assert email_input is not None

        #email_input.click()
        #self.driver.execute_script('mobile:type', {'text': email})

        email_input.send_keys(email).click()
        self.driver.execute_script('mobile: performEditorAction', {'action': 'done'})

    def set_password(self, password):
        password_input = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        assert password_input is not None

        password_input.send_keys(password).click()
        self.driver.execute_script('mobile: performEditorAction', {'action': 'done'})

    def click_login_button(self):
        login_button = self.driver.find_element(*LoginPageLocators.LOG_IN_BUTTON)
        assert login_button is not None
        login_button.click()
