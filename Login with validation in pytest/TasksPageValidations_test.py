import pytest
import logging
from selenium.common import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver.common.by import By
import time

# create a logger instance
logger = logging.getLogger(__name__)

# Global variables used for different methods POC-QA-Automation
ValidEmail = "saurabhdhariwal.com@gmail.com"
ValidPass = "addweb123"

ValidTitle = "Task Testing"
InvalidTitle = "$$ Nothing $$"

ValidCategory = "QA"
InvalidCategory = "$$ Nothing $$"

ValidProject = "Project Testing"
InvalidProject = "$$ Nothing $$"

ValidStartDate = "17-05-2023"
InvalidStartDate = "32-05-2023"

ValidDueDate = "18-05-2023"
InvalidDueDate = "32-05-2023"

ValidAssigned = "Pathan UveshMohammad"
InvalidAssigned = "$$ Nothing $$"

ValidLable = "QA"
InvalidLable = "$$ Nothing $$"

ValidStatus = "In-Progress"
InvalidStatus = "$$ Nothing $$"

ValidDescription = "Testing Description..."
InvalidDescription = "$$ Nothing $$"


@pytest.fixture(name="nvar")
def test_NewVar(driver):
    Title = driver.find_element(By.XPATH, '//*[@id="heading"]')
    Category = driver.find_element(By.XPATH, '//*[@id="save-task-data-form"]/div/div[1]/div[2]/div/div[1]/button')
    Project = driver.find_element(By.XPATH, '//*[@id="save-task-data-form"]/div/div[1]/div[3]/div/div/button')
    StartDate = driver.find_element(By.XPATH, '//*[@id="task_start_date"]')
    Duedate = driver.find_element(By.XPATH, '//*[@id="due_date"]')
    WithoutDuedate = driver.find_element(By.XPATH, '//*[@id="without_duedate"]')
    Assigned = driver.find_element(By.XPATH, '//*[@id="save-task-data-form"]/div/div[1]/div[9]/div/div/div[1]/button')
    Lable = driver.find_element(By.XPATH, '//*[@id="save-task-data-form"]/div/div[1]/div[10]/div/div/div[1]/button')
    Status = driver.find_element(By.XPATH, '//*[@id="save-task-data-form"]/div/div[1]/div[11]/div/div/button')
    Description = driver.find_element(By.XPATH, '//*[@id="description"]/div[1]')
    OtherTopics = driver.find_element(By.XPATH, '//*[@id="save-task-data-form"]/div/h4[2]/a')
    Milestone = driver.find_element(By.XPATH, '//*[@id="other-details"]/div[1]/div/div[1]/div/div/button')
    Priority = driver.find_element(By.XPATH, '//*[@id="other-details"]/div[1]/div/div[2]/div/div/button')
    Save = driver.find_element(By.XPATH, '//*[@id="save-task-form"]')
    Cancel = driver.find_element(By.XPATH, '//*[@id="save-task-data-form"]/div/div[3]/a')

    return Title, Category, Project, StartDate, Duedate, WithoutDuedate, Assigned, Lable, Status, Description, \
        OtherTopics, Milestone, Priority, Save, Cancel


@pytest.mark.order(22)
def test_ClickOnTask(driver, selenium):
    ul = driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul')
    lis = ul.find_elements(By.TAG_NAME, 'li')
    i = 0
    # Click on Work dropdown
    for li in lis:
        i = i + 1
        try:
            if li.find_element(By.TAG_NAME, 'a').text == "Work":
                class_attribute = li.get_attribute('class')
                if 'closeIt' in class_attribute:
                    # Click on work dropdown
                    li.find_element(By.TAG_NAME, 'a').click()
                    try:
                        # find <a> tag in work dropdown
                        a_links = li.find_elements(By.TAG_NAME, 'a')
                        for a in a_links:
                            if a.text == "Tasks":
                                a.click()
                    except NoSuchElementException:
                        print("You do not have access to Tasks Page.")
                else:
                    try:
                        # find <a> tag in work dropdown
                        a_links = li.find_elements(By.TAG_NAME, 'a')
                        for a in a_links:
                            if a.text == "Tasks":
                                a.click()
                    except NoSuchElementException:
                        print("You do not have access to Tasks Page.")
        except StaleElementReferenceException:
            continue
    time.sleep(4)
    if driver.Title == "Tasks":
        print("Successfully reached at Tasks page")
        logger.info("Successfully reached at Tasks page")


