import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create a logger instance
logger = logging.getLogger(__name__)

# Global variables used for different methods POC-QA-Automation
ValidEmail = "saurabhdhariwal.com@gmail.com"
ValidPass = "addweb123"

# Global variables used for different methods POC-QA-Automation
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

wait = ""


@pytest.fixture(name="nvar")
def test_NewVar(driver):
    Project = driver.find_element(By.XPATH,
                                  '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[1]/div/div/button')
    Task = driver.find_element(By.XPATH,
                               '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[2]/div/div/button')
    Employee = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[3]/div/div/button')
    Date = driver.find_element(By.XPATH, '//*[@id="start_date"]')
    Hr = driver.find_element(By.XPATH,
                             '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[5]/div/div/button')
    Min = driver.find_element(By.XPATH,
                              '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[6]/div/div/button')
    Memo = driver.find_element(By.XPATH, '//*[@id="memo"]')
    Save = driver.find_element(By.XPATH, '//*[@id="save-timelog-form"]')
    Cancel = driver.find_element(By.XPATH, '//*[@id="right-modal-content"]/div/div/div/div/a')
    AddMore = driver.find_element(By.XPATH, '//*[@id="add-more-form"]')
    return Project, Task, Employee, Date, Hr, Min, Memo, Save, Cancel, AddMore


@pytest.mark.order(30)
def test_ClickOnTimelogPage(driver, selenium):
    global wait
    wait = WebDriverWait(driver, 30)
    ul = driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul')
    lis = ul.find_elements(By.TAG_NAME, 'li')
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
    # time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="table-actions"]/a')))
    time.sleep(2)
    if driver.title == "Time Logs":
        print("Successfully reached at Time Logs page")
        logger.info("Successfully reached at Time Logs page")


@pytest.mark.order(31)
def test_LogTimeButton(driver):
    LogTime = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a')
    assert LogTime.is_enabled()
    print("The Log Time button is Enabled.")
    logger.info("The Log Time button is Enabled.")
    LogTime.click()
    # time.sleep(7)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[1]/div/div/button')))
    time.sleep(3)


@pytest.mark.order(32)
def test_ValidateComponents(driver, nvar):
    Project, Task, Employee, Date, Hr, Min, Memo, Save, Cancel, AddMore = nvar

    assert Project.is_enabled()
    print("The Project dropdown is Enabled.")
    logger.info("The Project dropdown is Enabled.")
    assert Task.is_enabled()
    print("The Task dropdown is Enabled.")
    logger.info("The Task dropdown is Enabled.")
    assert Employee.is_enabled()
    print("The Employee dropdown is Enabled.")
    logger.info("The Employee dropdown is Enabled.")
    assert Date.is_enabled()
    print("The Date picker is Enabled.")
    logger.info("The Date picker is Enabled.")
    assert Hr.is_enabled()
    print("The hour dropdown is Enabled.")
    logger.info("The hour dropdown is Enabled.")
    assert Min.is_enabled()
    print("The Minutes dropdown is Enabled.")
    logger.info("The Minutes dropdown is Enabled.")
    assert Memo.is_enabled()
    print("The Memo textarea is Enabled.")
    logger.info("The Memo textarea is Enabled.")
    assert Save.is_enabled()
    print("The Save button is Enabled.")
    logger.info("The Save button is Enabled.")
    assert Cancel.is_enabled()
    print("The Cancel button is Enabled.")
    logger.info("The Cancel button is Enabled.")
    assert AddMore.is_enabled()
    print("The Add more button is Enabled.")
    logger.info("The Add more is Enabled.")


@pytest.mark.order(33)
def test_WithBlankValue(driver, nvar):
    Project, Task, Employee, Date, Hr, Min, Memo, Save, Cancel, AddMore = nvar

    Save.click()
    # time.sleep(4)
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[1]/div/div[2]')))
    time.sleep(2)
    ProjectMsg = driver.find_element(By.XPATH,
                                      '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[1]/div/div[2]')
    TaskMsg = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[2]/div/div[2]')
    EmployeeMsg = driver.find_element(By.XPATH,
                                       '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[3]/div/div[2]')
    EndtimeMsg = driver.find_element(By.XPATH,
                                      '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[4]/div/div/div')
    MemoMsg = driver.find_element(By.XPATH, '//*[@id="save-timelog-data-form"]/div/div[2]/div[2]/div/div')

    if ProjectMsg.text == "Please select Project":
        print('"Please select Project." Message displayed successfully.')
        logger.info('"Please select Project." Message displayed successfully.')
    if TaskMsg.text == "Please select Task":
        print('"Please select Task." Message displayed successfully.')
        logger.info('"Please select Task." Message displayed successfully.')
    if EmployeeMsg.text == "Please select user":
        print('"Please select user" Message displayed successfully.')
        logger.info('"Please select user" Message displayed successfully.')
    if EndtimeMsg.text == "Please enter end time ":
        print('"Please enter end time " Message displayed successfully.')
        logger.info('"Please enter end time " Message displayed successfully.')
    if MemoMsg.text == "Please enter Memo":
        print('"Please enter Memo" Message displayed successfully.')
        logger.info('"Please enter Memo" Message displayed successfully.')


