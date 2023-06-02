import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from datetime import datetime
import time


# create a logger instance
logger = logging.getLogger(__name__)

# Global variables used for different methods POC-QA-Automation
valid_email = "uvesh@addwebsolution.in"
valid_pass = "addweb123"
current_day = "Nothing"
clockin_time = "Nothing"
expected_clockin_time = "Nothing"
user_name = "Nothing"


def test_enter_valid_credential(driver):
    email = driver.find_element(By.XPATH, '//*[@id="email"]')
    passwrd = driver.find_element(By.XPATH, '//*[@id="password"]')
    login = driver.find_element(By.XPATH, '//*[@id="submit-login"]')
    global valid_email
    global valid_pass

    email.send_keys(valid_email)
    passwrd.send_keys(valid_pass)
    login.click()
    time.sleep(5)


@pytest.mark.order(7)
def test_Click_on_Clockin(driver, selenium):
    try:
        # Clock-in Button
        clock_in = driver.find_element(By.XPATH, '//*[@id="clock-in"]')

        # Verify the clock-in button
        if clock_in.is_enabled():
            print("Successfully reached Dashboard, and Clock-in Button is Enabled")

        # Click on Clock-in button
        clock_in.click()
        time.sleep(5)

        # Save the clock-in button
        driver.find_element(By.XPATH, '//*[@id="save-clock-in"]').click()
        time.sleep(5)

    except NoSuchElementException:
        print("The User is already Clocked-in")


def test_Verify_Clockin_time_and_Get_username(driver, selenium):
    global clockin_time
    global expected_clockin_time
    global user_name
    global current_day

    # Get Current Date
    current_date = datetime.now()
    current_day = current_date.strftime("%d")
    current_day = current_day.lstrip("0")
    print("The Current Day is ", current_day)

    # Get Clock-in time
    clockin_at = driver.find_element(By.XPATH, '//*[@id="fullscreen"]/div[3]/div[1]/div[2]/p/span').text
    expected_clockin_time = clockin_at[14:22]
    clockin_time = clockin_at[14:19]
    print("The clockin time is", clockin_time)
    currentDateAndTime = datetime.now()

    currentTime = currentDateAndTime.strftime("%H:%M")
    print("The current time is", currentTime)

    if clockin_time == currentTime:
        print("The Clockin time is matching with Current time")

    # Get Username
    name = driver.find_element(By.XPATH, '//*[@id="fullscreen"]/div[3]/div[1]/div[1]/h4').text
    user_name = name[8:]
    print("The User name is ", user_name)
    time.sleep(5)


def test_Verify_clockin_and_attendance(driver, selenium):
    global clockin_time
    global expected_clockin_time
    global user_name

    ul = driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul')
    lis = ul.find_elements(By.TAG_NAME, 'li')
    i = 0

    for li in lis:
        i = i + 1
        try:
            if li.find_element(By.TAG_NAME, 'a').text == "HR":
                class_attribute = li.get_attribute('class')
                if 'closeIt' in class_attribute:
                    # Click on HR dropdown
                    li.find_element(By.TAG_NAME, 'a').click()
                    # Click on Attendance
                    driver.find_element(By.XPATH, f'//*[@id="sideMenuScroll"]/ul/li[{i}]/div/a[3]').click()

                else:
                    # Click on Attendance
                    driver.find_element(By.XPATH, f'//*[@id="sideMenuScroll"]/ul/li[{i}]/div/a[3]').click()

        except StaleElementReferenceException:
            continue

    time.sleep(3)

    # Click on Employee dropdown
    driver.find_element(By.XPATH, '//*[@id="filter-form"]/div/div[1]/div/div/button').click()

    employee_srch = driver.find_element(By.XPATH, '//*[@id="filter-form"]/div/div[1]/div/div/div/div[1]/input')

    # Search for valid option
    employee_srch.send_keys(user_name)
    emp_ul = driver.find_element(By.XPATH, '//*[@id="bs-select-1"]/ul')
    li_elements = emp_ul.find_elements(By.TAG_NAME, 'li')

    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in li_elements:
        try:
            if li.get_attribute('class') == 'active':
                active_a = li.find_element(By.TAG_NAME, 'a')
                break
        except StaleElementReferenceException:
            continue

    # Click on the active <li> element
    if active_a is not None:
        active_a.click()

    time.sleep(7)

    # Get the Employee name
    employee_name = driver.find_element(By.XPATH, '//*[@id="example"]/tbody/tr/td[1]/div/div/h5/a').text

    # Verify the Employee name
    if employee_name == user_name:
        print("The Employee's Name has been matched.")
        print(current_day)
    # Verify the day and click
    date_tr = driver.find_element(By.XPATH, '//*[@id="example"]/thead/tr')
    date_th = date_tr.find_elements(By.TAG_NAME, 'th')

    link_tr = driver.find_element(By.XPATH, '//*[@id="example"]/tbody/tr')
    link_td = link_tr.find_elements(By.TAG_NAME, 'td')

    for th, td in zip(date_th, link_td):
        if th.text == current_day:
            a = td.find_element(By.TAG_NAME, 'a')
            a.click()

    time.sleep(5)

    # Verify the clockin time
    actual_clockin_time = driver.find_element(By.XPATH,
                                              '//*[@id="myModalXl"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/p').text

    if actual_clockin_time == expected_clockin_time:
        print("The Actual Clockin time is matched with Expected Clockin Time")

    # Close the pop-up
    driver.find_element(By.XPATH, '//*[@id="myModalXl"]/div/div/div[1]/button').click()

    time.sleep(3)


def test_Clock_out(driver):

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
                        # Click on Private Dashboard
                        driver.find_element(By.XPATH, f'//*[@id="sideMenuScroll"]/ul/li[{i}]/div/a[2]').click()

                    except NoSuchElementException:
                        driver.find_element(By.XPATH, f'//*[@id="sideMenuScroll"]/ul/li[{i}]/div/a').click()

                else:
                    try:
                        # Click on Private Dashboard
                        driver.find_element(By.XPATH, f'/*[@id="sideMenuScroll"]/ul/li[{i}]/div/a[2]').click()

                    except NoSuchElementException:
                        driver.find_element(By.XPATH, f'//*[@id="sideMenuScroll"]/ul/li[{i}]/div/a').click()

        except StaleElementReferenceException:
            continue

    time.sleep(5)

    # Click on Clock out
    driver.find_element(By.XPATH, '//*[@id="clock-out"]').click()

    time.sleep(5)

    # Verify the Clock out
    clock_in = driver.find_element(By.XPATH, '//*[@id="clock-in"]')

    if clock_in.is_enabled():
        print("Clocked out successfully.")


    time.sleep(5)