@pytest.mark.order(23)
def test_SearchboxOnTaskPage(driver):
    SearchBox = driver.find_element(By.XPATH, '//*[@id="search-text-field"]')
    SearchBox.send_keys("Testing")
    time.sleep(8)
    try:
        Row1 = driver.find_element(By.XPATH, '//table//tbody//tr[1]')
        Cell1 = Row1.find_element(By.XPATH, './/td[3]')
        if Cell1.text == "Testing":
            print("The search functionality is working properly.")
    except NoSuchElementException:
        print("The value is not found in the table")


@pytest.mark.order(24)
def test_AddTaskButton(driver):
    AddTask = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a[1]')
    assert AddTask.is_enabled()
    print("The Add Task button is Enabled.")
    logger.info("The Add Task button is Enabled.")
    AddTask.click()
    time.sleep(5)


@pytest.mark.order(25)
def test_ValidateComponents(driver, nvar):
    Title, Category, Project, StartDate, Duedate, WithoutDuedate, Assigned, Lable, Status, Description, \
        OtherTopics, Milestone, Priority, Save, Cancel = nvar

    assert Title.is_enabled()
    print("The Title textbox is Enabled.")
    logger.info("The Title textbox is Enabled.")
    assert Category.is_enabled()
    print("The Category dropdown is Enabled.")
    logger.info("The Category dropdown is Enabled.")
    assert Project.is_enabled()
    print("The Project dropdown is Enabled.")
    logger.info("The Project dropdown is Enabled.")
    assert StartDate.is_enabled()
    print("The start date input is Enabled.")
    logger.info("The start date input is Enabled.")
    assert Duedate.is_enabled()
    print("The Due date input is Enabled.")
    logger.info("The Due date input is Enabled.")
    assert WithoutDuedate.is_enabled()
    print("The WithoutDuedate checkbox is Enabled.")
    logger.info("The WithoutDuedate checkbox is Enabled.")
    assert Assigned.is_enabled()
    print("The Assigned To dropdown is Enabled.")
    logger.info("The Assigned To dropdown is Enabled.")
    assert Lable.is_enabled()
    print("The Lable dropdown is Enabled.")
    logger.info("The Lable dropdown is Enabled.")
    assert Status.is_enabled()
    print("The Status dropdown is Enabled.")
    logger.info("The Status dropdown is Enabled.")
    assert Description.is_enabled()
    print("The Description textarea is Enabled.")
    logger.info("The Description textarea is Enabled.")
    assert OtherTopics.is_enabled()
    print("The Other Details button is Enabled.")
    logger.info("The Other Details button is Enabled.")
    OtherTopics.click()
    time.sleep(2)
    assert Milestone.is_enabled()
    print("The Milestones dropdown is Enabled.")
    logger.info("The Milestones dropdown is Enabled.")
    assert Priority.is_enabled()
    print("The Priority dropdown is Enabled.")
    logger.info("The Priority dropdown is Enabled.")
    assert Save.is_enabled()
    print("The Save button is Enabled.")
    logger.info("The Save button is Enabled.")
    assert Cancel.is_enabled()
    print("The Cancel button is Enabled.")
    logger.info("The Cancel button is Enabled.")


