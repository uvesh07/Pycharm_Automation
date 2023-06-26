from behave import given, then
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from behave import fixture, use_fixture
from rocketchat_API.rocketchat import RocketChat

@given('I launch the browser')
def step_launch_browser(context):
    # The driver fixture will be set up and available in the context.driver variable
    # create a Service object for the ChromeDriver
    service = Service('/home/addweb/PycharmProjects/FirstScript/Drivers/chromedriver.exe')
    # create a webdriver object and pass the Service object
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1280,1024")
    chrome_options.add_argument(f"user-data-dir={context.config.base_directory}/chrome-profile")
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    # Login to the site
    context.driver.get('https://ttstage.addwebprojects.com/login')
    context.driver.maximize_window()
    print("Launch browser")
    yield context.driver
    # Teardown - close the driver after the test completes
    context.driver.quit()



@then('the browser is launched successfully')
def step_browser_launched_successfully(context):
    # Add assertion or validation logic here
    assert context.driver is not None, "Browser is not launched successfully"