@pytest.mark.order(34)
def test_WithInvalidValue(driver, nvar):
    Project, Task, Employee, Date, Hr, Min, Memo, Save, Cancel, AddMore = nvar

    # Click on Project dropdown
    Project.click()
    ProjectSrch = driver.find_element(By.XPATH,
                                       '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/input')
    # Search for valid option
    ProjectSrch.send_keys(InvalidProject)
    LiElements = driver.find_elements(By.TAG_NAME, 'li')
    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in LiElements:
        if li.get_attribute('class') == 'no-results':
            print('"No result found" message displayed successfully for invalid search in Project dropdown')
            break
    # Click on Task dropdown
    try:
        Task.click()
    except StaleElementReferenceException:
        Task = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[2]/div/div/button')
        Task.click()
    TaskSrch = driver.find_element(By.XPATH,
                                    '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[1]/input')
    # Search for valid option
    TaskSrch.send_keys(ValidTask)
    LiElements = driver.find_elements(By.TAG_NAME, 'li')
    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in LiElements:
        if li.get_attribute('class') == 'no-results':
            print('"No result found" message displayed successfully for invalid search in Task dropdown')
            break
    # Click on Employee dropdown
    try:
        Employee.click()
    except StaleElementReferenceException:
        Employee = driver.find_element(By.XPATH,
                                       '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[3]/div/div/button')
        Employee.click()
    EmpSrch = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div[1]/input')
    # Search for valid option
    EmpSrch.send_keys(ValidEmployee)
    LiElements = driver.find_elements(By.TAG_NAME, 'li')
    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in LiElements:
        if li.get_attribute('class') == 'no-results':
            print('"No result found" message displayed successfully for invalid search in Employee dropdown')
            break
    # Click on the active <li> element
    if active_a is not None:
        active_a.click()
    # Click on Date input
    try:
        Date.click()
    except StaleElementReferenceException:
        Date = driver.find_element(By.XPATH, '//*[@id="start_date"]')
    # Search for valid option
    Date.clear()
    Date.send_keys(InvalidDate)
    # Click on Minutes dropdown
    Min = driver.find_element(By.XPATH,
                              '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[6]/div/div/button')
    Min.click()
    MinSrch = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[6]/div/div/div/div[1]/input')
    # Search for valid option
    MinSrch.send_keys(InvalidMin)
    LiElements = driver.find_elements(By.TAG_NAME, 'li')
    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in LiElements:
        if li.get_attribute('class') == 'no-results':
            print('"No result found" message displayed successfully for invalid search in Minutes Dropdown')
            break
    # Click on the active <li> element
    if active_a is not None:
        active_a.click()
    # Click on Hours dropdown
    Hr = driver.find_element(By.XPATH,
                             '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[5]/div/div/button')
    Hr.click()
    HrSrch = driver.find_element(By.XPATH,
                                  '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[5]/div/div/div/div[1]/input')
    # Search for valid option
    HrSrch.send_keys(InvalidHour)
    LiElements = driver.find_elements(By.TAG_NAME, 'li')
    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in LiElements:
        if li.get_attribute('class') == 'no-results':
            print('"No result found" message displayed successfully for invalid search in Hours dropdown')
            break
    # Click on the active <li> element
    if active_a is not None:
        active_a.click()
    # Click on Memo input
    Memo = driver.find_element(By.XPATH, '//*[@id="memo"]')
    # Search for valid option
    Memo.clear()
    Memo.send_keys(InvalidMemo)


