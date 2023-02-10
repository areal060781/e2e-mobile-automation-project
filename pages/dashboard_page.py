from .base_page import BasePage
from conf.locators import DashboardPageLocators


class DashboardPage(BasePage):
    """Dashboard page action methods come here"""

    def validate_welcome_message(self, name):
        auditor_name_text = self.driver.find_element(*DashboardPageLocators.AUDITOR_NAME_TEXT)

        # wait = WebDriverWait(self.driver, 20)
        # auditor_name_text = wait.until(EC.presence_of_element_located(
        #     (MobileBy.ACCESSIBILITY_ID, 'auditorNameText')))

        assert auditor_name_text is not None

        assert auditor_name_text.text.strip() == name
