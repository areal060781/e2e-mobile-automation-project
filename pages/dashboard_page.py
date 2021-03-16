from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from conf.locators import DashboardPageLocators


class DashboardPage(BasePage):

    def validate_welcome_message(self, name):
        auditor_name_text = self.driver.find_element(*DashboardPageLocators.AUDITOR_NAME_TEXT)

        # wait = WebDriverWait(self.driver, 20)
        # auditor_name_text = wait.until(EC.presence_of_element_located(
        #     (MobileBy.ACCESSIBILITY_ID, 'auditorNameText')))

        assert auditor_name_text is not None
        assert auditor_name_text.text == name

    def wait_for_loading_indicator(self):
        wait = WebDriverWait(self.driver, 70)

        # valor = wait.until(EC.visibility_of_element_located(
        #     (MobileBy.ACCESSIBILITY_ID, 'textIndicator')))

        wait.until(EC.invisibility_of_element_located(
            DashboardPageLocators.LOADING_INDICATOR))
