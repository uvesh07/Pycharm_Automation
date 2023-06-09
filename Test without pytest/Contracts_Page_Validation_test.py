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

valid_subject = "Testing"
invalid_subject = "Nothing"

valid_description = "Testing"
invalid_description = "Nothing"

valid_start_date = "17-05-2023"
invalid_start_date = "32-05-2023"

valid_enddate = "18-05-2023"
invalid_enddate = "32-05-2023"

valid_type = "Non-Billable"
invalid_type = "Nothing"

valid_name = "Non-Billable"
invalid_name = "Nothing"

valid_value = "Team-circuit-breakers"
invalid_value = "Nothing"

valid_currency = "Nick"
invalid_currency = "Nothing"

valid_client = "Testing summary..."
invalid_client = "Nothing"

valid_client_name = "Testing summary..."
invalid_client_name = "Nothing"

valid_client_email = "Testing summary..."
invalid_client_email = "Nothing"

valid_client_pass = "Testing summary..."
invalid_client_pass = "Nothing"


def test_enter_valid_creadential(driver):
    email = driver.find_element(By.XPATH, '//*[@id="email"]')
    passwrd = driver.find_element(By.XPATH, '//*[@id="password"]')
    login = driver.find_element(By.XPATH, '//*[@id="submit-login"]')
    global valid_email
    global valid_pass

    email.send_keys(valid_email)
    passwrd.send_keys(valid_pass)
    login.click()

    time.sleep(3)


@pytest.fixture(name="nvar")
def test_new_var(driver):
    subject = driver.find_element(By.XPATH, '//*[@id="subject"]')
    description = driver.find_element(By.XPATH, '//*[@id="description"]/div[1]')
    start_date = driver.find_element(By.XPATH, '//*[@id="start_date"]')
    end_date = driver.find_element(By.XPATH, '//*[@id="end_date"]')
    type_dropdown = driver.find_element(By.XPATH, '//*[@id="save-contract-data-form"]/div/div[1]/div[5]/div/div[1]/button')
    type_add_btn = driver.find_element(By.XPATH, '//*[@id="createContractType"]')
    contract_value = driver.find_element(By.XPATH, '//*[@id="save-contract-data-form"]/div/div[1]/div[6]/div/input')
    currency = driver.find_element(By.XPATH, '//*[@id="save-contract-data-form"]/div/div[1]/div[7]/div/div/div/button')
    client_dropdown = driver.find_element(By.XPATH, '//*[@id="save-contract-data-form"]/div/div[2]/div[1]/div/div[1]/button')
    client_add_btn = driver.find_element(By.XPATH, '//*[@id="add-client"]')
    save = driver.find_element(By.XPATH, '//*[@id="save-contract-form"]')
    cancel = driver.find_element(By.XPATH, '//*[@id="save-contract-data-form"]/div/div[3]/a')

    return


def test_click_on_projects(driver, selenium):
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/a').click()
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/div/a[2]').click()
    time.sleep(3)
    if driver.title == "Projects":
        print("Successfully reached at Projects page")
        logger.info("Successfully reached at Projects page")


def test_seachbox_on_projects_page(driver):
    search_box = driver.find_element(By.XPATH, '//*[@id="search-text-field"]')
    search_box.send_keys("Testing123")
    time.sleep(8)

    row1 = driver.find_element(By.XPATH, '//table//tbody//tr[1]')
    cell1 = row1.find_element(By.XPATH, './/td[3]')

    if cell1.text == "Testing123":
        print("The search functionality is working properly.")


def test_add_project_button(driver):
    add_project = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a[1]')
    assert add_project.is_enabled()
    print("The Add project button is Enabled.")
    logger.info("The Add project button is Enabled.")
    add_project.click()
    time.sleep(5)


