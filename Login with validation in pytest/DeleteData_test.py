import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time

# create a logger instance
logger = logging.getLogger(__name__)

# Global variables used for different methods POC-QA-Automation
ValidEmail = "saurabhdhariwal.com@gmail.com"
ValidPass = "addweb123"

ValidProject = "Project Testing"
InvalidProject = "Nothing"

ValidTask = "Task Testing"
InvalidTask = "Nothing"

ValidEmployee = "Pathan UveshMohammad"
InvalidEmployee = "Nothing"

ValidDate = "17-05-2023"
InvalidDate = "32-05-2023"

ValidHour = "3"
InvalidHour = "12"

ValidMin = "30"
InvalidMin = "60"

ValidMemo = "Testing......"
InvalidMemo = "Testing......"


@pytest.mark.order(38)
def test_ClickOnTimelogPage(driver, selenium):
    Ul = driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul')
    lis = Ul.find_elements(By.TAG_NAME, 'li')
    i = 0
    # Click on Work dropdown
    for li in lis:
        i = i + 1
        try:
            if li.find_element(By.TAG_NAME, 'a').text == "Work":
                ClassAttribute = li.get_attribute('class')
                if 'closeIt' in ClassAttribute:
                    # Click on work dropdown
                    li.find_element(By.TAG_NAME, 'a').click()
                    try:
                        # find <a> tag in work dropdown
                        a_links = li.find_elements(By.TAG_NAME, 'a')
                        for a in a_links:
                            if a.text == "Time Logs":
                                a.click()
                    except NoSuchElementException:
                        print("You do not have access to Time Logs Page.")
                else:
                    try:
                        # find <a> tag in work dropdown
                        a_links = li.find_elements(By.TAG_NAME, 'a')
                        for a in a_links:
                            if a.text == "Time Logs":
                                a.click()
                    except NoSuchElementException:
                        print("You do not have access to Time Logs Page.")
        except StaleElementReferenceException:
            continue
    time.sleep(3)
    if driver.title == "Time Logs":
        print("Successfully reached at Time Logs page")
        logger.info("Successfully reached at Time Logs page")


@pytest.mark.order(39)
def test_TimeLogSearch(driver):
    # find the saved Time log in
    Search = driver.find_element(By.XPATH, '//*[@id="search-text-field"]')
    Search.send_keys("Task Testing")
    time.sleep(10)


@pytest.mark.order(40)
def test_DeleteTimeLog(driver):
    time.sleep(5)
    Table = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody')
    Rows = Table.find_elements(By.TAG_NAME, 'tr')
    length = len(Rows)
    print("There are %s Rows in time log" % length)

    for i in range(1,length):
        NewLength = len(Rows)
        if NewLength != 1:
            Cell1 = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]/h5')
            TaskName = Cell1.text
        else:
            Cell1 = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr/td[3]/h5')
            TaskName = Cell1.text
        if TaskName == "Task Testing":
            driver.find_element(By.XPATH, f'/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[8]/div/div/a').click()
            driver.find_element(By.XPATH, f'/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[8]/div/div/div/a[3]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="body"]/div[8]/div/div[3]/button[1]').click()
            time.sleep(10)
            print("The " + TaskName + " Log deleted successfully from the table")


@pytest.mark.order(41)
def test_ClickOnTasksPage(driver, selenium):
    Ul = driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul')
    lis = Ul.find_elements(By.TAG_NAME, 'li')
    i = 0
    # Click on Work dropdown
    for li in lis:
        i = i + 1
        try:
            if li.find_element(By.TAG_NAME, 'a').text == "Work":
                ClassAttribute = li.get_attribute('class')
                if 'closeIt' in ClassAttribute:
                    # Click on work dropdown
                    li.find_element(By.TAG_NAME, 'a').click()
                    try:
                        # find <a> tag in work dropdown
                        a_links = li.find_elements(By.TAG_NAME, 'a')
                        for a in a_links:
                            if a.text == "Tasks":
                                a.click()
                    except NoSuchElementException:
                        print("You do not have access to Time Logs Page.")
                else:
                    try:
                        # find <a> tag in work dropdown
                        a_links = li.find_elements(By.TAG_NAME, 'a')
                        for a in a_links:
                            if a.text == "Tasks":
                                a.click()
                    except NoSuchElementException:
                        print("You do not have access to Time Logs Page.")
        except StaleElementReferenceException:
            continue
    time.sleep(3)
    if driver.title == "Tasks":
        print("Successfully reached at Tasks page")
        logger.info("Successfully reached at Tasks page")


