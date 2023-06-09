import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time

# create a logger instance
logger = logging.getLogger(__name__)

# Global variables used for different methods POC-QA-Automation
valid_email = "saurabhdhariwal.com@gmail.com"
valid_pass = "addweb123"

# Global variables used for different methods POC-QA-Automation
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
#     time.sleep(7)


@pytest.fixture(name="nvar")
def test_New_Var(driver):
    project = driver.find_element(By.XPATH,
                                  '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[1]/div/div/button')
    task = driver.find_element(By.XPATH,
                               '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[2]/div/div/button')
    employee = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[3]/div/div/button')
    date = driver.find_element(By.XPATH, '//*[@id="start_date"]')
    hr = driver.find_element(By.XPATH,
                             '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[5]/div/div/button')
    min = driver.find_element(By.XPATH,
                              '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[6]/div/div/button')
    memo = driver.find_element(By.XPATH, '//*[@id="memo"]')
    save = driver.find_element(By.XPATH, '//*[@id="save-timelog-form"]')
    cancel = driver.find_element(By.XPATH, '//*[@id="right-modal-content"]/div/div/div/div/a')
    add_more = driver.find_element(By.XPATH, '//*[@id="add-more-form"]')
    return project, task, employee, date, hr, min, memo, save, cancel, add_more


@pytest.mark.order(29)
def test_Click_on_Timelog_page(driver, selenium):
    # driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/a').click()
    # driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/div/a[4]').click()

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


@pytest.mark.order(30)
def test_Log_time_Button(driver):
    log_time = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a')
    assert log_time.is_enabled()
    print("The Log Time button is Enabled.")
    logger.info("The Log Time button is Enabled.")
    log_time.click()
    time.sleep(7)


@pytest.mark.order(31)
def test_Validate_Components(driver, nvar):
    project, task, employee, date, hr, min, memo, save, cancel, add_more = nvar

    assert project.is_enabled()
    print("The project dropdown is Enabled.")
    logger.info("The project dropdown is Enabled.")

    assert task.is_enabled()
    print("The task dropdown is Enabled.")
    logger.info("The task dropdown is Enabled.")

    assert employee.is_enabled()
    print("The employee dropdown is Enabled.")
    logger.info("The employee dropdown is Enabled.")

    assert date.is_enabled()
    print("The date picker is Enabled.")
    logger.info("The date picker is Enabled.")

    assert hr.is_enabled()
    print("The hour dropdown is Enabled.")
    logger.info("The hour dropdown is Enabled.")

    assert min.is_enabled()
    print("The minutes dropdown is Enabled.")
    logger.info("The minutes dropdown is Enabled.")

    assert memo.is_enabled()
    print("The memo textarea is Enabled.")
    logger.info("The memo textarea is Enabled.")

    assert save.is_enabled()
    print("The save button is Enabled.")
    logger.info("The save button is Enabled.")

    assert cancel.is_enabled()
    print("The cancel button is Enabled.")
    logger.info("The cancel button is Enabled.")

    assert add_more.is_enabled()
    print("The Add more button is Enabled.")
    logger.info("The Add more is Enabled.")


@pytest.mark.order(32)
def test_with_Blank_Value(driver, nvar):
    project, task, employee, date, hr, min, memo, save, cancel, add_more = nvar

    save.click()
    time.sleep(4)

    project_msg = driver.find_element(By.XPATH,
                                      '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[1]/div/div[2]')
    task_msg = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[2]/div/div[2]')
    employee_msg = driver.find_element(By.XPATH,
                                       '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[3]/div/div[2]')
    endtime_msg = driver.find_element(By.XPATH,
                                      '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[4]/div/div/div')
    memo_msg = driver.find_element(By.XPATH, '//*[@id="save-timelog-data-form"]/div/div[2]/div[2]/div/div')

    if project_msg.text == "Please select Project":
        print('"Please select Project." Message displayed successfully.')
        logger.info('"Please select Project." Message displayed successfully.')

    if task_msg.text == "Please select Task":
        print('"Please select Task." Message displayed successfully.')
        logger.info('"Please select Task." Message displayed successfully.')

    if employee_msg.text == "Please select user":
        print('"Please select user" Message displayed successfully.')
        logger.info('"Please select user" Message displayed successfully.')

    if endtime_msg.text == "Please enter end time ":
        print('"Please enter end time " Message displayed successfully.')
        logger.info('"Please enter end time " Message displayed successfully.')

    if memo_msg.text == "Please enter Memo":
        print('"Please enter Memo" Message displayed successfully.')
        logger.info('"Please enter Memo" Message displayed successfully.')