def test_validate_components(driver, nvar):
    project, start_date, deadline, deadline_check, category, department, client, summary, notes, public_project, \
        member, channel, topic, other_topics, add_file, currency, budget, hr, manual, client_manage, save, cancel = nvar

    assert project.is_enabled()
    print("The project text is Enabled.")
    logger.info("The project text is Enabled.")

    assert start_date.is_enabled()
    print("The start date input is Enabled.")
    logger.info("The start date input is Enabled.")

    assert deadline.is_enabled()
    print("The deadline input is Enabled.")
    logger.info("The deadline input is Enabled.")

    assert deadline_check.is_enabled()
    print("The deadline checkbox is Enabled.")
    logger.info("The deadline checkbox is Enabled.")

    assert category.is_enabled()
    print("The category dropdown is Enabled.")
    logger.info("The category dropdown is Enabled.")

    assert department.is_enabled()
    print("The department dropdown is Enabled.")
    logger.info("The department dropdown is Enabled.")

    assert client.is_enabled()
    print("The client dropdown is Enabled.")
    logger.info("The client dropdown is Enabled.")

    assert summary.is_enabled()
    print("The summary textarea is Enabled.")
    logger.info("The summary textarea is Enabled.")

    assert notes.is_enabled()
    print("The notes textarea is Enabled.")
    logger.info("The notes textarea is Enabled.")

    assert public_project.is_enabled()
    print("The Public project checkbox is Enabled.")
    logger.info("The Public project checkbox is Enabled.")

    assert member.is_enabled()
    print("The member dropdown is Enabled.")
    logger.info("The member dropdown is Enabled.")

    assert channel.is_enabled()
    print("The channel dropdown is Enabled.")
    logger.info("The channel dropdown is Enabled.")

    assert topic.is_enabled()
    print("The topic input is Enabled.")
    logger.info("The topic input is Enabled.")

    assert other_topics.is_enabled()
    print("The Other Details button is Enabled.")
    logger.info("The Other Details button is Enabled.")
    other_topics.click()
    time.sleep(2)

    assert add_file.is_enabled()
    print("The Add file input is Enabled.")
    logger.info("The Add file input is Enabled.")

    assert currency.is_enabled()
    print("The currency dropdown is Enabled.")
    logger.info("The currency dropdown is Enabled.")

    assert budget.is_enabled()
    print("The budget input is Enabled.")
    logger.info("The budget input is Enabled.")

    assert hr.is_enabled()
    print("The Hours input is Enabled.")
    logger.info("The Hours input is Enabled.")

    assert manual.is_enabled()
    print("The Allow manual time logs checkbox is Enabled.")
    logger.info("The Allow manual time logs checkbox is Enabled.")

    assert client_manage.is_enabled()
    print("The Client can manage tasks of this project checkbox is Enabled.")
    logger.info("The Client can manage tasks of this project checkbox is Enabled.")

    assert save.is_enabled()
    print("The save button is Enabled.")
    logger.info("The save button is Enabled.")

    assert cancel.is_enabled()
    print("The cancel button is Enabled.")
    logger.info("The cancel button is Enabled.")


def test_with_blank_value(driver, nvar):
    project, start_date, deadline, deadline_check, category, department, client, summary, notes, public_project, \
        member, channel, topic, other_topics, add_file, currency, budget, hr, manual, client_manage, save, cancel = nvar

    save.click()
    time.sleep(2)

    project_msg = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[1]/div/div')
    start_date_msg = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[2]/div/div[2]')
    deadline_msg = driver.find_element(By.XPATH, '//*[@id="deadlineBox"]/div/div[2]')
    member_msg = driver.find_element(By.XPATH, '//*[@id="add_members"]/div/div/div[3]')

    if project_msg.text == "The project name field is required.":
        print('"The project name field is required." Message displayed successfully.')
        logger.info('"The project name field is required." Message displayed successfully.')

    if start_date_msg.text == "The start date field is required.":
        print('"The start date field is required." Message displayed successfully.')
        logger.info('"The start date field is required." Message displayed successfully.')

    if deadline_msg.text == "The deadline field is required.":
        print('"The deadline field is required." Message displayed successfully.')
        logger.info('"The deadline field is required." Message displayed successfully.')

    if member_msg.text == "Select at least 1 member":
        print('"Select at least 1 member" Message displayed successfully.')
        logger.info('"Select at least 1 member" Message displayed successfully.')


