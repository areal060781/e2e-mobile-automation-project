from appium.webdriver.common.mobileby import MobileBy


class BasePageLocators(object):
    LOADING_INDICATOR = (MobileBy.ACCESSIBILITY_ID, 'loadingIndicator.image')


class WelcomePageLocators(object):
    LOG_IN_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'signIn.button')
    NEW_ACCOUNT_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'signUp.button')
    CUSTOMER_SUPPORT_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'customerSupport.button')


class LoginPageLocators(object):
    EMAIL_INPUT = (MobileBy.ACCESSIBILITY_ID, 'email.input')
    PASSWORD_INPUT = (MobileBy.ACCESSIBILITY_ID, 'password.input')
    #PASSWORD_RECOVERY_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'passwordRecoveryButton')
    LOG_IN_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'signIn.button')
    #CUSTOMER_SUPPORT_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'customerSupport.button')


class DashboardPageLocators(object):
    AUDITOR_NAME_TEXT = (MobileBy.ACCESSIBILITY_ID, 'auditorName.label')


class OnBoardingLocators(object):
    UNDERSTOOD_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'confirm.button')
    SKIP_LINK = (MobileBy.ACCESSIBILITY_ID, 'skip.button')
