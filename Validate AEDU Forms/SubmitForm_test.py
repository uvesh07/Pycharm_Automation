import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from datetime import datetime
import time
from datetime import date, timedelta
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import sys


# Global variables used for different methods POC-QA-Automation
ValidEmail = "addwebsolution@gmail.com"
ValidPass = "addweb@123"
Title = ""
Message = ""
SelSub = ""
SelClass = ""
Date = ""
SelFile = ""
Save = ""


@pytest.fixture(name="nvar")
def test_VariableTest(driver):
    global Title, Message, SelSub, SelClass, Date, SelFile, Save
    Title = driver.find_element(By.XPATH, '//*[@id="title"]')
    Message = driver.find_element(By.XPATH, '//*[@id="form1"]/div/div[2]/div/div[1]/div[2]/iframe')
    SelSub = driver.find_element(By.XPATH, '//*[@id="subject_id"]')
    SelClass = driver.find_element(By.XPATH, '//*[@id="class_id"]')
    Date = driver.find_element(By.XPATH, '//*[@id="publish_date"]')
    SelFile = driver.find_element(By.XPATH, '//*[@id="files"]')
    Save = driver.find_element(By.XPATH, '//*[@id="form1"]/div/div[3]/button')

    return Title, Message, SelSub, SelClass, Date, SelFile, Save


@pytest.mark.order(1)
def test_Login(driver):
    Email = driver.find_element(By.XPATH, '//*[@id="form-username"]')
    Password = driver.find_element(By.XPATH, '//*[@id="form-password"]')
    Login = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[2]/form[1]/button')
    global ValidEmail
    global ValidPass
    Email.clear()
    Password.clear()
    Email.send_keys(ValidEmail)
    Password.send_keys(ValidPass)
    Login.click()
    time.sleep(5)
    # Click on Homework Link
    Ul = driver.find_element(By.XPATH, '//*[@id="sibe-box"]/ul[2]')
    lis = Ul.find_elements(By.TAG_NAME, 'li')
    i = 0
    for li in lis:
        i = i + 1
        try:
            if li.find_element(By.TAG_NAME, 'a').text == "Homework":
                li.find_element(By.TAG_NAME, 'a').click()
        except StaleElementReferenceException:
            continue
    time.sleep(5)
    # Click on Add work
    print("Click on Add home work")
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div[1]/div/a').click()
    time.sleep(4)


@pytest.mark.order(2)
def test_AddBlankHomework(driver, nvar):
    ValidAddfile = "/home/addweb/PycharmProjects/Ticktalk leads automation/Images/bg color.jpeg"
    # time.sleep(4)
    Title, Message, SelSub, SelClass, Date, SelFile, Save = nvar
    driver.execute_script("arguments[0].scrollIntoView(true);", Save)
    Save.click()
    time.sleep(4)
    TitleMsg = driver.find_element(By.XPATH, '//*[@id="form1"]/div/div[2]/div/div[1]/div[1]/span/p')
    MessageMsg = driver.find_element(By.XPATH, '//*[@id="form1"]/div/div[2]/div/div[1]/div[2]/span/p')
    SelSubMsg = driver.find_element(By.XPATH, '//*[@id="form1"]/div/div[2]/div/div[1]/div[3]/div/span/p')
    SelClassMsg = driver.find_element(By.XPATH, '//*[@id="form1"]/div/div[2]/div/div[1]/div[4]/div/span/p')
    CheckMsg = driver.find_element(By.XPATH, '//*[@id="form1"]/div/div[2]/div/div[1]/div[5]/span/p')
    DateMsg = driver.find_element(By.XPATH, '//*[@id="form1"]/div/div[2]/div/div[2]/div/div[1]/span/p')
    if TitleMsg.is_enabled() and MessageMsg.is_enabled() and SelSubMsg.is_enabled() and SelClassMsg.is_enabled() and CheckMsg.is_enabled() and DateMsg.is_enabled():
        if TitleMsg.text == "The Title field is required.":
            print('"The Title field is required." Message displayed successfully.')
        if MessageMsg.text == "The Message field is required.":
            print('"The Message field is required." Message displayed successfully.')
        if SelSubMsg.text == "The Subject field is required.":
            print('"The Subject field is required.." Message displayed successfully.')
        if SelClassMsg.text == "The Class field is required.":
            print('"The Class field is required." Message displayed successfully.')
        if CheckMsg.text == "The Section field is required.":
            print('"The Section field is required." Message displayed successfully.')
        if DateMsg.text == "The Date field is required.":
            print('"The Date field is required." Message displayed successfully.')
    else:
        print("The blank field validations are not displayed")


