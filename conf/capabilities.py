import os

IMPLICITLY_WAIT = 10
LOADING_INDICATOR_WAIT = 10

EXECUTOR = 'http://127.0.0.1:4723/wd/hub'

APP_NAME = '1.1.0-dev(2)'

ANDROID_BASE_CAPS = {
    'platformName': 'Android',
    'platformVersion': os.getenv('ANDROID_PLATFORM_VERSION') or '9.0',
    'deviceName': os.getenv('ANDROID_DEVICE_VERSION') or 'GS8',
    'app': os.path.expanduser('~/apps/' + APP_NAME + '.apk'),
    'udid': '3653354b4c303098',
    'appPackage': 'com.grainchain.forms.development',
    'appActivity': 'com.grainchain.forms.MainActivity',
    'autoGrantPermissions': True
}

IOS_BASE_CAPS = {
    'platformName': 'iOS',
    'platformVersion': os.getenv('IOS_PLATFORM_VERSION') or '12.2',
    'deviceName': os.getenv('IOS_DEVICE_NAME') or 'iPhone 8 Simulator',
    # 'app': os.path.abspath('../apps/' + APP_NAME + '.ipa'),
    # 'udid': '3653354b4c303098',
    # 'automationName': 'xcuitest',
    # 'showIOSLog': False,
}
