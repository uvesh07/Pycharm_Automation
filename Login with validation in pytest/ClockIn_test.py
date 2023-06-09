import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from datetime import datetime
import time
import sys


# Global variables used for different methods POC-QA-Automation
ValidEmail = "uvesh@addwebsolution.in"
ValidPass = "addweb123"
CurrentDay = "Nothing"
ClockinTime = "Nothing"
ExpectedClockinTime = "Nothing"
UserName = "Nothing"


@pytest.mark.order(7)
def test_ClickOnClockin(driver, selenium):
    try:
        # Clock-in Button
        ClockIn = driver.find_element(By.XPATH, '//*[@id="clock-in"]')
        # Verify the clock-in button
        if ClockIn.is_enabled():
            print("Successfully reached Dashboard, and Clock-in Button is Enabled")
        # Click on Clock-in button
        ClockIn.click()
        time.sleep(5)
        # Save the clock-in button
        driver.find_element(By.XPATH, '//*[@id="save-clock-in"]').click()
        time.sleep(5)
    except NoSuchElementException:
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
    time.sleep(5)


@pytest.mark.order(9)
def test_VerifyClockinAndAttendance(driver, selenium):
    global ClockinTime
    global ExpectedClockinTime
    global UserName
    Ul = driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul')
    lis = Ul.find_elements(By.TAG_NAME, 'li')
    i = 0
    for li in lis:
        i = i + 1
        try:
            if li.find_element(By.TAG_NAME, 'a').text == "HR":
                ClassAttribute = li.get_attribute('class')
                if 'closeIt' in ClassAttribute:
                    # Click on HR dropdown
                    li.find_element(By.TAG_NAME, 'a').click()
                    try:
                        # find <a> tag in work dropdown
                        a_links = li.find_elements(By.TAG_NAME, 'a')

                        for a in a_links:
                            if a.text == "Attendance":
                                a.click()
                    except NoSuchElementException:
                        print("You do not have access to Attendance Page.")
                else:
                    try:
                        # find <a> tag in work dropdown
                        a_links = li.find_elements(By.TAG_NAME, 'a')
                        for a in a_links:
                            if a.text == "Attendance":
                                a.click()
                    except NoSuchElementException:
                        print("You do not have access to Attendance Page.")
        except StaleElementReferenceException:
            continue
    time.sleep(3)
    # Click on Employee dropdown
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
    time.sleep(7)
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
    time.sleep(5)
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
    lis = Ul.find_elements(By.TAG_NAME, 'li')
    i = 0
    # Clcik on Private Dashboard
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
    time.sleep(5)
    # Click on Clock out
    driver.find_element(By.XPATH, '//*[@id="clock-out"]').click()
    time.sleep(5)
    # Verify the Clock out
    ClockIn = driver.find_element(By.XPATH, '//*[@id="clock-in"]')
    if ClockIn.is_enabled():
        print("Clocked out successfully.")
    time.sleep(5)
