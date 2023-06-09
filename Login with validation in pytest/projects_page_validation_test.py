import pytest
import logging
from datetime import datetime, timedelta
from selenium.common import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# create a logger instance
logger = logging.getLogger(__name__)

# Global variables used for different methods POC-QA-Automation
valid_email = "saurabhdhariwal.com@gmail.com"
valid_pass = "addweb123"

valid_project = "Testing"
invalid_project = "Nothing"

valid_start_date = "17-05-2023"
invalid_start_date = "32-05-2023"

valid_deadline = "18-05-2023"
invalid_deadline = "32-05-2023"

valid_category = "Non-Billable"
invalid_category = "Nothing"

valid_department = "Team-circuit-breakers"
invalid_depatment = "Nothing"

valid_client = "Nick"
invalid_client = "Nothing"

valid_summary = "Testing summary..."
invalid_summary = "Nothing"

valid_note = "Testing Notes......"
invalid_note = "Nothing"

valid_member = "Pathan UveshMohammad"
invalid_member = "Nothing"

valid_channel = "QA_1"
invalid_channel = "Nothing"

valid_topic = "saurabhdhariwal.com@gmail.com"
invalid_topic = "Nothing"

valid_currency = "USD"
invalid_currency = "Nothing"

valid_budget = "1000"
invalid_budget = "Nothing"

valid_hr = "50"
invalid_hr = "Nothing"


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
#     time.sleep(3)


@pytest.fixture(name="nvar")
def test_new_Var(driver):
    project = driver.find_element(By.XPATH, '//*[@id="project_name"]')
    start_date = driver.find_element(By.XPATH, '//*[@id="start_date"]')
    deadline = driver.find_element(By.XPATH, '//*[@id="deadline"]')
    deadline_check = driver.find_element(By.XPATH, '//*[@id="without_deadline"]')
    category = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[5]/div/div[1]/button')
    department = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[6]/div/div[1]/button')
    client = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[7]/div/div[1]/button')
    summary = driver.find_element(By.XPATH, '//*[@id="project_summary"]/div[1]')
    notes = driver.find_element(By.XPATH, '//*[@id="notes"]/div[1]')
    public_project = driver.find_element(By.XPATH, '//*[@id="is_public"]')
    member = driver.find_element(By.XPATH, '//*[@id="add_members"]/div/div/div[1]/button')
    channel = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[12]/div/div[1]/button')
    topic = driver.find_element(By.XPATH, '//*[@id="channel_topic"]')
    other_topics = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/h4[2]/a')
    add_file = driver.find_element(By.XPATH, '//*[@id="file-upload-dropzone"]/input')
    currency = driver.find_element(By.XPATH, '//*[@id="other-project-details"]/div[2]/div/div/button')
    budget = driver.find_element(By.XPATH, '//*[@id="project_budget"]')
    hr = driver.find_element(By.XPATH, '//*[@id="hours_allocated"]')
    manual = driver.find_element(By.XPATH, '//*[@id="manual_timelog"]')
    client_manage = driver.find_element(By.XPATH, '//*[@id="client_view_task"]')
    save = driver.find_element(By.XPATH, '//*[@id="save-project-form"]')
    cancel = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[3]/a')

    return project, start_date, deadline, deadline_check, category, department, client, summary, notes, public_project, \
        member, channel, topic, other_topics, add_file, currency, budget, hr, manual, client_manage, save, cancel


@pytest.mark.order(11)
def test_Click_on_Projects(driver, selenium):
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
                            if a.text == "Projects":
                                a.click()

                    except NoSuchElementException:
                        print("You do not have access to Projects Page.")

                else:
                    try:
                        # find <a> tag in work dropdown
                        a_links = li.find_elements(By.TAG_NAME, 'a')

                        for a in a_links:
                            if a.text == "Projects":
                                a.click()

                    except NoSuchElementException:
                        print("You do not have access to Projects Page.")

        except StaleElementReferenceException:
            continue

    time.sleep(4)
    if driver.title == "Projects":
        print("Successfully reached at Projects page")


@pytest.mark.order(12)
def test_Seachbox_on_Projects_page(driver):
    search_box = driver.find_element(By.XPATH, '//*[@id="search-text-field"]')
    search_box.send_keys("Testing123")
    time.sleep(8)

    try:
        row1 = driver.find_element(By.XPATH, '//table//tbody//tr[1]')
        cell1 = row1.find_element(By.XPATH, './/td[3]')
        if cell1.text == "Testing123":
            print("The search functionality is working properly.")
    except NoSuchElementException:
        print("The value is not found in the table")


@pytest.mark.order(13)
def test_Add_project_Button(driver):
    add_project = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a[1]')
    assert add_project.is_enabled()
    print("The Add project button is Enabled.")
    logger.info("The Add project button is Enabled.")
    add_project.click()
    time.sleep(8)


@pytest.mark.order(14)
def test_Validate_Components(driver, nvar):
    project, start_date, deadline, deadline_check, category, department, client, summary, notes, public_project, \
        member, channel, topic, other_topics, add_file, currency, budget, hr, manual, client_manage, save, cancel = nvar

    assert project.is_enabled()
    print("The project textbox is Enabled.")
    logger.info("The project textbox is Enabled.")

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


@pytest.mark.order(15)
def test_with_Blank_Value(driver, nvar):
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


