import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from datetime import datetime
import time
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


# Global variables used for different methods POC-QA-Automation
ValidEmail = "uvesh@addwebsolution.in"
ValidPass = "addweb123"
CurrentDay = "Nothing"
ClockinTime = "Nothing"
ExpectedClockinTime = "Nothing"
UserName = "Nothing"
wait = ""


@pytest.mark.order(7)
def test_ClickOnClockin(driver, selenium):
    global wait
    wait = WebDriverWait(driver, 30)
    try:
        # Clock-in Button
        ClockIn = driver.find_element(By.XPATH, '//*[@id="clock-in"]')
        # Verify the clock-in button
        if ClockIn.is_enabled():
            print("Successfully reached Dashboard, and Clock-in Button is Enabled")
        # Click on Clock-in button
        ClockIn.click()
        # time.sleep(5)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="save-clock-in"]')))
        # Save the clock-in button
        driver.find_element(By.XPATH, '//*[@id="save-clock-in"]').click()
        # time.sleep(5)
    except NoSuchElementException:
        driver.save_screenshot(os.path.join(os.getcwd(), "Screenshots", "Dashboard.png"))
        over = driver.find_element(By.XPATH, '//*[@id="mob-client-detail"]/a[2]/span')
        if over.is_enabled():
            print("The User is on Admin Dashboard")
        print("The User is already Clocked-in")


@pytest.mark.order(8)
def test_VerifyClockinTimeAndGetUsername(driver, selenium):
    global ClockinTime
    global ExpectedClockinTime
    global UserName
    global CurrentDay

    # Get Current Date
    CurrentDate = datetime.now()
    CurrentDay = CurrentDate.strftime("%d")
    CurrentDay = CurrentDay.lstrip("0")
    print("The Current Day is ", CurrentDay)

    # Get Clock-in time
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="fullscreen"]/div[3]/div[1]/div[2]/p/span')))
    Clockin_At = driver.find_element(By.XPATH, '//*[@id="fullscreen"]/div[3]/div[1]/div[2]/p/span').text
    ExpectedClockinTime = Clockin_At[14:22]
    print("expected time at verify clockin : " + ExpectedClockinTime)
    ClockinTime = Clockin_At[14:19]
    print("clockin time at verify clockin : " + ClockinTime)
    print("The clockin time is", ClockinTime)
    CurrentDateAndTime = datetime.now()
    CurrentTime = CurrentDateAndTime.strftime("%H:%M")
    print("The current time is", CurrentTime)
    if ClockinTime == CurrentTime:
        print("The Clockin time is matching with Current time")
    # Get Username
    name = driver.find_element(By.XPATH, '//*[@id="fullscreen"]/div[3]/div[1]/div[1]/h4').text
    UserName = name[8:]
    print("The User name is ", UserName)
    time.sleep(3)


@pytest.mark.order(9)
def test_VerifyClockinAndAttendance(driver, selenium):
    global ClockinTime
    global ExpectedClockinTime
    global UserName
    Ul = driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul')
    element = Ul.find_element(By.LINK_TEXT, "HR")
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()
    element = Ul.find_element(By.LINK_TEXT, "Attendance")
    actions.move_to_element(element).click().perform()
    # time.sleep(3)
    # Click on Employee dropdown
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="filter-form"]/div/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="filter-form"]/div/div[1]/div/div/button').click()
    EmployeeSrch = driver.find_element(By.XPATH, '//*[@id="filter-form"]/div/div[1]/div/div/div/div[1]/input')
    # Search for valid option
    EmployeeSrch.send_keys(UserName)
    EmpUl = driver.find_element(By.XPATH, '//*[@id="bs-select-1"]/ul')
    LiElements = EmpUl.find_elements(By.TAG_NAME, 'li')
    # Iterate through the <li> elements and find the first one that has the "active" class
    Active_a = None
    for li in LiElements:
        try:
            if li.get_attribute('class') == 'active':
                Active_a = li.find_element(By.TAG_NAME, 'a')
                break
        except StaleElementReferenceException:
            continue
    # Click on the active <li> element
    if Active_a is not None:
        Active_a.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="example"]/tbody/tr')))
    time.sleep(10)
    # Get the Employee name
    EmployeeName = driver.find_element(By.XPATH, '//*[@id="example"]/tbody/tr/td[1]/div/div/h5/a').text
    # Verify the Employee name
    if EmployeeName == UserName:
        print("The Employee's Name has been matched.")
    # Verify the day and click
    DateTr = driver.find_element(By.XPATH, '//*[@id="example"]/thead/tr')
    DateTh = DateTr.find_elements(By.TAG_NAME, 'th')
    LinkTr = driver.find_element(By.XPATH, '//*[@id="example"]/tbody/tr')
    LinkTd = LinkTr.find_elements(By.TAG_NAME, 'td')
    for th, td in zip(DateTh, LinkTd):
        if th.text == CurrentDay:
            a = td.find_element(By.TAG_NAME, 'a')
            a.click()
    # time.sleep(5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="myModalXl"]/div/div/div[2]/div[2]/div[2]/div/div[2]/div')))
    ClockinUl = driver.find_element(By.XPATH, '//*[@id="myModalXl"]/div/div/div[2]/div[2]/div[2]/div/div[2]/div')
    ClockinLis = ClockinUl.find_elements(By.TAG_NAME, 'li')
    size = sys.getsizeof(ClockinLis)
    flag = 0
    for i in range(1, size):
        try:
            Untrimmed = driver.find_element(By.XPATH, f'/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[{i}]/ul/li[1]/p[2]').text
            ActualClockinTime = Untrimmed[0:8]
            if ActualClockinTime == ExpectedClockinTime:
                print("The actual clockin : " + ActualClockinTime + " matched with expected clockin time : " + ExpectedClockinTime + "")
                flag = 1
        except NoSuchElementException:
            continue
    if flag == 0:
        print("The actual clockin time does not match with expected clockin time.")
    driver.find_element(By.XPATH, '//*[@id="myModalXl"]/div/div/div[1]/button').click()
    time.sleep(3)


@pytest.mark.order(10)
def test_ClockOut(driver):
    Ul = driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul')
    element = Ul.find_element(By.LINK_TEXT, "Dashboard")
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()
    element = Ul.find_element(By.LINK_TEXT, "Private Dashboard")
    actions.move_to_element(element).click().perform()
    # time.sleep(5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="clock-out"]')))
    # Click on Clock out
    driver.find_element(By.XPATH, '//*[@id="clock-out"]').click()
    # time.sleep(5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="clock-in"]')))
    # Verify the Clock out
    ClockIn = driver.find_element(By.XPATH, '//*[@id="clock-in"]')
    if ClockIn.is_enabled():
        print("Clocked out successfully.")
    time.sleep(5)
