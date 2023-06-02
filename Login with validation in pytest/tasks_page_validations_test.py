import pytest
import logging

from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import time

# create a logger instance
logger = logging.getLogger(__name__)

# Global variables used for different methods POC-QA-Automation
valid_email = "saurabhdhariwal.com@gmail.com"
valid_pass = "addweb123"

valid_title = "Task Testing"
invalid_title = "$$ Nothing $$"

valid_category = "QA"
invalid_category = "$$ Nothing $$"

valid_project = "Project Testing"
invalid_project = "$$ Nothing $$"

valid_start_date = "17-05-2023"
invalid_start_date = "32-05-2023"

valid_due_date = "18-05-2023"
invalid_due_date = "32-05-2023"

valid_assigned = "Pathan UveshMohammad"
invalid_assigned = "$$ Nothing $$"

valid_lable = "QA"
invalid_lable = "$$ Nothing $$"

valid_status = "In-Progress"
invalid_status = "$$ Nothing $$"

valid_description = "Testing Description..."
invalid_description = "$$ Nothing $$"


# def test_enter_valid_creadential(driver):
#     email = driver.find_element(By.XPATH, '//*[@id="email"]')
#     passwrd = driver.find_element(By.XPATH, '//*[@id="password"]')
#     login = driver.find_element(By.XPATH, '//*[@id="submit-login"]')
#     global valid_email
#     global valid_pass
#
#     email.send_keys(valid_email)
#     passwrd.send_keys(valid_pass)
#     login.click()
#
#     time.sleep(5)


@pytest.fixture(name="nvar")
def Test_new_Var(driver):
    title = driver.find_element(By.XPATH, '//*[@id="heading"]')
    category = driver.find_element(By.XPATH, '//*[@id="save-task-data-form"]/div/div[1]/div[2]/div/div[1]/button')
    project = driver.find_element(By.XPATH, '//*[@id="save-task-data-form"]/div/div[1]/div[3]/div/div/button')
    start_date = driver.find_element(By.XPATH, '//*[@id="task_start_date"]')
    duedate = driver.find_element(By.XPATH, '//*[@id="due_date"]')
    without_duedate = driver.find_element(By.XPATH, '//*[@id="without_duedate"]')
    assigned = driver.find_element(By.XPATH, '//*[@id="save-task-data-form"]/div/div[1]/div[9]/div/div/div[1]/button')
    lable = driver.find_element(By.XPATH, '//*[@id="save-task-data-form"]/div/div[1]/div[10]/div/div/div[1]/button')
    status = driver.find_element(By.XPATH, '//*[@id="save-task-data-form"]/div/div[1]/div[11]/div/div/button')
    description = driver.find_element(By.XPATH, '//*[@id="description"]/div[1]')
    other_topics = driver.find_element(By.XPATH, '//*[@id="save-task-data-form"]/div/h4[2]/a')
    milestone = driver.find_element(By.XPATH, '//*[@id="other-details"]/div[1]/div/div[1]/div/div/button')
    priority = driver.find_element(By.XPATH, '//*[@id="other-details"]/div[1]/div/div[2]/div/div/button')
    save = driver.find_element(By.XPATH, '//*[@id="save-task-form"]')
    cancel = driver.find_element(By.XPATH, '//*[@id="save-task-data-form"]/div/div[3]/a')

    return title, category, project, start_date, duedate, without_duedate, assigned, lable, status, description, \
        other_topics, milestone, priority, save, cancel


@pytest.mark.order(18)
def Test_Click_on_Task(driver, selenium):
    # driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/a').click()
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/div/a[3]').click()
    time.sleep(4)
    if driver.title == "Tasks":
        print("Successfully reached at Tasks page")
        logger.info("Successfully reached at Tasks page")


@pytest.mark.order(19)
def Test_Searchbox_on_Task_page(driver):
    search_box = driver.find_element(By.XPATH, '//*[@id="search-text-field"]')
    search_box.send_keys("Testing")
    time.sleep(8)

    try:
        row1 = driver.find_element(By.XPATH, '//table//tbody//tr[1]')
        cell1 = row1.find_element(By.XPATH, './/td[3]')
        if cell1.text == "Testing":
            print("The search functionality is working properly.")
    except NoSuchElementException:
        print("The value is not found in the table")


@pytest.mark.order(20)
def Test_Add_task_Button(driver):
    add_task = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a[1]')
    assert add_task.is_enabled()
    print("The Add Task button is Enabled.")
    logger.info("The Add Task button is Enabled.")
    add_task.click()
    time.sleep(5)