@pytest.mark.order(42)
def test_TaskSearch(driver):
    # find the saved Tasks
    Search = driver.find_element(By.XPATH, '//*[@id="search-text-field"]')
    Search.send_keys("Task Testing")
    time.sleep(7)


@pytest.mark.order(43)
def test_DeleteTask(driver):
    time.sleep(5)
    Table = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody')
    Rows = Table.find_elements(By.TAG_NAME, 'tr')
    length = len(Rows)
    print("There are %s Rows in Tasks" % length)

    for i in range(1,length):
        NewLength = len(Rows)
        if NewLength != 1:
            Cell1 = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]/div/div/h5')
            TaskName = Cell1.text
        else:
            Cell1 = driver.find_element(By.XPATH,
                                        '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr/td[3]/div/div/h5')
            TaskName = Cell1.text
        if TaskName == "Task Testing":
            driver.find_element(By.XPATH, f'/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[10]/div/div/a').click()
            driver.find_element(By.XPATH, f'/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[10]/div/div/div/a[3]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div[8]/div/div[3]/button[1]').click()
            time.sleep(10)
            print("The '" + TaskName + "' Task deleted successfully from the table")


@pytest.mark.order(44)
def test_ClickOnProjectsPage(driver, selenium):
    Ul = driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul')
    lis = Ul.find_elements(By.TAG_NAME, 'li')
    i = 0
    # Click on Work dropdown
    for li in lis:
        i = i + 1
        try:
            if li.find_element(By.TAG_NAME, 'a').text == "Work":
                ClassAttribute = li.get_attribute('class')
                if 'closeIt' in ClassAttribute:
                    # Click on work dropdown
                    li.find_element(By.TAG_NAME, 'a').click()
                    try:
                        # find <a> tag in work dropdown
                        a_links = li.find_elements(By.TAG_NAME, 'a')
                        for a in a_links:
                            if a.text == "Projects":
                                a.click()
                    except NoSuchElementException:
                        print("You do not have access to Time Logs Page.")
                else:
                    try:
                        # find <a> tag in work dropdown
                        a_links = li.find_elements(By.TAG_NAME, 'a')
                        for a in a_links:
                            if a.text == "Projects":
                                a.click()
                    except NoSuchElementException:
                        print("You do not have access to Time Logs Page.")
        except StaleElementReferenceException:
            continue
    time.sleep(3)
    if driver.title == "Projects":
        print("Successfully reached at Projects page")
        logger.info("Successfully reached at Projects page")


@pytest.mark.order(45)
def test_ProjectSearch(driver):
    # find the saved Tasks
    Search = driver.find_element(By.XPATH, '//*[@id="search-text-field"]')
    Search.send_keys("Project Testing")
    time.sleep(7)


@pytest.mark.order(46)
def test_DeleteProject(driver):
    time.sleep(5)
    Table = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody')
    Rows = Table.find_elements(By.TAG_NAME, 'tr')
    length = len(Rows)
    print("There are %s Rows in Projects" % length)
    for i in range(1,length):
        NewLength = len(Rows)
        if NewLength != 1:
            Cell1 = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]/div/div/h5')
            project_name = Cell1.text
            if project_name == "Project Testing":
                driver.find_element(By.XPATH,
                                    f'/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[10]/div/div/a').click()
                driver.find_element(By.XPATH,
                                    f'/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[10]/div/div/div/a[3]').click()
                time.sleep(3)
                driver.find_element(By.XPATH, '/html/body/div[8]/div/div[3]/button[1]').click()
                time.sleep(10)
                print("The '" + project_name + "' Task deleted successfully from the table")
        else:
            Cell1 = driver.find_element(By.XPATH,
                                        '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr/td[3]/div/div/h5')
            project_name = Cell1.text
            if project_name == "Project Testing":
                driver.find_element(By.XPATH,
                                    f'/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr/td[10]/div/div/a').click()
                driver.find_element(By.XPATH,
                                    f'/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr/td[10]/div/div/div/a[3]').click()
                time.sleep(3)
                driver.find_element(By.XPATH, '/html/body/div[8]/div/div[3]/button[1]').click()
                time.sleep(10)
                print("The '" + project_name + "' Project deleted successfully from the table")
