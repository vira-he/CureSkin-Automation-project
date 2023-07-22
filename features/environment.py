import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from support.logger import logger


def browser_init(context, test_name):
    """
    :param context: Behave context
    """
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # context.driver = webdriver.Firefox()
    # context.driver = webdriver.Safari()


    #### HEADLESS MODE ####

    # chrome_options = webdriver.ChromeOptions()
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--window-size=1920,1080")
    # context.driver = webdriver.Chrome(
    #     options=chrome_options,
    #     service=service
    # )

    #### BROWSERSTACK ####

    options = webdriver.FirefoxOptions()
    options.set_preference('profile', "/Users/test/Library/Application Support/Firefox/Profiles/<name_of_your_profile>")

    caps = {

        "os": "Windows",
        "osVersion": "11",
        "buildName": "firefoxprofile- python",
        "sessionName": "firefoxprofile- python",
        "browserName": "Firefox",
    }

    options.set_capability('bstack:options', caps)

    context.driver = webdriver.Remote(
        command_executor='http://virahetman_JQceH1:H886nJkaPzvgr9Nkneup@hub.browserstack.com/wd/hub',
        options=options)

    # LANA"S CODE
    # desired_cap = {
    #     'bstack:options': {
    #         "os": "Windows",
    #         "osVersion": "11",
    #         "browserVersion": "latest",
    #         "local": "false",
    #         "seleniumVersion": "3.5.2",
    #     },
    #     "browserName": "Edge",
    # }
    # bs_user = 'virahetman_JQceH1'
    # bs_key = 'H886nJkaPzvgr9Nkneup'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, options=options)

    context.driver.maximize_window()

    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 5)
    #
    context.app = Application(context.driver)

    # Allure command:
    # python3 -m behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/amazon_signin.feature


def before_scenario(context, scenario):
    # print(f'Started scenario: ', {scenario.name})
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)
    context.driver.execute_script('browserstack_executor:{"action":"setSessionName", "arguments":{"name": " ' + scenario.name + ' " }}')


def before_step(context, step):
    # print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        # print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')
        # Mark test case as FAILED on BrowserStack:
        # Documentation: https://www.browserstack.com/docs/automate/selenium/view-test-results/mark-tests-as-pass-fail
        # context.driver.execute_script(
        #     'browserstack_executor: {"action": "setSessionStatus", "arguments": '
        #     '{"status":"failed", "reason": "Step failed"}}'
        # )

        # Attach a screenshot to Allure report in case the step fails:
        # allure.attach(
        #     context.driver.get_screenshot_as_png(),
        #     name=f'{step.name}.png',
        #     attachment_type=AttachmentType.PNG
        # )


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
