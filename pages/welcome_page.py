from .base_page import BasePage
from conf.locators import WelcomePageLocators


class WelcomePage(BasePage):
    def click_login_button(self):
        login_button = self.driver.find_element(*WelcomePageLocators.LOG_IN_BUTTON)
        assert login_button is not None
        login_button.click()
