from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conf.capabilities import LOADING_INDICATOR_WAIT
from conf.locators import BasePageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def wait_for_loading_indicator(self):
        wait = WebDriverWait(self.driver, LOADING_INDICATOR_WAIT)

        # valor = wait.until(EC.visibility_of_element_located(
        #     (MobileBy.ACCESSIBILITY_ID, 'textIndicator')))

        wait.until(EC.invisibility_of_element_located(
            BasePageLocators.LOADING_INDICATOR))