@pytest.mark.order(33)
def test_with_Invalid_value(driver, nvar):
    project, task, employee, date, hr, min, memo, save, cancel, add_more = nvar

    # Click on project dropdown
    project.click()
    project_srch = driver.find_element(By.XPATH,
                                       '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/input')

    # Search for valid option
    project_srch.send_keys(invalid_project)

    li_elements = driver.find_elements(By.TAG_NAME, 'li')

    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in li_elements:
        if li.get_attribute('class') == 'no-results':
            print('"No result found" message displayed successfully for invalid search in Project dropdown')
            break

    # Click on Task dropdown
    try:
        task.click()

    except StaleElementReferenceException:
        task = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[2]/div/div/button')
        task.click()

    task_srch = driver.find_element(By.XPATH,
                                    '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[1]/input')

    # Search for valid option
    task_srch.send_keys(valid_task)

    li_elements = driver.find_elements(By.TAG_NAME, 'li')

    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in li_elements:
        if li.get_attribute('class') == 'no-results':
            print('"No result found" message displayed successfully for invalid search in Task dropdown')
            break

    # Click on Employee dropdown
    try:
        employee.click()

    except StaleElementReferenceException:
        employee = driver.find_element(By.XPATH,
                                       '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[3]/div/div/button')
        employee.click()

    emp_srch = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div[1]/input')

    # Search for valid option
    emp_srch.send_keys(valid_employee)

    li_elements = driver.find_elements(By.TAG_NAME, 'li')

    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in li_elements:
        if li.get_attribute('class') == 'no-results':
            print('"No result found" message displayed successfully for invalid search in Employee dropdown')
            break

    # Click on the active <li> element
    if active_a is not None:
        active_a.click()

    # Click on Date input
    try:
        date.click()

    except StaleElementReferenceException:
        date = driver.find_element(By.XPATH, '//*[@id="start_date"]')

    # Search for valid option
    date.clear()
    date.send_keys(invalid_date)

    # Click on Minutes dropdown

    min = driver.find_element(By.XPATH,
                              '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[6]/div/div/button')
    min.click()

    min_srch = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[6]/div/div/div/div[1]/input')

    # Search for valid option
    min_srch.send_keys(invalid_min)

    li_elements = driver.find_elements(By.TAG_NAME, 'li')

    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in li_elements:
        if li.get_attribute('class') == 'no-results':
            print('"No result found" message displayed successfully for invalid search in Minutes Dropdown')
            break

    # Click on the active <li> element
    if active_a is not None:
        active_a.click()

    # Click on Hours dropdown

    hr = driver.find_element(By.XPATH,
                             '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[5]/div/div/button')
    hr.click()

    hr_srch = driver.find_element(By.XPATH,
                                  '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[5]/div/div/div/div[1]/input')

    # Search for valid option
    hr_srch.send_keys(invalid_hour)

    li_elements = driver.find_elements(By.TAG_NAME, 'li')

    # Iterate through the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in li_elements:
        if li.get_attribute('class') == 'no-results':
            print('"No result found" message displayed successfully for invalid search in Hours dropdown')
            break

    # Click on the active <li> element
    if active_a is not None:
        active_a.click()

    # Click on Memo input

    memo = driver.find_element(By.XPATH, '//*[@id="memo"]')

    # Search for valid option
    memo.clear()
    memo.send_keys(invalid_memo)

    # save.click()

    # Close the web driver
    # time.sleep(3)
    # driver.close()


@pytest.mark.order(34)
def test_with_Invalid_date_Value(driver, nvar):
    project, task, employee, date, hr, min, memo, save, cancel, add_more = nvar

    # Click on project dropdown
    project.click()
    project_srch = driver.find_element(By.XPATH,
                                       '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/input')

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

    # Click on Task dropdown
    try:
        task.click()

    except StaleElementReferenceException:
        task = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[2]/div/div/button')
        task.click()

    task_srch = driver.find_element(By.XPATH,
                                    '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[1]/input')

    # Search for valid option
    task_srch.send_keys(valid_task)

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

    # Click on Employee dropdown
    try:
        employee.click()

    except StaleElementReferenceException:
        employee = driver.find_element(By.XPATH,
                                       '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[3]/div/div/button')
        employee.click()

    emp_srch = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div[1]/input')

    # Search for valid option
    emp_srch.send_keys(valid_employee)

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

    # Click on Minutes dropdown

    min = driver.find_element(By.XPATH,
                              '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[6]/div/div/button')
    min.click()

    min_srch = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[6]/div/div/div/div[1]/input')

    # Search for valid option
    min_srch.send_keys(valid_min)

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

    # Click on Hours dropdown

    hr = driver.find_element(By.XPATH,
                             '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[5]/div/div/button')
    hr.click()

    hr_srch = driver.find_element(By.XPATH,
                                  '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[5]/div/div/div/div[1]/input')

    # Search for valid option
    hr_srch.send_keys(valid_hour)

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

    # Click on Memo input

    memo = driver.find_element(By.XPATH, '//*[@id="memo"]')

    # Search for valid option
    memo.clear()
    memo.send_keys(valid_memo)

    # Click on Date input
    try:
        date.click()

    except StaleElementReferenceException:
        date = driver.find_element(By.XPATH, '//*[@id="start_date"]')

    # Search for valid option
    date.clear()
    date.send_keys(invalid_date)
    save.click()

    time.sleep(2)

    date_err = driver.find_element(By.XPATH, '//*[@id="body"]/div[8]')
    if date_err.text == "A two digit day could not be found Data missing":
        print('"A two digit day could not be found Data missing" Message displayed successfully')

    # Close the web driver
    time.sleep(3)