@pytest.mark.order(35)
def test_WithInvalidDateValue(driver, nvar):
    Project, Task, Employee, Date, Hr, Min, Memo, Save, Cancel, AddMore = nvar

    # Click on Project dropdown
    Project.click()
    ProjectSrch = driver.find_element(By.XPATH,
                                       '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/input')
    # Search for valid option
    ProjectSrch.send_keys(ValidProject)
    LiElements = driver.find_elements(By.TAG_NAME, 'li')
    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in LiElements:
        if li.get_attribute('class') == 'active':
            active_a = li.find_element(By.TAG_NAME, 'a')
            break
    # Click on the active <li> element
    if active_a is not None:
        active_a.click()
    # Click on Task dropdown
    try:
        Task.click()
    except StaleElementReferenceException:
        Task = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[2]/div/div/button')
        Task.click()
    TaskSrch = driver.find_element(By.XPATH,
                                    '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[1]/input')
    # Search for valid option
    TaskSrch.send_keys(ValidTask)
    LiElements = driver.find_elements(By.TAG_NAME, 'li')
    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in LiElements:
        if li.get_attribute('class') == 'active':
            active_a = li.find_element(By.TAG_NAME, 'a')
            break
    # Click on the active <li> element
    if active_a is not None:
        active_a.click()
    # Click on Employee dropdown
    try:
        Employee.click()
    except StaleElementReferenceException:
        Employee = driver.find_element(By.XPATH,
                                       '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[3]/div/div/button')
        Employee.click()
    EmpSrch = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div[1]/input')
    # Search for valid option
    EmpSrch.send_keys(ValidEmployee)
    LiElements = driver.find_elements(By.TAG_NAME, 'li')
    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in LiElements:
        if li.get_attribute('class') == 'active':
            active_a = li.find_element(By.TAG_NAME, 'a')
            break
    # Click on the active <li> element
    if active_a is not None:
        active_a.click()
    # Click on Minutes dropdown
    Min = driver.find_element(By.XPATH,
                              '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[6]/div/div/button')
    Min.click()
    MinSrch = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[6]/div/div/div/div[1]/input')
    # Search for valid option
    MinSrch.send_keys(ValidMin)
    LiElements = driver.find_elements(By.TAG_NAME, 'li')
    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in LiElements:
        if li.get_attribute('class') == 'active':
            active_a = li.find_element(By.TAG_NAME, 'a')
            break
    # Click on the active <li> element
    if active_a is not None:
        active_a.click()
    # Click on Hours dropdown
    Hr = driver.find_element(By.XPATH,
                             '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[5]/div/div/button')
    Hr.click()
    HrSrch = driver.find_element(By.XPATH,
                                  '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[5]/div/div/div/div[1]/input')
    # Search for valid option
    HrSrch.send_keys(ValidHour)
    LiElements = driver.find_elements(By.TAG_NAME, 'li')
    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in LiElements:
        if li.get_attribute('class') == 'active':
            active_a = li.find_element(By.TAG_NAME, 'a')
            break
    # Click on the active <li> element
    if active_a is not None:
        active_a.click()
    # Click on Memo input
    Memo = driver.find_element(By.XPATH, '//*[@id="memo"]')
    # Search for valid option
    Memo.clear()
    Memo.send_keys(ValidMemo)
    # Click on Date input
    try:
        Date.click()
    except StaleElementReferenceException:
        Date = driver.find_element(By.XPATH, '//*[@id="start_date"]')
    # Search for valid option
    Date.clear()
    Date.send_keys(InvalidDate)
    Save.click()
    time.sleep(1)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="body"]/div[8]')))
    time.sleep(1)
    Date_err = driver.find_element(By.XPATH, '//*[@id="body"]/div[8]')
    if Date_err.text == "A two digit day could not be found Data missing":
        print('"A two digit day could not be found Data missing" Message displayed successfully')
    # Close the web driver
    time.sleep(3)


