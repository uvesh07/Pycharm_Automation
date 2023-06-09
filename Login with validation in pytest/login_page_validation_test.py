import pytest
import logging
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
import time

# create a logger instance
logger = logging.getLogger(__name__)

# Global variables used for different methods
valid_email = "uvesh@addwebsolution.in"
invalid_email = "uveshaddwebsolution.in"
blank_email = ""
valid_pass = "addweb123"
invalid_pass = "addweb1234"
blank_pass = ""


@pytest.fixture(name="var")
def test_Var(driver):
    email = driver.find_element(By.XPATH, '//*[@id="email"]')
    passwrd = driver.find_element(By.XPATH, '//*[@id="password"]')
    login = driver.find_element(By.XPATH, '//*[@id="submit-login"]')
    return email, passwrd, login


@pytest.mark.order(1)
def test_Login_Page(driver, selenium):
    assert driver.title == "AddWeb Solution"
    print("Successfully reached at Login page")
    logger.info("Successfully reached at Login page")
    time.sleep(3)


@pytest.mark.order(2)
def test_Validate_Textbox_Button(driver, var):
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
def test_Enter_blank_Creadential(driver, var):
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
def test_Enter_invalid_Email(driver, var):
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
def test_Enter_invalid_Pass(driver, var):
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
def test_Enter_valid_Creadential(driver, var):
    email, passwrd, login = var
    global valid_email
    global valid_pass
    email.clear()
    passwrd.clear()
    email.send_keys(valid_email)
    passwrd.send_keys(valid_pass)
    login.click()

    time.sleep(5)

    # if driver.title == "Dashboard":
    #     print("Successfully Logged in.")
    #     logger.info("Successfully Logged in.")
    #
    # else:
    ul = driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul')
    lis = ul.find_elements(By.TAG_NAME, 'li')
    i = 0

    for li in lis:
        i = i + 1
        try:
            if li.find_element(By.TAG_NAME, 'a').text == "Dashboard":
                class_attribute = li.get_attribute('class')
                if 'closeIt' in class_attribute:
                    # Click on Dashboard dropdown
                    li.find_element(By.TAG_NAME, 'a').click()

                    try:
                        # find <a> tag in work dropdown
                        a_links = li.find_elements(By.TAG_NAME, 'a')

                        for a in a_links:
                            if a.text == "Private Dashboard":
                                a.click()

                    except NoSuchElementException:
                        print("You do not have access to Private Dashboard Page.")

                else:
                    try:
                        # find <a> tag in work dropdown
                        a_links = li.find_elements(By.TAG_NAME, 'a')

                        for a in a_links:
                            if a.text == "Private Dashboard":
                                a.click()

                    except NoSuchElementException:
                        print("You do not have access to Private Dashboard Page.")

        except StaleElementReferenceException:
            continue

    time.sleep(3)