def test_with_invalid_value(driver, nvar):
    project, start_date, deadline, deadline_check, category, department, client, summary, notes, public_project, \
        member, channel, topic, other_topics, add_file, currency, budget, hr, manual, client_manage, save, cancel = nvar

# send keys in project textbox
    project.clear()
    project.send_keys(invalid_project)


# Click on Start Date input
    start_date.click()

    # send keys to start date
    start_date.clear()
    start_date.send_keys(invalid_start_date)


# Click on Deadline input
    deadline.click()

    # send keys to deadline
    deadline.clear()
    deadline.send_keys(invalid_deadline)

# Click on Category dropdown
    category.click()

    category_srch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[5]/div/div[1]/div/div[1]/input')

    # Search for valid option
    category_srch.send_keys(invalid_category)

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

# Click on Department dropdown
    department.click()

    department_srch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[6]/div/div[1]/div/div[1]/input')

    # Search for valid option
    department_srch.send_keys(invalid_depatment)

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

# Click on Client dropdown
    client.click()

    client_srch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[7]/div/div[1]/div/div[1]/input')

    # Search for valid option
    client_srch.send_keys(invalid_client)

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

# Click on Summary dropdown
    summary.clear()
    driver.find_element(By.XPATH,
                        '//*[@id="save-project-data-form"]/div/div[1]/div[8]/div/div[1]/span[2]/button[1]').click()
    summary.send_keys(invalid_summary)


# Click on Notes dropdown
    notes.clear()
    driver.find_element(By.XPATH,
                        '//*[@id="save-project-data-form"]/div/div[1]/div[9]/div/div[1]/span[2]/button[2]').click()
    notes.send_keys(invalid_note)

# Click on Member dropdown
    member.click()

    member_srch = driver.find_element(By.XPATH,
                                      '//*[@id="add_members"]/div/div/div[1]/div/div[1]/input')

    # Search for valid option
    member_srch.send_keys(invalid_member)

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

# Click on Channel dropdown
    channel.click()

    channel_srch = driver.find_element(By.XPATH,
                                      '//*[@id="save-project-data-form"]/div/div[1]/div[12]/div/div[1]/div/div[1]/input')

    # Search for valid option
    channel_srch.send_keys(invalid_channel)

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

# Click on Topic input
    topic.clear()
    topic.send_keys(invalid_topic)

# Click on Add files input
#     valid_addfile = "/home/addweb/Downloads/activity_D-transformed.jpeg"
#     invalid_addfile = "/home/addweb/Downloads///"
#     add_file.send_keys(invalid_addfile)

# Click on Currency dropdown
    currency.click()

    currency_srch = driver.find_element(By.XPATH,
                                       '//*[@id="other-project-details"]/div[2]/div/div/div/div[1]/input')

    # Search for valid option
    currency_srch.send_keys(invalid_currency)

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

# Click on Budget dropdown
    budget.clear()
    budget.send_keys(invalid_budget)


# Click on Hours input
    hr.clear()
    hr.send_keys(invalid_budget)


# Click on Hours input
    hr.clear()
    hr.send_keys(invalid_budget)


# Click on Manual timelog checkbox
    manual.click()

# Click save button
    save.click()
    time.sleep(2)

    start_date_msg = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[2]/div/div[2]')
    deadline_msg = driver.find_element(By.XPATH, '//*[@id="deadlineBox"]/div/div[2]')

    if start_date_msg.text == "The start date does not match the format d-m-Y.":
        print('"The start date does not match the format d-m-Y." Message displayed successfully.')
        logger.info('"The start date does not match the format d-m-Y." Message displayed successfully.')

    if deadline_msg.text == "The deadline does not match the format d-m-Y.":
        print('"The deadline does not match the format d-m-Y." Message displayed successfully.')
        logger.info('"The deadline does not match the format d-m-Y." Message displayed successfully.')


