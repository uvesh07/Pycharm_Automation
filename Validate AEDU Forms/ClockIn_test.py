import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from datetime import datetime
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import sys


# Global variables used for different methods POC-QA-Automation
ValidEmail = "addwebsolution@gmail.com"
ValidPass = "addweb@123"


@pytest.fixture(name="nvar")
def test_Variable_test(driver):
    Email = driver.find_element(By.XPATH, '//*[@id="form-username"]')
    Password = driver.find_element(By.XPATH, '//*[@id="form-password"]')
    Login = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[2]/form[1]/button')
    return Email, Password, Login


@pytest.mark.order(7)
def test_Login(driver, nvar):
    Email, Password, Login = nvar
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


@pytest.mark.order(7)
def test_AddHomework(driver):
    valid_addfile = "/home/addweb/PycharmProjects/Ticktalk leads automation/Images/bg color.jpeg"

    # Click on Add work
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div[1]/div/a').click()
    time.sleep(4)
    # Enter Title
    driver.find_element(By.XPATH, '//*[@id="title"]').send_keys("Test 1")
    time.sleep(4)
    # Enter Message
    driver.find_element(By.XPATH, '/html/body').send_keys("Testing....")
    time.sleep(4)
    # Select Subject
    sel = driver.find_element(By.XPATH, '//*[@id="subject_id"]')
    time.sleep(4)
    # Click on Select subject
    sel.click()
    time.sleep(4)
    # Select Option
    sel.select_by_visible_text("ENGLISH (Theory) ")
    time.sleep(4)
    # Select Class
    sel = driver.find_element(By.XPATH, '//*[@id="class_id"]')
    time.sleep(4)
    # Click on Select subject
    sel.click()
    time.sleep(4)
    # Select Option
    sel.select_by_visible_text("VI")
    time.sleep(4)
    # Enter Date
    driver.find_element(By.XPATH, '//*[@id="publish_date"]').send_keys("12-06-2023")
    time.sleep(4)
    # Select file
    driver.find_element(By.XPATH, '//*[@id="files"]').send_keys(valid_addfile)
    time.sleep(4)
    # Submit the Form
    driver.find_element(By.XPATH, '//*[@id="form1"]/div/div[3]/button').click()
    time.sleep(5)