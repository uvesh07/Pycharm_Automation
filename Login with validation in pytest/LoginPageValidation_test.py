import time
import pytest
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


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
    wait = WebDriverWait(driver, 30)
    return Email, Password, Login, wait


@pytest.mark.order(1)
def test_LoginPage(driver, var):
    Email, Password, Login, wait = var
    assert driver.title == "AddWeb Solution"
    print("Successfully reached at Login page")
    # time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]')))


@pytest.mark.order(2)
def test_ValidateTextboxButton(driver, var):
    Email, Password, Login, wait = var

    assert Email.is_enabled()
    print("The Email textbox is Enabled.")
    assert Password.is_enabled()
    print("The Password textbox is Enabled.")
    assert Login.is_enabled()
    print("The Login button is Enabled.")


@pytest.mark.order(3)
def test_EnterBlankCreadential(driver, var):
    Email, Password, Login, wait = var
    global BlankEmail
    global BlankPass
    Email.send_keys(BlankEmail)
    Password.send_keys(BlankPass)
    Login.click()
    # time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-form"]/section/div/div/div/div/div[1]/div')))
    EmailMsg = driver.find_element(By.XPATH, '//*[@id="login-form"]/section/div/div/div/div/div[1]/div')
    PassMsg = driver.find_element(By.XPATH, '//*[@id="password-section"]/div[1]/div')
    if EmailMsg.text == "The Email field is required.":
        print('"The Email field is required." Message displayed successfully.')
    if PassMsg.text == "The password field is required.":
        print('"The password field is required." Message displayed successfully.')


@pytest.mark.order(4)
def test_EnterInValidEmail(driver, var):
    Email, Password, Login, wait = var
    global InvalidEmail
    global ValidPass
    Email.send_keys(InvalidEmail)
    Password.send_keys(ValidPass)
    Login.click()
    # time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-form"]/section/div/div/div/div/div[1]/div')))
    EmailMsg = driver.find_element(By.XPATH, '//*[@id="login-form"]/section/div/div/div/div/div[1]/div')
    if EmailMsg.text == "The email must be a valid email address.,The email format is invalid.":
        print('"The email must be a valid email address.,The email format is invalid." Message displayed successfully.')


@pytest.mark.order(5)
def test_EnterInvalidPass(driver, var):
    Email, Password, Login, wait = var
    global ValidEmail
    global InvalidPass
    Email.clear()
    Password.clear()
    Email.send_keys(ValidEmail)
    Password.send_keys(InvalidPass)
    Login.click()
    # time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-form"]/section/div/div/div/div/div[1]/div')))
    EmailMsg = driver.find_element(By.XPATH, '//*[@id="login-form"]/section/div/div/div/div/div[1]/div')
    if EmailMsg.text == "These credentials do not match our records.":
        print('"These credentials do not match our records." Message displayed successfully.')


@pytest.mark.order(6)
def test_EnterValidCreadential(driver, var):
    Email, Password, Login, wait = var
    global ValidEmail
    global ValidPass
    Email.clear()
    Password.clear()
    Email.send_keys(ValidEmail)
    Password.send_keys(ValidPass)
    Login.click()
    time.sleep(5)
    # wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sideMenuScroll"]/ul')))
    Ul = driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul')
    element = Ul.find_element(By.LINK_TEXT, "Private Dashboard")
    if element.is_enabled():
        print("The Private dashboard is displayed properly")

    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()
    time.sleep(3)