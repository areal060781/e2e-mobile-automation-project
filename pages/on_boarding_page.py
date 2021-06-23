from .base_page import BasePage
from conf.locators import OnBoardingLocators


class OnBoardingPage(BasePage):

    def click_skip_link(self):
        skip_link = self.driver.find_element(*OnBoardingLocators.SKIP_LINK)
        assert skip_link is not None
        skip_link.click()
