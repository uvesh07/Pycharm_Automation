import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from rocketchat_API.rocketchat import RocketChat

# Global variables to store test results
Message = "This is for testing purpose."
TotalTests = 0
NumPassed = 0
NumFailed = 0
NumErrors = 0
NumSkipped = 0


# In conftest.py
def pytest_collection_modifyitems(config, items):
    # Sort the test items based on the marker order
    items.sort(key=lambda x: int(x.get_closest_marker("order").args[0]))


@pytest.fixture(scope="session", autouse=True, name="driver")
def setup():
    # create a Service object for the ChromeDriver
    service = Service('/home/addweb/PycharmProjects/FirstScript/Drivers/chromedriver.exe')
    # create a webdriver object and pass the Service object
    global driver
    driver = webdriver.Chrome(service=service)
    # Login to the site
    driver.get('https://demo.aedu.co.in/site/login')
    driver.maximize_window()
    print("Launch browser")
    return driver


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
