from webdriver import browser
from conf.data import email, password, auditor_name
from pages.welcome_page import WelcomePage as WelcomeScreen
from pages.login_page import LoginPage as LoginScreen
from pages.on_boarding_page import OnBoardingPage as OnBoarding
from pages.dashboard_page import DashboardPage as DashboardScreen


def test_T53_login_with_correct_data(browser):
    login_activity = WelcomeScreen(browser)
    login_activity.click_login_button()

    # login_activity = LoginScreen(browser)
    # login_activity.set_email(email)
    # login_activity.set_password(password)
    # login_activity.click_login_button()
    #
    # on_boarding_activity = OnBoarding(browser)
    # on_boarding_activity.wait_for_loading_indicator()
    # on_boarding_activity.click_skip_link()
    #
    # dashboard_activity = DashboardScreen(browser)
    # dashboard_activity.wait_for_loading_indicator()
    # dashboard_activity.validate_welcome_message(auditor_name)

