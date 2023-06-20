import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from rocketchat_API.rocketchat import RocketChat
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import datetime

# Global variables to store test results
Message = "This is for testing purpose."
TotalTests = 0
NumPassed = 0
NumFailed = 0
NumErrors = 0
NumSkipped = 0


# In conftest.py
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", nargs="+", default="chrome", help="Specify the browser(s) for testing")


def pytest_collection_modifyitems(config, items):
    # Sort the test items based on the marker order
    items.sort(key=lambda x: int(x.get_closest_marker("order").args[0]))


@pytest.fixture(scope="session", autouse=True, name="driver")
def setup(request):
    browser_types = request.config.getoption("--browser")
    for browser_type in browser_types:
        if browser_type == "chrome":
            # Create a Service object for the ChromeDriver
            service = ChromeService('/home/addweb/PycharmProjects/FirstScript/Drivers/chromedriver.exe')
            # Create ChromeOptions and DesiredCapabilities objects
            chrome_options = ChromeOptions()
            chrome_capabilities = DesiredCapabilities.CHROME.copy()
            chrome_capabilities["acceptInsecureCerts"] = True
            # Create a webdriver object and pass the Service, Options, and Capabilities objects, desired_capabilities=chrome_capabilities
            driver = webdriver.Chrome(service=service, options=chrome_options)
            # Execute the tests for Chrome browser
            run_tests(driver)
        elif browser_type == "firefox":
            # Create a Service object for the geckodriver
            service = FirefoxService('Drivers/geckodriver.exe')
            # Create FirefoxOptions and DesiredCapabilities objects
            firefox_options = FirefoxOptions()
            firefox_capabilities = DesiredCapabilities.FIREFOX.copy()
            firefox_capabilities["acceptInsecureCerts"] = True
            # Create a webdriver object and pass the Service, Options, and Capabilities objects, capabilities=firefox_capabilities
            driver = webdriver.Firefox(service=service, options=firefox_options)
            # Execute the tests for Firefox browser
            run_tests(driver)
        else:
            raise ValueError(f"Invalid browser type: {browser_type}")


def run_tests(driver):
    # Login to the site
    driver.get('https://ttstage.addwebprojects.com/login')
    driver.maximize_window()
    print("Launch browser")
    return dri
    # Execute the tests

    # Teardown: Quit the webdriver instance after the tests
    # driver.quit()

    # # Login to the site
    # driver.get('https://ttstage.addwebprojects.com/login')
    # driver.maximize_window()
    # print("Launch browser")
    #
    # return driver

    # yield driver
    # driver.quit()

    # # create a Service object for the ChromeDriver
    # service = Service('/home/addweb/PycharmProjects/FirstScript/Drivers/chromedriver.exe')
    # # create a webdriver object and pass the Service object
    # global driver
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--window-size=1280,1024")
    # driver = webdriver.Chrome(service=service)
    # # Login to the site
    # driver.get('https://ttstage.addwebprojects.com/login')
    # driver.maximize_window()
    # print("Launch browser")
    # return driver


def pytest_configure(config):
    current_time = datetime.now().strftime("%Y%m%d-%H%M%S")
    config.option.htmlpath = f"test_report_{current_time}.html"


def pytest_runtest_makereport(item, call):
    global TotalTests, NumPassed, NumFailed, NumErrors, NumSkipped
    if call.when == "call":  # Called after each test execution
        # Increment the total test count
        TotalTests += 1
        # Check the outcome of the test
        if call.excinfo is None:
            # Test passed
            NumPassed += 1
        elif call.excinfo.errisinstance(pytest.fail.Exception):
            # Test failed
            NumFailed += 1
        elif call.excinfo.errisinstance(Exception):
            # Test resulted in an error
            NumErrors += 1
        elif call.excinfo.errisinstance(pytest.skip.Exception):
            # Test was skipped
            NumSkipped += 1


def Send_To_Channel(Message):
    # Set the channel or user to whom you want to send the zip file
    TeamRoom = 'team-circuit-breakers'
    rocket = RocketChat('uvesh@addwebsolution.in', 'Uvesh@890', server_url='https://chat.addwebsolution.in/')
    # rocket.chat_post_message(room_id=TeamRoom, text=Message)


def pytest_terminal_summary(terminalreporter):
    global TotalTests, NumPassed, NumFailed, NumErrors, NumSkipped
    global Message
    Message = "Test summary \n"
    Message += f"Total Tests: {TotalTests} \n"
    Message += f"Passed: {NumPassed} \n"
    Message += f"Failed: {NumFailed} \n"
    Message += f"Errors: {NumErrors} \n"
    Message += f"Skipped: {NumSkipped} \n"
    Send_To_Channel(Message)


def pytest_html_report_title(report):
    report.title = "Automation Report"
