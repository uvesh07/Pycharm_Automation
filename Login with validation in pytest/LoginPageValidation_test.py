import time
import pytest
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By

# Global variables used for different methods
ValidEmail = "uvesh@addwebsolution.in"
InvalidEmail = "uveshaddwebsolution.in"
BlankEmail = ""
ValidPass = "addweb123"
InvalidPass = "addweb1234"
BlankPass = ""


@pytest.fixture(name="var")
def test_Variable_test(driver):
    Email = driver.find_element(By.XPATH, '//*[@id="email"]')
    Password = driver.find_element(By.XPATH, '//*[@id="password"]')
    Login = driver.find_element(By.XPATH, '//*[@id="submit-login"]')
    return Email, Password, Login


@pytest.mark.order(1)
def test_LoginPage(driver, selenium):
    assert driver.title == "AddWeb Solution"
    print("Successfully reached at Login page")
    time.sleep(3)


@pytest.mark.order(2)
def test_ValidateTextboxButton(driver, var):
    Email, Password, Login = var

    assert Email.is_enabled()
    print("The Email textbox is Enabled.")
    assert Password.is_enabled()
    print("The Password textbox is Enabled.")
    assert Login.is_enabled()
    print("The Login button is Enabled.")


@pytest.mark.order(3)
def test_EnterBlankCreadential(driver, var):
    Email, Password, Login = var
    global BlankEmail
    global BlankPass
    Email.send_keys(BlankEmail)
    Password.send_keys(BlankPass)
    Login.click()
    time.sleep(3)
    EmailMsg = driver.find_element(By.XPATH, '//*[@id="login-form"]/section/div/div/div/div/div[1]/div')
    PassMsg = driver.find_element(By.XPATH, '//*[@id="password-section"]/div[1]/div')
    if EmailMsg.text == "The Email field is required.":
        print('"The Email field is required." Message displayed successfully.')
    if PassMsg.text == "The password field is required.":
        print('"The password field is required." Message displayed successfully.')


@pytest.mark.order(4)
def test_EnterInValidEmail(driver, var):
    Email, Password, Login = var
    global InvalidEmail
    global ValidPass
    Email.send_keys(InvalidEmail)
    Password.send_keys(ValidPass)
    Login.click()
    time.sleep(3)
    EmailMsg = driver.find_element(By.XPATH, '//*[@id="login-form"]/section/div/div/div/div/div[1]/div')
    if EmailMsg.text == "The Email must be a valid Email address.,The Email format is invalid.":
        print('"The Email must be a valid Email address.,The Email format is invalid." Message displayed successfully.')


@pytest.mark.order(5)
def test_EnterInvalidPass(driver, var):
    Email, Password, Login = var
    global ValidEmail
    global InvalidPass
    Email.clear()
    Password.clear()
    Email.send_keys(ValidEmail)
    Password.send_keys(InvalidPass)
    Login.click()
    time.sleep(3)
    EmailMsg = driver.find_element(By.XPATH, '//*[@id="login-form"]/section/div/div/div/div/div[1]/div')
    if EmailMsg.text == "These credentials do not match our records.":
        print('"These credentials do not match our records." Message displayed successfully.')


@pytest.mark.order(6)
def test_EnterValidCreadential(driver, var):
    Email, Password, Login = var
    global ValidEmail
    global ValidPass
    Email.clear()
    Password.clear()
    Email.send_keys(ValidEmail)
    Password.send_keys(ValidPass)
    Login.click()
    time.sleep(5)

    Ul = driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul')
    lis = Ul.find_elements(By.TAG_NAME, 'li')
    i = 0
    for li in lis:
        i = i + 1
        try:
            if li.find_element(By.TAG_NAME, 'a').text == "Dashboard":
                ClassAttribute = li.get_attribute('class')
                if 'closeIt' in ClassAttribute:
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