@pytest.mark.order(35)
def test_with_Valid_Value(driver, nvar):
    project, task, employee, date, hr, min, memo, save, cancel, add_more = nvar

    # Click on project dropdown
    project.click()
    project_srch = driver.find_element(By.XPATH,
                                       '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/input')

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

    # Click on Task dropdown
    try:
        task.click()

    except StaleElementReferenceException:
        task = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[2]/div/div/button')
        task.click()

    task_srch = driver.find_element(By.XPATH,
                                    '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[1]/input')

    # Search for valid option
    task_srch.send_keys(valid_task)

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

    # Click on Employee dropdown
    try:
        employee.click()

    except StaleElementReferenceException:
        employee = driver.find_element(By.XPATH,
                                       '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[3]/div/div/button')
        employee.click()

    emp_srch = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div[1]/input')

    # Search for valid option
    emp_srch.send_keys(valid_employee)

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

    # Click on Date input
    try:
        date.click()

    except StaleElementReferenceException:
        date = driver.find_element(By.XPATH, '//*[@id="start_date"]')

    # Search for valid option
    date.clear()
    date.send_keys(valid_date)
    s_date = driver.find_element(By.XPATH, '//*[@id="start_time"]')
    s_date.click()

    # Click on Minutes dropdown

    min = driver.find_element(By.XPATH,
                              '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[6]/div/div/button')
    min.click()

    min_srch = driver.find_element(By.XPATH,
                                   '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[6]/div/div/div/div[1]/input')

    # Search for valid option
    min_srch.send_keys(valid_min)

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

    # Click on Hours dropdown

    hr = driver.find_element(By.XPATH,
                             '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[5]/div/div/button')
    hr.click()

    hr_srch = driver.find_element(By.XPATH,
                                  '//*[@id="save-timelog-data-form"]/div/div[2]/div[1]/div[2]/div[5]/div/div/div/div[1]/input')

    # Search for valid option
    hr_srch.send_keys(valid_hour)

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

    # Click on Memo input

    memo = driver.find_element(By.XPATH, '//*[@id="memo"]')

    # Search for valid option
    memo.clear()
    memo.send_keys(valid_memo)

    # Click on Memo input

    save.click()
    time.sleep(6)
    log_time = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a')
    if log_time.is_enabled():
        print("The form with valid data saved successfully.")


@pytest.mark.order(36)
def test_Search_in_Table(driver):
    # find the saved lead in table and click on edit button
    row1 = driver.find_element(By.XPATH, '//table//tbody//tr[1]')
    cell1 = row1.find_element(By.XPATH, './/td[2]')
    var_id = cell1.text

    driver.find_element(By.XPATH, f'//*[@id="dropdownMenuLink-%s"]' % var_id).click()
    driver.find_element(By.XPATH, f'//*[@id="row-%s"]/td[8]/div/div/div/a[2]' % var_id).click()
    print("The Log searched successfully in the table")
    time.sleep(2)


@pytest.mark.order(37)
def test_Edit_and_Save(driver):
    memo = driver.find_element(By.XPATH, '//*[@id="memo"]')

    # Search for valid option
    memo.clear()
    memo.send_keys("Testing Edit form by changing the value of memo textarea ...")

    save = driver.find_element(By.XPATH, '//*[@id="save-timelog-form"]')
    save.click()
    time.sleep(6)

    log_time = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a')
    if log_time.is_enabled():
        print("The Edit form saved successfully.")

    # Close the web driver
    time.sleep(3)
    # driver.close()
