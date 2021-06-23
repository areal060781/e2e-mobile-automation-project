import pytest
from appium import webdriver

from conf.capabilities import EXECUTOR, ANDROID_BASE_CAPS, IMPLICITLY_WAIT


@pytest.fixture
def browser():
    driver = webdriver.Remote(EXECUTOR, ANDROID_BASE_CAPS)
    driver.implicitly_wait(IMPLICITLY_WAIT)

    yield driver

    driver.quit()