@pytest.mark.order(16)
def test_with_Invalid_Value(driver, nvar):
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
    hr.send_keys(invalid_hr)


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


@pytest.mark.order(17)
def test_with_Invalid_Startdate_and_Deadline(driver, nvar):
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
    hr.send_keys(valid_hr)

# Click on Manual timelog checkbox
    manual.click()

# Click save button
    save.click()
    time.sleep(4)

    deadline_msg = driver.find_element(By.XPATH, '//*[@id="deadlineBox"]/div/div[2]')

    if deadline_msg.text == "The deadline must be a date after or equal to start date.":
        print('"The deadline must be a date after or equal to start date." Message displayed successfully.')
        logger.info('"The deadline must be a date after or equal to start date." Message displayed successfully.')


@pytest.mark.order(18)
def test_with_Valid_Data_and_Checkbox(driver, nvar):
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
#     public_project.click()

# Click on Member dropdown
#     try:
#         member.click()
#
# except ElementNotInteractableException: print('When user check the "Create Public Project" checkbox the Add project
    # member element removed successfully')

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

    # driver.switch_to_frame(0)

# Click on Add files input
    valid_addfile = "/home/addweb/PycharmProjects/Ticktalk leads automation/Images/bg color.jpeg"

    # Find the dropzone element
    dropzone = driver.find_element(By.XPATH, '//*[@id="file-upload-dropzone"]')

    # Create an ActionChains object to perform actions on the dropzone
    actions = ActionChains(driver)

    # Click on the dropzone to activate the file input
    actions.move_to_element(dropzone).click().perform()

    # Locate the file input element within the dropzone
    file_input = dropzone.find_element(By.XPATH, '//*[@id="file-upload-dropzone"]/input')

    driver.execute_script("arguments[0].type = 'file';", file_input)
    driver.execute_script("arguments[0].style.display = 'block';", file_input)
    # Set the file path in the file input
    file_input.send_keys(valid_addfile)

    time.sleep(20)

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
    hr.send_keys(valid_hr)


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

    time.sleep(8)


@pytest.mark.order(19)
def test_Search_in_Table(driver):
    # find the saved lead in table and click on edit button
    row1 = driver.find_element(By.XPATH, '//table//tbody//tr[1]')
    cell1 = row1.find_element(By.XPATH, './/td[2]')
    var_id = cell1.text

    driver.find_element(By.XPATH, f'//*[@id="dropdownMenuLink-%s"]' % var_id).click()
    driver.find_element(By.XPATH, f'//*[@id="row-%s"]/td[9]/div/div/div/a[2]' % var_id).click()
    print("The Project searched successfully in the table")
    time.sleep(10)


@pytest.mark.order(20)
def test_Edit_and_Save(driver):

    project = driver.find_element(By.XPATH, '//*[@id="project_name"]')

    # Edit project name
    project.clear()
    project.send_keys("Project Testing")

    # Edit status of project
    status = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[10]/div/div/button')
    status.click()

    status_srch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[10]/div/div/div/div[1]/input')
    # Search for valid option
    status_srch.send_keys("In Progress")

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
    save = driver.find_element(By.XPATH, '//*[@id="save-project-form"]')
    save.click()
    time.sleep(10)

    add_project = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a[1]')
    if add_project.is_enabled():
        print("The Edit form saved successfully.")

    # Close the web driver
    time.sleep(5)
    # driver.close()


@pytest.mark.order(21)
def test_add_Sprint(driver):
    # find the saved lead in table and click on edit button
    row1 = driver.find_element(By.XPATH, '//table//tbody//tr[1]')
    cell1 = row1.find_element(By.XPATH, './/td[2]')
    var_id = cell1.text

    driver.find_element(By.XPATH, f'//*[@id="dropdownMenuLink-%s"]' % var_id).click()
    driver.find_element(By.XPATH, f'//*[@id="row-%s"]/td[3]/div/div/h5/a' % var_id).click()

    time.sleep(7)

    sprint = driver.find_element(By.XPATH, '//*[@id="mob-client-detail"]/nav/ul/li[6]/a')
    sprint.click()

    time.sleep(7)

    add_sprint = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a')
    add_sprint.click()

    time.sleep(7)

    title = driver.find_element(By.XPATH, '//*[@id="heading"]')
    title.send_keys("sprint 1")

    # Get today's date
    today = datetime.now().date()

    # Format the date into "d-m-y" format
    formatted_date = today.strftime("%d-%m-%Y")

    # Calculate the date 5 days from today
    five_days_after = formatted_date

    end_date = driver.find_element(By.XPATH, '//*[@id="due_date"]')
    end_date.clear()
    end_date.send_keys(five_days_after)

    # Save the sprint
    save = driver.find_element(By.XPATH, '//*[@id="save-task-form"]')
    save.click()

    time.sleep(10)

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
                            if a.text == "Projects":
                                a.click()

                    except NoSuchElementException:
                        print("You do not have access to Projects Page.")

                else:
                    try:
                        # find <a> tag in work dropdown
                        a_links = li.find_elements(By.TAG_NAME, 'a')

                        for a in a_links:
                            if a.text == "Projects":
                                a.click()

                    except NoSuchElementException:
                        print("You do not have access to Projects Page.")

        except StaleElementReferenceException:
            continue

    time.sleep(5)