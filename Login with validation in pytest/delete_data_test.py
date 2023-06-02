import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time

# create a logger instance
logger = logging.getLogger(__name__)

# Global variables used for different methods POC-QA-Automation
valid_email = "saurabhdhariwal.com@gmail.com"
valid_pass = "addweb123"

valid_project = "Project Testing"
invalid_project = "Nothing"

valid_task = "Task Testing"
invalid_task = "Nothing"

valid_employee = "Pathan UveshMohammad"
invalid_employee = "Nothing"

valid_date = "17-05-2023"
invalid_date = "32-05-2023"

valid_hour = "3"
invalid_hour = "12"

valid_min = "30"
invalid_min = "60"

valid_memo = "Testing......"
invalid_memo = "Testing......"


@pytest.fixture(name="var")
def Test_Var(driver):
    email = driver.find_element(By.XPATH, '//*[@id="email"]')
    passwrd = driver.find_element(By.XPATH, '//*[@id="password"]')
    login = driver.find_element(By.XPATH, '//*[@id="submit-login"]')
    return email, passwrd, login


def test_Enter_valid_Creadential(driver, var):
    email, passwrd, login = var
    global valid_email
    global valid_pass
    email.clear()
    passwrd.clear()
    email.send_keys(valid_email)
    passwrd.send_keys(valid_pass)
    login.click()

    time.sleep(3)

    if driver.title == "Dashboard":
        print("Successfully Logged in.")
        logger.info("Successfully Logged in.")

    time.sleep(3)


# @pytest.mark.order(25)
def test_Click_on_Timelog_page(driver, selenium):
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/a').click()
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/div/a[4]').click()
    time.sleep(3)
    if driver.title == "Time Logs":
        print("Successfully reached at Time Logs page")
        logger.info("Successfully reached at Time Logs page")


# @pytest.mark.order(32)
def test_Time_log_Search(driver):
    # find the saved Time log in
    search = driver.find_element(By.XPATH, '//*[@id="search-text-field"]')
    search.send_keys("Task Testing")
    time.sleep(7)


# @pytest.mark.order(26)
def test_Delete_Time_log(driver):
    time.sleep(5)

    table = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    length = len(rows)

    print("There are %s rows in time log" % length)

    for i in range(1,length):
        new_length = len(rows)
        if new_length != 1:
            cell1 = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]/h5')
            task_name = cell1.text

        else:
            cell1 = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr/td[3]/h5')
            task_name = cell1.text

        if task_name == "Task Testing":

            driver.find_element(By.XPATH, f'/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[8]/div/div/a').click()
            driver.find_element(By.XPATH, f'/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[8]/div/div/div/a[3]').click()

            time.sleep(3)

            driver.find_element(By.XPATH, '//*[@id="body"]/div[8]/div/div[3]/button[1]').click()

            time.sleep(3)

            print("The " + task_name + " Log deleted successfully from the table")


# @pytest.mark.order(25)
def test_Click_on_Tasks_page(driver, selenium):
    # driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/a').click()
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/div/a[3]').click()
    time.sleep(3)
    if driver.title == "Tasks":
        print("Successfully reached at Tasks page")
        logger.info("Successfully reached at Tasks page")


# @pytest.mark.order(32)
def test_Task_Search(driver):
    # find the saved Tasks
    search = driver.find_element(By.XPATH, '//*[@id="search-text-field"]')
    search.send_keys("Task Testing")
    time.sleep(7)


# @pytest.mark.order(26)
def test_Delete_Task(driver):
    time.sleep(5)

    table = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    length = len(rows)

    print("There are %s rows in Tasks" % length)

    for i in range(1,length):
        new_length = len(rows)
        if new_length != 1:
            cell1 = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]/div/div/h5')
            task_name = cell1.text

        else:
            cell1 = driver.find_element(By.XPATH,
                                        '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr/td[3]/div/div/h5')
            task_name = cell1.text

        if task_name == "Task Testing":

            driver.find_element(By.XPATH, f'/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[10]/div/div/a').click()
            driver.find_element(By.XPATH, f'/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[10]/div/div/div/a[3]').click()

            time.sleep(3)

            driver.find_element(By.XPATH, '/html/body/div[8]/div/div[3]/button[1]').click()

            time.sleep(3)

            print("The '" + task_name + "' Task deleted successfully from the table")


# @pytest.mark.order(25)
def test_Click_on_Projects_page(driver, selenium):
    # driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/a').click()
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/div/a[2]').click()
    time.sleep(3)
    if driver.title == "Projects":
        print("Successfully reached at Projects page")
        logger.info("Successfully reached at Projects page")


# @pytest.mark.order(32)
def test_Project_Search(driver):
    # find the saved Tasks
    search = driver.find_element(By.XPATH, '//*[@id="search-text-field"]')
    search.send_keys("Project Testing")
    time.sleep(7)


# @pytest.mark.order(26)
def test_Delete_Project(driver):
    time.sleep(5)

    table = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    length = len(rows)

    print("There are %s rows in Tasks" % length)

    for i in range(1,length):
        new_length = len(rows)
        if new_length != 1:
            cell1 = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]/div/div/h5')
            project_name = cell1.text

            if project_name == "Project Testing":
                driver.find_element(By.XPATH,
                                    f'/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[10]/div/div/a').click()
                driver.find_element(By.XPATH,
                                    f'/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[10]/div/div/div/a[3]').click()

                time.sleep(3)

                driver.find_element(By.XPATH, '/html/body/div[8]/div/div[3]/button[1]').click()

                time.sleep(3)

                print("The '" + project_name + "' Task deleted successfully from the table")

        else:
            cell1 = driver.find_element(By.XPATH,
                                        '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr/td[3]/div/div/h5')
            project_name = cell1.text

            if project_name == "Task Testing":
                driver.find_element(By.XPATH,
                                    f'/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr/td[10]/div/div/a').click()
                driver.find_element(By.XPATH,
                                    f'/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr/td[10]/div/div/div/a[3]').click()

                time.sleep(3)

                driver.find_element(By.XPATH, '/html/body/div[8]/div/div[3]/button[1]').click()

                time.sleep(3)

                print("The '" + project_name + "' Task deleted successfully from the table")