def test_with_invalid_startdate_and_deadline(driver, nvar):
    project, start_date, deadline, deadline_check, category, department, client, summary, notes, public_project, \
        member, channel, topic, other_topics, add_file, currency, budget, hr, manual, client_manage, save, cancel = nvar

# send keys in project textbox
    project.clear()
    project.send_keys(valid_project)


# Click on Start Date input
    start_date.click()

    # send keys to start date
    start_date.clear()
    start_date.send_keys("17-05-2023")


# Click on Deadline input
    deadline.click()

    # send keys to deadline
    deadline.clear()
    deadline.send_keys("16-05-2023")

# Click on Category dropdown
    category.click()

    category_srch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[5]/div/div[1]/div/div[1]/input')

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

# Click on Department dropdown
    department.click()

    department_srch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[6]/div/div[1]/div/div[1]/input')

    # Search for valid option
    department_srch.send_keys(valid_department)

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

# Click on Client dropdown
    client.click()

    client_srch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[7]/div/div[1]/div/div[1]/input')

    # Search for valid option
    client_srch.send_keys(valid_client)

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

# Click on Summary dropdown
    summary.clear()
    driver.find_element(By.XPATH,
                        '//*[@id="save-project-data-form"]/div/div[1]/div[8]/div/div[1]/span[2]/button[1]').click()
    summary.send_keys(valid_summary)


# Click on Notes dropdown
    notes.clear()
    driver.find_element(By.XPATH,
                        '//*[@id="save-project-data-form"]/div/div[1]/div[9]/div/div[1]/span[2]/button[2]').click()
    notes.send_keys(valid_note)

# Click on Member dropdown
    member.click()

    member_srch = driver.find_element(By.XPATH,
                                      '//*[@id="add_members"]/div/div/div[1]/div/div[1]/input')

    # Search for valid option
    member_srch.send_keys(valid_member)

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

# Click on Channel dropdown
    channel.click()

    channel_srch = driver.find_element(By.XPATH,
                                      '//*[@id="save-project-data-form"]/div/div[1]/div[12]/div/div[1]/div/div[1]/input')

    # Search for valid option
    channel_srch.send_keys(valid_channel)

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

# Click on Topic input
    topic.clear()
    topic.send_keys(valid_topic)

# Click on Add files input
#     valid_addfile = "/home/addweb/Downloads/activity_D-transformed.jpeg"
#     invalid_addfile = "/home/addweb/Downloads///"
#     add_file.send_keys(invalid_addfile)

# Click on Currency dropdown
    currency.click()

    currency_srch = driver.find_element(By.XPATH,
                                       '//*[@id="other-project-details"]/div[2]/div/div/div/div[1]/input')

    # Search for valid option
    currency_srch.send_keys(valid_currency)

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

# Click on Budget dropdown
    budget.clear()
    budget.send_keys(valid_budget)


# Click on Hours input
    hr.clear()
    hr.send_keys(valid_budget)


# Click on Hours input
    hr.clear()
    hr.send_keys(valid_budget)


# Click on Manual timelog checkbox
    manual.click()

# Click save button
    save.click()
    time.sleep(4)

    deadline_msg = driver.find_element(By.XPATH, '//*[@id="deadlineBox"]/div/div[2]')

    if deadline_msg.text == "The deadline must be a date after or equal to start date.":
        print('"The deadline must be a date after or equal to start date." Message displayed successfully.')
        logger.info('"The deadline must be a date after or equal to start date." Message displayed successfully.')


def test_with_valid_data_and_checkbox(driver, nvar):
    project, start_date, deadline, deadline_check, category, department, client, summary, notes, public_project, \
        member, channel, topic, other_topics, add_file, currency, budget, hr, manual, client_manage, save, cancel = nvar

# send keys in project textbox
    project.clear()
    project.send_keys(valid_project)


# Click on Start Date input
    start_date.click()

    # send keys to start date
    start_date.clear()
    start_date.send_keys("17-05-2023")

# Check Deadline checkbox
    deadline_check.click()

# Click on Deadline input
    try:
        deadline.click()

    except ElementNotInteractableException:
        print('When user check the "There is no project deadline" checkbox the Deadline element removed successfully')