@pytest.mark.order(3)
def test_AddHomework(driver, nvar):
    ValidAddfile = "/home/addweb/PycharmProjects/Ticktalk leads automation/Images/bg color.jpeg"
    # Click on Add work
    # driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div[1]/div/a').click()
    time.sleep(4)
    Title, Message, SelSub, SelClass, Date, SelFile, Save = nvar
    # Enter Title
    Title.send_keys("Test 1")
    # Enter Message
    Message.send_keys("Testing....")
    # Click on Select subject
    SelSub.click()
    # Select Option
    SelectSub = Select(SelSub)
    SelectSub.select_by_value("14")
    # Click on Select subject
    SelClass.click()
    # Select Option
    SelectClass = Select(SelClass)
    SelectClass.select_by_visible_text("VI")
    time.sleep(2)
    # Check the section
    Check = driver.find_element(By.XPATH, '//*[@id="section_id"]/label[2]/div/input')
    driver.execute_script("arguments[0].scrollIntoView(true);", Check)
    Check.click()
    # Enter Date
    # Get today's date
    Today = date.today()
    # Calculate tomorrow's date
    Tomorrow = Today + timedelta(days=1)
    # Format tomorrow's date as DD-MM-YYYY
    FormattedDate = Tomorrow.strftime("%d-%m-%Y")
    Date.send_keys(FormattedDate)
    # Select file
    SelFile.send_keys(ValidAddfile)
    # Submit the Form
    Save.click()
    time.sleep(4)
    SaveMsg = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div[2]/div[1]/div')
    if SaveMsg.is_enabled() and SaveMsg.text == "Homework added successfully!":
        print("The Form Saved Successfully..")
    Tbody = driver.find_element(By.XPATH, '//*[@id="DataTables_Table_0"]/tbody')
    Tr = Tbody.find_elements(By.TAG_NAME, 'tr')
    Size = len(Tr)
    for i in range(1, Size):
        TableTitle = driver.find_element(By.XPATH, f'//*[@id="DataTables_Table_0"]/tbody/tr[{i}]/td[1]/a')
        # Find the Saved Homework in the Table
        if TableTitle.text == "Test 1":
            print("The Saved Form found in the table")
            # Click on Edit Button
            Edit = driver.find_element(By.XPATH, f'//*[@id="DataTables_Table_0"]/tbody/tr[{i}]/td[4]/a[2]')
            driver.execute_script("arguments[0].scrollIntoView(true);", Edit)
            Edit.click()
            time.sleep(5)
            break


@pytest.mark.order(4)
def test_EditHomework(driver):
    Title = driver.find_element(By.XPATH, '//*[@id="title"]')
    Save = driver.find_element(By.XPATH, '//*[@id="form1"]/div/div[3]/div/button')
    # Edit Title
    Title.clear()
    Title.send_keys("Edited Title..")
    # Check the section
    Check = driver.find_element(By.XPATH, '//*[@id="section_id"]/div/input')
    driver.execute_script("arguments[0].scrollIntoView(true);", Check)
    Check.click()
    driver.execute_script("arguments[0].scrollIntoView(true);", Save)
    # Save the Form
    Save.click()
    time.sleep(3)
    EditMsg = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div[2]/div[1]/div')
    if EditMsg.is_enabled() and EditMsg.text == "Homework Updated successfully!":
        print("The Form Updated Successfully..")
