from appium.webdriver.common.mobileby import MobileBy


class WelcomePageLocators(object):
    LOG_IN_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'signInButton')
    NEW_ACCOUNT_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'newAccountButton')
    CUSTOMER_SUPPORT_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'customerSupportButton')


class LoginPageLocators(object):
    EMAIL_INPUT = (MobileBy.ACCESSIBILITY_ID, 'emailInput')
    PASSWORD_INPUT = (MobileBy.ACCESSIBILITY_ID, 'passwordInput')
    LOG_IN_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'signInButton')
    PASSWORD_RECOVERY_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'passwordRecoveryButton')


class DashboardPageLocators(object):
    AUDITOR_NAME_TEXT = (MobileBy.ACCESSIBILITY_ID, 'auditorNameText')
    LOADING_INDICATOR = (MobileBy.ACCESSIBILITY_ID, 'loadingIndicator')