@pytest.mark.order(21)
def Test_Validate_Components(driver, nvar):
    title, category, project, start_date, duedate, without_duedate, assigned, lable, status, description, \
        other_topics, milestone, priority, save, cancel = nvar

    assert title.is_enabled()
    print("The title textbox is Enabled.")
    logger.info("The title textbox is Enabled.")

    assert category.is_enabled()
    print("The category dropdown is Enabled.")
    logger.info("The category dropdown is Enabled.")

    assert project.is_enabled()
    print("The project dropdown is Enabled.")
    logger.info("The project dropdown is Enabled.")

    assert start_date.is_enabled()
    print("The start date input is Enabled.")
    logger.info("The start date input is Enabled.")

    assert duedate.is_enabled()
    print("The Due date input is Enabled.")
    logger.info("The Due date input is Enabled.")

    assert without_duedate.is_enabled()
    print("The without_duedate checkbox is Enabled.")
    logger.info("The without_duedate checkbox is Enabled.")

    assert assigned.is_enabled()
    print("The Assigned To dropdown is Enabled.")
    logger.info("The Assigned To dropdown is Enabled.")

    assert lable.is_enabled()
    print("The Lable dropdown is Enabled.")
    logger.info("The Lable dropdown is Enabled.")

    assert status.is_enabled()
    print("The Status dropdown is Enabled.")
    logger.info("The Status dropdown is Enabled.")

    assert description.is_enabled()
    print("The Description textarea is Enabled.")
    logger.info("The Description textarea is Enabled.")

    assert other_topics.is_enabled()
    print("The Other Details button is Enabled.")
    logger.info("The Other Details button is Enabled.")
    other_topics.click()
    time.sleep(2)

    assert milestone.is_enabled()
    print("The Milestones dropdown is Enabled.")
    logger.info("The Milestones dropdown is Enabled.")

    assert priority.is_enabled()
    print("The Priority dropdown is Enabled.")
    logger.info("The Priority dropdown is Enabled.")

    assert save.is_enabled()
    print("The save button is Enabled.")
    logger.info("The save button is Enabled.")

    assert cancel.is_enabled()
    print("The cancel button is Enabled.")
    logger.info("The cancel button is Enabled.")


@pytest.mark.order(22)
def Test_with_Valid_Data(driver, nvar):
    title, category, project, start_date, duedate, without_duedate, assigned, lable, status, description, \
        other_topics, milestone, priority, save, cancel = nvar

    # send keys in project textbox
    title.clear()
    title.send_keys(valid_title)

    # Click on Category dropdown
    category.click()

    category_srch = driver.find_element(By.XPATH,
                                        '//*[@id="save-task-data-form"]/div/div[1]/div[2]/div/div[1]/div/div[1]/input')

    # Search for valid option
    category_srch.send_keys(valid_category)

    li_elements = driver.find_elements(By.TAG_NAME, 'li')

    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in li_elements:
        if li.get_attribute('class') == 'active':
            active_a = li.find_element(By.TAG_NAME, 'a')
            break

    # Click on the active <li> element
    if active_a is not None:
        active_a.click()

    # Click on Project dropdown
    project.click()

    project_srch = driver.find_element(By.XPATH,
                                       '//*[@id="save-task-data-form"]/div/div[1]/div[3]/div/div/div/div[1]/input')

    # Search for valid option
    project_srch.send_keys(valid_project)

    li_elements = driver.find_elements(By.TAG_NAME, 'li')

    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in li_elements:
        if li.get_attribute('class') == 'active':
            active_a = li.find_element(By.TAG_NAME, 'a')
            break

    # Click on the active <li> element
    if active_a is not None:
        active_a.click()

    # Click on Start Date input
    start_date.click()

    # send keys to start date
    start_date.clear()
    start_date.send_keys(valid_start_date)

    # Check Due Date checkbox
    without_duedate.click()

    # Click on Due Date input
    try:
        duedate.click()
        # send keys to start date
        duedate.clear()
        duedate.send_keys(valid_due_date)

    except ElementNotInteractableException:
        print('When user check the "There is no project deadline" checkbox the Deadline element removed successfully')

    # Click on Assigned To dropdown
    assigned.click()

    assigned_srch = driver.find_element(By.XPATH,
                                        '//*[@id="save-task-data-form"]/div/div[1]/div[9]/div/div/div[1]/div/div[1]/input')

    # Search for valid option
    assigned_srch.send_keys(valid_assigned)

    li_elements = driver.find_elements(By.TAG_NAME, 'li')

    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in li_elements:
        if li.get_attribute('class') == 'active':
            active_a = li.find_element(By.TAG_NAME, 'a')
            break

    # Click on the active <li> element
    if active_a is not None:
        active_a.click()

    # Click on Lable dropdown
    lable.click()

    lable_srch = driver.find_element(By.XPATH,
                                     '//*[@id="save-task-data-form"]/div/div[1]/div[10]/div/div/div[1]/div/div[1]/input')

    # Search for valid option
    lable_srch.send_keys(valid_lable)

    li_elements = driver.find_elements(By.TAG_NAME, 'li')

    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in li_elements:
        if li.get_attribute('class') == 'active':
            active_a = li.find_element(By.TAG_NAME, 'a')
            break

    # Click on the active <li> element
    if active_a is not None:
        active_a.click()

    # Click on Status dropdown
    status.click()

    status_srch = driver.find_element(By.XPATH,
                                      '//*[@id="save-task-data-form"]/div/div[1]/div[11]/div/div/div/div[1]/input')

    # Search for valid option
    status_srch.send_keys(valid_status)

    li_elements = driver.find_elements(By.TAG_NAME, 'li')

    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in li_elements:
        if li.get_attribute('class') == 'active':
            active_a = li.find_element(By.TAG_NAME, 'a')
            break

    # Click on the active <li> element
    if active_a is not None:
        active_a.click()

    # Click on Description textarea
    description.clear()
    description.send_keys(valid_description)

    # Select option from Milestone Dropdown
    milestone.click()
    sel = driver.find_element(By.XPATH, '//*[@id="priority"]')
    sel.select_by_visible_text("Test")

    # Select option from Priority Dropdown
    priority.click()
    sel = driver.find_element(By.XPATH, '//*[@id="milestone_id"]')
    sel.select_by_visible_text("Low")

    # Save the Add task form
    save.click()
    time.sleep(8)


