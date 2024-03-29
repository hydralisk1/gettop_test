from selenium import webdriver
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    # Web drivers by browser
    # context.driver = webdriver.Chrome()
    # context.driver = webdriver.Firefox()

    # Headless Chrome Browser
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--window-size=1920,1080')
    context.driver = webdriver.Chrome(chrome_options=options)

    # Browser Stack
    # bs_user = "joonilkim1"
    # bs_pw = "c6e85fe6YAg6QxTpP6o1"
    #
    # desired_cap = {
    #     'browser': 'Chrome',
    #     'browser_version': '89.0',
    #     'os': 'Windows',
    #     'os_version': '10',
    #     'name': 'Bstack-[Python] Sample Test'
    # }
    # url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    # 10 sec changed to 3 sec since 10 sec is too long time
    # context.driver.wait = WebDriverWait(context.driver, 5)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