@pytest.mark.order(36)
def test_WithValidValue(driver, nvar):
    Project, Task, Employee, Date, Hr, Min, Memo, Save, Cancel, AddMore = nvar

    # Click on Project dropdown
    Project.click()
    ProjectSrch = driver.find_element(By.XPATH,
                                       '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/input')
    # Search for valid option
    ProjectSrch.send_keys(ValidProject)
    LiElements = driver.find_elements(By.TAG_NAME, 'li')
    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in LiElements:
        if li.get_attribute('class') == 'active':
            active_a = li.find_element(By.TAG_NAME, 'a')
            break
    # Click on the active <li> element
    if active_a is not None:
        active_a.click()
    time.sleep(2)
    # Click on Task dropdown
    try:
        Task.click()
    except StaleElementReferenceException:
        Task = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[2]/div/div/button')
        Task.click()
    TaskSrch = driver.find_element(By.XPATH,
                                    '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[1]/input')
    # Search for valid option
    TaskSrch.send_keys(ValidTask)
    LiElements = driver.find_elements(By.TAG_NAME, 'li')
    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in LiElements:
        if li.get_attribute('class') == 'active':
            active_a = li.find_element(By.TAG_NAME, 'a')
            break
    # Click on the active <li> element
    if active_a is not None:
        active_a.click()
    time.sleep(2)
    # Click on Employee dropdown
    try:
        Employee.click()
    except StaleElementReferenceException:
        Employee = driver.find_element(By.XPATH,
                                       '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[3]/div/div/button')
        Employee.click()
    EmpSrch = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div[1]/input')
    # Search for valid option
    EmpSrch.send_keys(ValidEmployee)
    LiElements = driver.find_elements(By.TAG_NAME, 'li')
    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in LiElements:
        if li.get_attribute('class') == 'active':
            active_a = li.find_element(By.TAG_NAME, 'a')
            break
    # Click on the active <li> element
    if active_a is not None:
        active_a.click()
    time.sleep(2)
    # Click on Date input
    try:
        Date.click()
    except StaleElementReferenceException:
        Date = driver.find_element(By.XPATH, '//*[@id="start_date"]')
    # Search for valid option
    Date.clear()
    Date.send_keys(ValidDate)
    s_Date = driver.find_element(By.XPATH, '//*[@id="start_time"]')
    s_Date.click()
    # Click on Minutes dropdown
    Min = driver.find_element(By.XPATH,
                              '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[6]/div/div/button')
    Min.click()
    MinSrch = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[6]/div/div/div/div[1]/input')
    # Search for valid option
    MinSrch.send_keys(ValidMin)
    LiElements = driver.find_elements(By.TAG_NAME, 'li')
    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in LiElements:
        if li.get_attribute('class') == 'active':
            active_a = li.find_element(By.TAG_NAME, 'a')
            break
    # Click on the active <li> element
    if active_a is not None:
        active_a.click()
    # Click on Hours dropdown
    Hr = driver.find_element(By.XPATH,
                             '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[5]/div/div/button')
    Hr.click()
    HrSrch = driver.find_element(By.XPATH,
                                  '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[5]/div/div/div/div[1]/input')
    # Search for valid option
    HrSrch.send_keys(ValidHour)
    LiElements = driver.find_elements(By.TAG_NAME, 'li')
    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in LiElements:
        if li.get_attribute('class') == 'active':
            active_a = li.find_element(By.TAG_NAME, 'a')
            break
    # Click on the active <li> element
    if active_a is not None:
        active_a.click()
    # Click on Memo input
    Memo = driver.find_element(By.XPATH, '//*[@id="memo"]')
    # Search for valid option
    Memo.clear()
    Memo.send_keys(ValidMemo)
    # Click on Memo input
    Save.click()
    # time.sleep(6)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//table//tbody//tr[1]')))
    time.sleep(3)
    LogTime = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a')
    if LogTime.is_enabled():
        print("The form with valid data Saved successfully.")


@pytest.mark.order(37)
def test_SearchInTable(driver):
    # find the Saved lead in table and click on edit button
    Row1 = driver.find_element(By.XPATH, '//table//tbody//tr[1]')
    Cell1 = Row1.find_element(By.XPATH, './/td[2]')
    VarId = Cell1.text
    driver.find_element(By.XPATH, f'//*[@id="dropdownMenuLink-%s"]' % VarId).click()
    time.sleep(2)
    driver.find_element(By.XPATH, f'//*[@id="row-%s"]/td[8]/div/div/div/a[2]' % VarId).click()
    print("The Log searched successfully in the table")
    # time.sleep(5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="memo"]')))
    time.sleep(3)


@pytest.mark.order(38)
def test_EditAndSave(driver):
    Memo = driver.find_element(By.XPATH, '//*[@id="memo"]')
    # Search for valid option
    Memo.clear()
    Memo.send_keys("Testing Edit form by changing the value of Memo textarea ...")
    Save = driver.find_element(By.XPATH, '//*[@id="save-timelog-form"]')
    Save.click()
    # time.sleep(6)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="table-actions"]/a')))
    time.sleep(3)
    LogTime = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a')
    if LogTime.is_enabled():
        print("The Edit form Saved successfully.")
    # Close the web driver
    time.sleep(3)