@pytest.mark.order(23)
def Test_Search_in_Table(driver):
    # find the saved lead in table and click on edit button
    row1 = driver.find_element(By.XPATH, '//table//tbody//tr[1]')
    cell1 = row1.find_element(By.XPATH, './/td[2]')
    var_id = cell1.text

    driver.find_element(By.XPATH, f'//*[@id="dropdownMenuLink-%s"]' % var_id).click()
    driver.find_element(By.XPATH, f'//*[@id="row-%s"]/td[10]/div/div/div/a[2]' % var_id).click()
    print("The task searched successfully in the table")
    time.sleep(10)


@pytest.mark.order(24)
def Test_Edit_and_Save(driver):

# Edit status of project

    status = driver.find_element(By.XPATH, '//*[@id="save-task-data-form"]/div/div[1]/div[11]/div/div/button')
    status.click()

    status_srch = driver.find_element(By.XPATH,
                                      '//*[@id="save-task-data-form"]/div/div[1]/div[11]/div/div/div/div[1]/input')
    # Search for valid option
    status_srch.send_keys("In-Progress")

    li_elements = driver.find_elements(By.TAG_NAME, 'li')

    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in li_elements:
        if li.get_attribute('class') == 'active':
            active_a = li.find_element(By.TAG_NAME, 'a')
            break

    # Click on the active <li> element
    if active_a is not None:
        active_a.click()

    # Edit sprint of project
    sprint = driver.find_element(By.XPATH, '//*[@id="save-task-data-form"]/div/div[1]/div[7]/div/div[1]/button')
    sprint.click()

    status_srch = driver.find_element(By.XPATH,
                                      '//*[@id="save-task-data-form"]/div/div[1]/div[7]/div/div[1]/div/div[1]/input')
    # Search for valid option
    status_srch.send_keys("sprint 1")

    li_elements = driver.find_elements(By.TAG_NAME, 'li')

    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in li_elements:
        if li.get_attribute('class') == 'active':
            active_a = li.find_element(By.TAG_NAME, 'a')
            break

    # Click on the active <li> element
    if active_a is not None:
        active_a.click()

    # Save the Edit form
    save = driver.find_element(By.XPATH, '//*[@id="save-task-form"]')
    save.click()
    time.sleep(10)

    add_project = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a')
    if add_project.is_enabled():
        print("The Edit form saved successfully.")

    # Close the web driver
    time.sleep(5)
    # driver.close()
