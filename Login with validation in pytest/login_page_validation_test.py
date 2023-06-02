import pytest
import logging
from selenium.webdriver.common.by import By
import time

# create a logger instance
logger = logging.getLogger(__name__)

# Global variables used for different methods
valid_email = "saurabhdhariwal.com@gmail.com"
invalid_email = "saurabhdhariwal.comgmail.com"
blank_email = ""
valid_pass = "addweb123"
invalid_pass = "addweb1234"
blank_pass = ""


@pytest.fixture(name="var")
def Test_Var(driver):
    email = driver.find_element(By.XPATH, '//*[@id="email"]')
    passwrd = driver.find_element(By.XPATH, '//*[@id="password"]')
    login = driver.find_element(By.XPATH, '//*[@id="submit-login"]')
    return email, passwrd, login


@pytest.mark.order(1)
def Test_Login_Page(driver, selenium):
    assert driver.title == "AddWeb Solution"
    print("Successfully reached at Login page")
    logger.info("Successfully reached at Login page")
    time.sleep(3)


@pytest.mark.order(2)
def Test_Validate_Textbox_Button(driver, var):
    email, passwrd, login = var

    assert email.is_enabled()
    print("The Email textbox is Enabled.")
    logger.info("The Email textbox is Enabled.")

    assert passwrd.is_enabled()
    print("The Password textbox is Enabled.")
    logger.info("The Password textbox is Enabled.")

    assert login.is_enabled()
    print("The Login button is Enabled.")
    logger.info("The Login button is Enabled.")


@pytest.mark.order(3)
def Test_Enter_blank_Creadential(driver, var):
    email, passwrd, login = var
    global blank_email
    global blank_pass
    email.send_keys(blank_email)
    passwrd.send_keys(blank_pass)
    login.click()

    time.sleep(3)

    email_msg = driver.find_element(By.XPATH, '//*[@id="login-form"]/section/div/div/div/div/div[1]/div')
    pass_msg = driver.find_element(By.XPATH, '//*[@id="password-section"]/div[1]/div')

    if email_msg.text == "The email field is required.":
        print('"The email field is required." Message displayed successfully.')
        logger.info('"The email field is required." Message displayed successfully.')

    if pass_msg.text == "The password field is required.":
        print('"The password field is required." Message displayed successfully.')
        logger.info('"The password field is required." Message displayed successfully.')


@pytest.mark.order(4)
def Test_Enter_invalid_Email(driver, var):
    email, passwrd, login = var
    global invalid_email
    global valid_pass
    email.send_keys(invalid_email)
    passwrd.send_keys(valid_pass)
    login.click()

    time.sleep(3)

    email_msg = driver.find_element(By.XPATH, '//*[@id="login-form"]/section/div/div/div/div/div[1]/div')

    if email_msg.text == "The email must be a valid email address.,The email format is invalid.":
        print('"The email must be a valid email address.,The email format is invalid." Message displayed successfully.')
        logger.info('"The email must be a valid email address.,The email format is invalid." Message displayed successfully.')


@pytest.mark.order(5)
def Test_Enter_invalid_Pass(driver, var):
    email, passwrd, login = var
    global valid_email
    global invalid_pass
    email.clear()
    passwrd.clear()
    email.send_keys(valid_email)
    passwrd.send_keys(invalid_pass)
    login.click()

    time.sleep(3)

    email_msg = driver.find_element(By.XPATH, '//*[@id="login-form"]/section/div/div/div/div/div[1]/div')

    if email_msg.text == "These credentials do not match our records.":
        print('"These credentials do not match our records." Message displayed successfully.')
        logger.info('"These credentials do not match our records." Message displayed successfully.')


@pytest.mark.order(6)
def Test_Enter_valid_Creadential(driver, var):
    email, passwrd, login = var
    global valid_email
    global valid_pass
    email.clear()
    passwrd.clear()
    email.send_keys(valid_email)
    passwrd.send_keys(valid_pass)
    login.click()

    time.sleep(3)

    if(driver.title == "Dashboard"):
        print("Successfully Logged in.")
        logger.info("Successfully Logged in.")

    time.sleep(3)
