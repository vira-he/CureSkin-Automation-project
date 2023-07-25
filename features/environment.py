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


def browser_init(context, scenario):
    """
    :param context: Behave context
    """
    # service = Service(executable_path='/Users/vera/Desktop/QAA/CureSkin-Automation-project/chromedriver')
    # context.driver = webdriver.Chrome(service=service)

    # context.driver = webdriver.Firefox()
    # context.driver = webdriver.Safari()

    # HEADLESS MODE
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

    # BROWSERSTACK
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

    context.driver.execute_script('browserstack_executor:{"action":"setSessionName",\
     "arguments":{"name": " ' + scenario.name + ' " }}')

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 5)
    context.app = Application(context.driver)

    # Allure command:
    # python3 -m behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/cureskin_main.feature


def before_scenario(context, scenario):
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario)


def before_step(context, step):
    # print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
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
