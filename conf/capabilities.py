import os

# App folder should be on home directory
APP_FOLDER = 'apps/'
APP_NAME = '1.1.0-dev(2)'

IMPLICITLY_WAIT = 10
LOADING_INDICATOR_WAIT = 10

EXECUTOR = 'http://127.0.0.1:4723/wd/hub'

ANDROID_BASE_CAPS = {
    'platformName': 'Android',
    'platformVersion': os.getenv('ANDROID_PLATFORM_VERSION') or '9.0',
    'deviceName': os.getenv('ANDROID_DEVICE_VERSION') or 'GS8',
    'app': os.path.expanduser('~/' + APP_FOLDER + APP_NAME + '.apk'),
    'udid': '3653354b4c303098',
    'appPackage': 'com.grainchain.forms.development',
    'appActivity': 'com.grainchain.forms.MainActivity',
    'autoGrantPermissions': True
}

IOS_BASE_CAPS = {
    'platformName': 'iOS',
    'platformVersion': os.getenv('IOS_PLATFORM_VERSION') or '12.2',
    'deviceName': os.getenv('IOS_DEVICE_NAME') or 'iPhone 8 Simulator',
    # 'app': os.path.expanduser('~/' + APP_FOLDER + APP_NAME + '.ipa'),
    # 'udid': 'a250528f152ab3d07dcf5cc9091bf5dc70bba618',
    # 'automationName': 'xcuitest',
    # 'autoAcceptAlerts': True
}
