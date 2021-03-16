import os

IMPLICITLY_WAIT = 10
LOADIN_INDICATOR_WAIT = 60

EXECUTOR = 'http://127.0.0.1:4723/wd/hub'

ANDROID_BASE_CAPS = {
    'platformName': 'Android',
    'platformVersion': os.getenv('ANDROID_PLATFORM_VERSION') or '9.0',
    'deviceName': os.getenv('ANDROID_DEVICE_VERSION') or 'GS8',
    # 'app': os.path.expanduser('./android/app/build/outputs/apk/app-debug.apk'),
    'udid': '3653354b4c303098',
    'appPackage': 'com.grainchain.forms',
    'appActivity': 'com.grainchain.forms.MainActivity',
}


IOS_BASE_CAPS = {
    'platformName': 'iOS',
    'platformVersion': os.getenv('IOS_PLATFORM_VERSION') or '12.2',
    'deviceName': os.getenv('IOS_DEVICE_NAME') or 'iPhone 8 Simulator',
    # 'app': os.path.abspath('../apps/TestApp.app.zip'),
    #'udid': '3653354b4c303098',
    # 'automationName': 'xcuitest',
    # 'showIOSLog': False,
}