# Click on Category dropdown
    category.click()

    category_srch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[5]/div/div[1]/div/div[1]/input')

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

# Click on Department dropdown
    department.click()

    department_srch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[6]/div/div[1]/div/div[1]/input')

    # Search for valid option
    department_srch.send_keys(valid_department)

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

# Click on Client dropdown
    client.click()

    client_srch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[7]/div/div[1]/div/div[1]/input')

    # Search for valid option
    client_srch.send_keys(valid_client)

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

# Click on Summary dropdown
    summary.clear()
    driver.find_element(By.XPATH,
                        '//*[@id="save-project-data-form"]/div/div[1]/div[8]/div/div[1]/span[2]/button[1]').click()
    summary.send_keys(valid_summary)


# Click on Notes dropdown
    notes.clear()
    driver.find_element(By.XPATH,
                        '//*[@id="save-project-data-form"]/div/div[1]/div[9]/div/div[1]/span[2]/button[2]').click()
    notes.send_keys(valid_note)

# Check the Public project checkbox
    public_project.click()

# Click on Member dropdown
    try:
        member.click()

    except ElementNotInteractableException:
        print('When user check the "Create Public Project" checkbox the Add project member element removed successfully')

# Click on Channel dropdown
    channel.click()

    channel_srch = driver.find_element(By.XPATH,
                                      '//*[@id="save-project-data-form"]/div/div[1]/div[12]/div/div[1]/div/div[1]/input')

    # Search for valid option
    channel_srch.send_keys(valid_channel)

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

# Click on Topic input
    topic.clear()
    topic.send_keys(valid_topic)

# Click on Add files input
#     valid_addfile = "/home/addweb/Downloads/activity_D-transformed.jpeg"
#     invalid_addfile = "/home/addweb/Downloads///"
#     add_file.send_keys(invalid_addfile)

# Click on Currency dropdown
    currency.click()

    currency_srch = driver.find_element(By.XPATH,
                                       '//*[@id="other-project-details"]/div[2]/div/div/div/div[1]/input')

    # Search for valid option
    currency_srch.send_keys(valid_currency)

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

# Click on Budget dropdown
    budget.clear()
    budget.send_keys(valid_budget)


# Click on Hours input
    hr.clear()
    hr.send_keys(valid_budget)


# Click on Hours input
    hr.clear()
    hr.send_keys(valid_budget)


# Click on Manual timelog checkbox
    manual.click()

# Check the Client can manage tasks of this project checkbox
    client_manage.click()
    task_notification = driver.find_element(By.XPATH, '//*[@id="client_task_notification"]')
    if task_notification.is_enabled():
        print('When user check the "The Client can manage tasks of this project" checkbox the "Send task notification '
              'to client?" checkbox is enabled.')

# Click save button
    save.click()
    time.sleep(4)

    add_project = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a[1]')
    if add_project.is_enabled():
        print("The Form with valid data saved successfully.")


def test_search_in_table(driver):
    # find the saved lead in table and click on edit button
    row1 = driver.find_element(By.XPATH, '//table//tbody//tr[1]')
    cell1 = row1.find_element(By.XPATH, './/td[2]')
    var_id = cell1.text

    driver.find_element(By.XPATH, f'//*[@id="dropdownMenuLink-%s"]' % var_id).click()
    driver.find_element(By.XPATH, f'//*[@id="row-%s"]/td[9]/div/div/div/a[2]' % var_id).click()
    print("The Project searched successfully in the table")
    time.sleep(4)


def test_edit_and_save(driver):

    project = driver.find_element(By.XPATH, '//*[@id="project_name"]')

    # Search for valid option
    project.clear()
    project.send_keys("Testing Edit form by changing the value of Project textbox ...")

    save = driver.find_element(By.XPATH, '//*[@id="save-project-form"]')
    save.click()
    time.sleep(4)

    add_project = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a[1]')
    if add_project.is_enabled():
        print("The Edit form saved successfully.")

    # Close the web driver
    time.sleep(3)
    driver.close()