@pytest.mark.order(26)
def test_WithValidData(driver, nvar):
    Title, Category, Project, StartDate, Duedate, WithoutDuedate, Assigned, Lable, Status, Description, \
        OtherTopics, Milestone, Priority, Save, Cancel = nvar

    # send keys in Project textbox
    Title.clear()
    Title.send_keys(ValidTitle)
    # Click on Category dropdown
    Category.click()
    CategorySrch = driver.find_element(By.XPATH,
                                        '//*[@id="save-task-data-form"]/div/div[1]/div[2]/div/div[1]/div/div[1]/input')
    # Search for valid option
    CategorySrch.send_keys(ValidCategory)
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
    # Click on Project dropdown
    Project.click()
    ProjectSrch = driver.find_element(By.XPATH,
                                       '//*[@id="save-task-data-form"]/div/div[1]/div[3]/div/div/div/div[1]/input')
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
    time.sleep(4)
    # Click on Start Date input
    StartDate.click()
    # send keys to start date
    StartDate.clear()
    StartDate.send_keys(ValidStartDate)
    # Check Due Date checkbox
    WithoutDuedate.click()
    # Click on Due Date input
    try:
        Duedate.click()
        # send keys to start date
        Duedate.clear()
        Duedate.send_keys(ValidDueDate)
    except ElementNotInteractableException:
        print('When user check the "There is no Project deadline" checkbox the Deadline element removed successfully')
    # Click on Assigned To dropdown
    Assigned.click()
    AssignedSrch = driver.find_element(By.XPATH,
                                        '//*[@id="save-task-data-form"]/div/div[1]/div[9]/div/div/div[1]/div/div[1]/input')
    # Search for valid option
    AssignedSrch.send_keys(ValidAssigned)
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
    # Click on Lable dropdown
    Lable.click()
    LableSrch = driver.find_element(By.XPATH,
                                     '//*[@id="save-task-data-form"]/div/div[1]/div[10]/div/div/div[1]/div/div[1]/input')
    # Search for valid option
    LableSrch.send_keys(ValidLable)
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
    # Click on Status dropdown
    Status.click()
    StatusSrch = driver.find_element(By.XPATH,
                                      '//*[@id="save-task-data-form"]/div/div[1]/div[11]/div/div/div/div[1]/input')
    # Search for valid option
    StatusSrch.send_keys(ValidStatus)
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
    # Click on Description textarea
    Description.clear()
    Description.send_keys(ValidDescription)
    # Select option from Milestone Dropdown
    Milestone.click()
    sel = driver.find_element(By.XPATH, '//*[@id="priority"]')
    sel.select_by_visible_text("Test")
    # Select option from Priority Dropdown
    Priority.click()
    sel = driver.find_element(By.XPATH, '//*[@id="milestone_id"]')
    sel.select_by_visible_text("Low")
    # Save the Add task form
    Save.click()
    time.sleep(8)


@pytest.mark.order(27)
def test_SearchInTable(driver):
    # find the Saved lead in table and click on edit button
    Row1 = driver.find_element(By.XPATH, '//table//tbody//tr[1]')
    Cell1 = Row1.find_element(By.XPATH, './/td[2]')
    VarId = Cell1.text
    driver.find_element(By.XPATH, f'//*[@id="dropdownMenuLink-%s"]' % VarId).click()
    driver.find_element(By.XPATH, f'//*[@id="row-%s"]/td[10]/div/div/div/a[2]' % VarId).click()
    print("The task searched successfully in the table")
    time.sleep(10)


@pytest.mark.order(28)
def test_EditAndSave(driver):

    # Edit Status of Project
    Status = driver.find_element(By.XPATH, '//*[@id="save-task-data-form"]/div/div[1]/div[11]/div/div/button')
    Status.click()
    StatusSrch = driver.find_element(By.XPATH,
                                      '//*[@id="save-task-data-form"]/div/div[1]/div[11]/div/div/div/div[1]/input')
    # Search for valid option
    StatusSrch.send_keys("In-Progress")
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
    # Edit Sprint of Project
    Sprint = driver.find_element(By.XPATH, '//*[@id="save-task-data-form"]/div/div[1]/div[7]/div/div[1]/button')
    Sprint.click()
    StatusSrch = driver.find_element(By.XPATH,
                                      '//*[@id="save-task-data-form"]/div/div[1]/div[7]/div/div[1]/div/div[1]/input')
    # Search for valid option
    StatusSrch.send_keys("sprint 1")
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
    # Save the Edit form
    Save = driver.find_element(By.XPATH, '//*[@id="save-task-form"]')
    Save.click()
    time.sleep(10)
    AddProject = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a')
    if AddProject.is_enabled():
        print("The Edit form Saved successfully.")
    # Close the web driver
    time.sleep(5)
    # driver.close()
