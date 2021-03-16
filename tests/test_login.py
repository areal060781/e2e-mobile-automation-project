import pytest
from appium import webdriver

from conf.setup import EXECUTOR, ANDROID_BASE_CAPS, IMPLICITLY_WAIT
from conf.data import email, password, auditor_name
from pages.welcome_page import WelcomePage as WelcomeScreen
from pages.login_page import LoginPage as LoginScreen
from pages.dashboard_page import DashboardPage as DashboardScreen


@pytest.fixture
def browser():
    driver = webdriver.Remote(EXECUTOR, ANDROID_BASE_CAPS)
    driver.implicitly_wait(IMPLICITLY_WAIT)

    yield driver

    driver.quit()


def test_login_message_correctness(browser):
    login_activity = WelcomeScreen(browser)
    login_activity.click_login_button()

    login_activity = LoginScreen(browser)
    login_activity.set_email(email)
    login_activity.set_password(password)
    login_activity.click_login_button()

    dashboard_activity = DashboardScreen(browser)
    dashboard_activity.wait_for_loading_indicator()
    dashboard_activity.validate_welcome_message(auditor_name)

