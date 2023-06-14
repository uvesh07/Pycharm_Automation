import pytest
from datetime import datetime, timedelta
from selenium.common import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Global variables used for different methods POC-QA-Automation
ValidEmail = "saurabhdhariwal.com@gmail.com"
ValidPass = "addweb123"

ValidProject = "Testing"
InvalidProject = "Nothing"

ValidStartDate = "17-05-2023"
InvalidStartDate = "32-05-2023"

ValidDeadline = "18-05-2023"
InvalidDeadline = "32-05-2023"

ValidCategory = "Non-Billable"
InvalidCategory = "Nothing"

ValidDepartment = "Team-circuit-breakers"
InvalidDepartment = "Nothing"

ValidClient = "Nick"
InvalidClient = "Nothing"

ValidSummary = "Testing summary..."
InvalidSummary = "Nothing"

ValidNote = "Testing Notes......"
inValidNote = "Nothing"

ValidMember = "Pathan UveshMohammad"
InvalidMember = "Nothing"

ValidChannel = "QA_1"
InvalidChannel = "Nothing"

ValidTopic = "saurabhdhariwal.com@gmail.com"
InvalidTopic = "Nothing"

ValidCurrency = "USD"
InvalidCurrency = "Nothing"

ValidBudget = "1000"
InvalidBudget = "Nothing"

ValidHr = "50"
InvalidHr = "Nothing"

wait = ""


@pytest.fixture(name="nvar")
def test_NewVar(driver):
    Project = driver.find_element(By.XPATH, '//*[@id="project_name"]')
    StartDate = driver.find_element(By.XPATH, '//*[@id="start_date"]')
    Deadline = driver.find_element(By.XPATH, '//*[@id="deadline"]')
    DeadlineCheck = driver.find_element(By.XPATH, '//*[@id="without_deadline"]')
    Category = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[5]/div/div[1]/button')
    Department = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[6]/div/div[1]/button')
    Client = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[7]/div/div[1]/button')
    Summary = driver.find_element(By.XPATH, '//*[@id="project_summary"]/div[1]')
    Notes = driver.find_element(By.XPATH, '//*[@id="notes"]/div[1]')
    PublicProject = driver.find_element(By.XPATH, '//*[@id="is_public"]')
    Member = driver.find_element(By.XPATH, '//*[@id="add_members"]/div/div/div[1]/button')
    Channel = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[12]/div/div[1]/button')
    Topic = driver.find_element(By.XPATH, '//*[@id="channel_topic"]')
    OtherTopics = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/h4[2]/a')
    AddFile = driver.find_element(By.XPATH, '//*[@id="file-upload-dropzone"]/input')
    Currency = driver.find_element(By.XPATH, '//*[@id="other-project-details"]/div[2]/div/div/button')
    Budget = driver.find_element(By.XPATH, '//*[@id="project_budget"]')
    Hr = driver.find_element(By.XPATH, '//*[@id="hours_allocated"]')
    Manual = driver.find_element(By.XPATH, '//*[@id="manual_timelog"]')
    ClientManage = driver.find_element(By.XPATH, '//*[@id="client_view_task"]')
    Save = driver.find_element(By.XPATH, '//*[@id="save-project-form"]')
    Cancel = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[3]/a')

    return Project, StartDate, Deadline, DeadlineCheck, Category, Department, Client, Summary, Notes, PublicProject, \
        Member, Channel, Topic, OtherTopics, AddFile, Currency, Budget, Hr, Manual, ClientManage, Save, Cancel


@pytest.mark.order(11)
def test_ClickOnProjects(driver, selenium):
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
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="search-text-field"]')))
    if driver.title == "Projects":
        print("Successfully reached at Projects page")


@pytest.mark.order(13)
def test_AddProjectButton(driver):
    global wait
    AddProject = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a[1]')
    assert AddProject.is_enabled()
    print("The Add project button is Enabled.")
    AddProject.click()
    # time.sleep(8)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="project_name"]')))


@pytest.mark.order(14)
def test_ValidateComponents(driver, nvar):
    global wait
    Project, StartDate, Deadline, DeadlineCheck, Category, Department, Client, Summary, Notes, PublicProject, \
        Member, Channel, Topic, OtherTopics, AddFile, Currency, Budget, Hr, Manual, ClientManage, Save, Cancel = nvar

    assert Project.is_enabled()
    print("The project textbox is Enabled.")
    assert StartDate.is_enabled()
    print("The start date input is Enabled.")
    assert Deadline.is_enabled()
    print("The Deadline input is Enabled.")
    assert DeadlineCheck.is_enabled()
    print("The Deadline checkbox is Enabled.")
    assert Category.is_enabled()
    print("The Category dropdown is Enabled.")
    assert Department.is_enabled()
    print("The Department dropdown is Enabled.")
    assert Client.is_enabled()
    print("The Client dropdown is Enabled.")
    assert Summary.is_enabled()
    print("The Summary textarea is Enabled.")
    assert Notes.is_enabled()
    print("The Notes textarea is Enabled.")
    assert PublicProject.is_enabled()
    print("The Public project checkbox is Enabled.")
    assert Member.is_enabled()
    print("The Member dropdown is Enabled.")
    assert Channel.is_enabled()
    print("The Channel dropdown is Enabled.")
    assert Topic.is_enabled()
    print("The Topic input is Enabled.")
    assert OtherTopics.is_enabled()
    print("The Other Details button is Enabled.")
    OtherTopics.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="other-project-details"]/div[2]/div/div/button')))
    assert AddFile.is_enabled()
    print("The Add file input is Enabled.")
    assert Currency.is_enabled()
    print("The Currency dropdown is Enabled.")
    assert Budget.is_enabled()
    print("The Budget input is Enabled.")
    assert Hr.is_enabled()
    print("The Hours input is Enabled.")
    assert Manual.is_enabled()
    print("The Allow Manual time logs checkbox is Enabled.")
    assert ClientManage.is_enabled()
    print("The Client can manage tasks of this project checkbox is Enabled.")
    assert Save.is_enabled()
    print("The Save button is Enabled.")
    assert Cancel.is_enabled()
    print("The Cancel button is Enabled.")


@pytest.mark.order(15)
def test_WithBlankValue(driver, nvar):
    Project, StartDate, Deadline, DeadlineCheck, Category, Department, Client, Summary, Notes, PublicProject, \
        Member, Channel, Topic, OtherTopics, AddFile, Currency, Budget, Hr, Manual, ClientManage, Save, Cancel = nvar

    global wait
    Save.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[1]/div/div')))
    ProjectMsg = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[1]/div/div')
    StartDateMsg = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[2]/div/div[2]')
    DeadlineMsg = driver.find_element(By.XPATH, '//*[@id="deadlineBox"]/div/div[2]')
    MemberMsg = driver.find_element(By.XPATH, '//*[@id="add_members"]/div/div/div[3]')

    if ProjectMsg.text == "The project name field is required.":
        print('"The project name field is required." Message displayed successfully.')
    if StartDateMsg.text == "The start date field is required.":
        print('"The start date field is required." Message displayed successfully.')
    if DeadlineMsg.text == "The Deadline field is required.":
        print('"The Deadline field is required." Message displayed successfully.')
    if MemberMsg.text == "Select at least 1 Member":
        print('"Select at least 1 Member" Message displayed successfully.')


@pytest.mark.order(16)
def test_WithInvalidValue(driver, nvar):
    Project, StartDate, Deadline, DeadlineCheck, Category, Department, Client, Summary, Notes, PublicProject, \
        Member, Channel, Topic, OtherTopics, AddFile, Currency, Budget, Hr, Manual, ClientManage, Save, Cancel = nvar

    global wait
# send keys in project textbox
    Project.clear()
    Project.send_keys(InvalidProject)
# Click on Start Date input
    StartDate.click()
    # send keys to start date
    StartDate.clear()
    StartDate.send_keys(InvalidStartDate)
# Click on Deadline input
    Deadline.click()
    # send keys to Deadline
    Deadline.clear()
    Deadline.send_keys(InvalidDeadline)
# Click on Category dropdown
    Category.click()
    CategorySrch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[5]/div/div[1]/div/div[1]/input')
    # Search for valid option
    CategorySrch.send_keys(InvalidCategory)
    LiElements = driver.find_elements(By.TAG_NAME, 'li')
    # Iterate tHrough the <li> elements and find the first one that has the "active" class
    active_a = None
    for li in LiElements:
        if li.get_attribute('class') == 'no-results':
            print('"No result found" message displayed successfully for invalid search in Hours dropdown')
            break
    # Click on the active <li> element
    if active_a is not None:
        active_a.click()
# Click on Department dropdown
    Department.click()
    DepartmentSrch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[6]/div/div[1]/div/div[1]/input')
    # Search for valid option
    DepartmentSrch.send_keys(InvalidDepartment)
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
# Click on Client dropdown
    Client.click()
    ClientSrch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[7]/div/div[1]/div/div[1]/input')
    # Search for valid option
    ClientSrch.send_keys(InvalidClient)
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
# Click on Summary dropdown
    Summary.clear()
    driver.find_element(By.XPATH,
                        '//*[@id="save-project-data-form"]/div/div[1]/div[8]/div/div[1]/span[2]/button[1]').click()
    Summary.send_keys(InvalidSummary)
# Click on Notes dropdown
    Notes.clear()
    driver.find_element(By.XPATH,
                        '//*[@id="save-project-data-form"]/div/div[1]/div[9]/div/div[1]/span[2]/button[2]').click()
    Notes.send_keys(inValidNote)
# Click on Member dropdown
    Member.click()
    MemberSrch = driver.find_element(By.XPATH,
                                      '//*[@id="add_members"]/div/div/div[1]/div/div[1]/input')
    # Search for valid option
    MemberSrch.send_keys(InvalidMember)
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
# Click on Channel dropdown
    Channel.click()
    ChannelSrch = driver.find_element(By.XPATH,
                                      '//*[@id="save-project-data-form"]/div/div[1]/div[12]/div/div[1]/div/div[1]/input')
    # Search for valid option
    ChannelSrch.send_keys(InvalidChannel)
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
# Click on Topic input
    Topic.clear()
    Topic.send_keys(InvalidTopic)
# Click on Currency dropdown
    Currency.click()
    CurrencySrch = driver.find_element(By.XPATH,
                                       '//*[@id="other-project-details"]/div[2]/div/div/div/div[1]/input')
    # Search for valid option
    CurrencySrch.send_keys(InvalidCurrency)
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
# Click on Budget dropdown
    Budget.clear()
    Budget.send_keys(InvalidBudget)
# Click on Hours input
    Hr.clear()
    Hr.send_keys(InvalidHr)
# Click on Manual timelog checkbox
    Manual.click()
# Click Save button
    Save.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[2]/div/div[2]')))
    StartDateMsg = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[2]/div/div[2]')
    DeadlineMsg = driver.find_element(By.XPATH, '//*[@id="deadlineBox"]/div/div[2]')
    if StartDateMsg.text == "The start date does not match the format d-m-Y.":
        print('"The start date does not match the format d-m-Y." Message displayed successfully.')
    if DeadlineMsg.text == "The Deadline does not match the format d-m-Y.":
        print('"The Deadline does not match the format d-m-Y." Message displayed successfully.')


@pytest.mark.order(17)
def test_WithInvalidStartdateAndDeadline(driver, nvar):
    Project, StartDate, Deadline, DeadlineCheck, Category, Department, Client, Summary, Notes, PublicProject, \
        Member, Channel, Topic, OtherTopics, AddFile, Currency, Budget, Hr, Manual, ClientManage, Save, Cancel = nvar

    global wait
# send keys in project textbox
    Project.clear()
    Project.send_keys(ValidProject)
# Click on Start Date input
    StartDate.click()
    # send keys to start date
    StartDate.clear()
    StartDate.send_keys("17-05-2023")
# Click on Deadline input
    Deadline.click()
    # send keys to Deadline
    Deadline.clear()
    Deadline.send_keys("16-05-2023")
# Click on Category dropdown
    Category.click()
    CategorySrch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[5]/div/div[1]/div/div[1]/input')
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
# Click on Department dropdown
    Department.click()
    DepartmentSrch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[6]/div/div[1]/div/div[1]/input')
    # Search for valid option
    DepartmentSrch.send_keys(ValidDepartment)
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
# Click on Client dropdown
    Client.click()
    ClientSrch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[7]/div/div[1]/div/div[1]/input')
    # Search for valid option
    ClientSrch.send_keys(ValidClient)
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
# Click on Summary dropdown
    Summary.clear()
    driver.find_element(By.XPATH,
                        '//*[@id="save-project-data-form"]/div/div[1]/div[8]/div/div[1]/span[2]/button[1]').click()
    Summary.send_keys(ValidSummary)
# Click on Notes dropdown
    Notes.clear()
    driver.find_element(By.XPATH,
                        '//*[@id="save-project-data-form"]/div/div[1]/div[9]/div/div[1]/span[2]/button[2]').click()
    Notes.send_keys(ValidNote)
# Click on Member dropdown
    Member.click()
    MemberSrch = driver.find_element(By.XPATH,
                                      '//*[@id="add_members"]/div/div/div[1]/div/div[1]/input')
    # Search for valid option
    MemberSrch.send_keys(ValidMember)
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
# Click on Channel dropdown
    Channel.click()
    ChannelSrch = driver.find_element(By.XPATH,
                                      '//*[@id="save-project-data-form"]/div/div[1]/div[12]/div/div[1]/div/div[1]/input')
    # Search for valid option
    ChannelSrch.send_keys(ValidChannel)
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
# Click on Topic input
    Topic.clear()
    Topic.send_keys(ValidTopic)
# Click on Currency dropdown
    Currency.click()
    CurrencySrch = driver.find_element(By.XPATH,
                                       '//*[@id="other-project-details"]/div[2]/div/div/div/div[1]/input')
    # Search for valid option
    CurrencySrch.send_keys(ValidCurrency)
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
# Click on Budget dropdown
    Budget.clear()
    Budget.send_keys(ValidBudget)
# Click on Hours input
    Hr.clear()
    Hr.send_keys(ValidHr)
# Click on Manual timelog checkbox
    Manual.click()
# Click Save button
    Save.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deadlineBox"]/div/div[2]')))
    DeadlineMsg = driver.find_element(By.XPATH, '//*[@id="deadlineBox"]/div/div[2]')
    if DeadlineMsg.text == "The Deadline must be a date after or equal to start date.":
        print('"The Deadline must be a date after or equal to start date." Message displayed successfully.')


@pytest.mark.order(18)
def test_WithValidDataAndCheckbox(driver, nvar):
    Project, StartDate, Deadline, DeadlineCheck, Category, Department, Client, Summary, Notes, PublicProject, \
        Member, Channel, Topic, OtherTopics, AddFile, Currency, Budget, Hr, Manual, ClientManage, Save, Cancel = nvar

    global wait
# send keys in project textbox
    Project.clear()
    Project.send_keys(ValidProject)
# Click on Start Date input
    StartDate.click()
    # send keys to start date
    StartDate.clear()
    StartDate.send_keys("17-05-2023")
# Check Deadline checkbox
    DeadlineCheck.click()
# Click on Deadline input
    try:
        Deadline.click()
    except ElementNotInteractableException:
        print('When user check the "There is no project Deadline" checkbox the Deadline element removed successfully')
# Click on Category dropdown
    Category.click()
    CategorySrch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[5]/div/div[1]/div/div[1]/input')
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
# Click on Department dropdown
    Department.click()
    DepartmentSrch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[6]/div/div[1]/div/div[1]/input')
    # Search for valid option
    DepartmentSrch.send_keys(ValidDepartment)
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
# Click on Client dropdown
    Client.click()
    ClientSrch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[7]/div/div[1]/div/div[1]/input')
    # Search for valid option
    ClientSrch.send_keys(ValidClient)
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
# Click on Summary dropdown
    Summary.clear()
    driver.find_element(By.XPATH,
                        '//*[@id="save-project-data-form"]/div/div[1]/div[8]/div/div[1]/span[2]/button[1]').click()
    Summary.send_keys(ValidSummary)
# Click on Notes dropdown
    Notes.clear()
    driver.find_element(By.XPATH,
                        '//*[@id="save-project-data-form"]/div/div[1]/div[9]/div/div[1]/span[2]/button[2]').click()
    Notes.send_keys(ValidNote)
    Member.click()
    MemberSrch = driver.find_element(By.XPATH,
                                      '//*[@id="add_members"]/div/div/div[1]/div/div[1]/input')
    # Search for valid option
    MemberSrch.send_keys(ValidMember)
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
# Click on Channel dropdown
    Channel.click()
    ChannelSrch = driver.find_element(By.XPATH,
                                      '//*[@id="save-project-data-form"]/div/div[1]/div[12]/div/div[1]/div/div[1]/input')
    # Search for valid option
    ChannelSrch.send_keys(ValidChannel)
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
# Click on Topic input
    Topic.clear()
    Topic.send_keys(ValidTopic)

# Click on Currency dropdown
    Currency.click()
    CurrencySrch = driver.find_element(By.XPATH,
                                       '//*[@id="other-project-details"]/div[2]/div/div/div/div[1]/input')
    # Search for valid option
    CurrencySrch.send_keys(ValidCurrency)
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
# Click on Budget dropdown
    Budget.clear()
    Budget.send_keys(ValidBudget)
# Click on Hours input
    Hr.clear()
    Hr.send_keys(ValidHr)
# Click on Manual timelog checkbox
    Manual.click()
# Check the Client can manage tasks of this project checkbox
    ClientManage.click()
    task_notification = driver.find_element(By.XPATH, '//*[@id="client_task_notification"]')
    if task_notification.is_enabled():
        print('When user check the "The Client can manage tasks of this project" checkbox the "Send task notification '
              'to Client?" checkbox is enabled.')
# Click Save button
    Save.click()
    # time.sleep(4)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="table-actions"]/a[1]')))
    AddProject = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a[1]')
    if AddProject.is_enabled():
        print("The Form with valid data Saved successfully.")
    time.sleep(5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//table//tbody//tr[1]')))
    time.sleep(3)


@pytest.mark.order(19)
def test_SearchInTable(driver):
    global wait
    # find the Saved Project in table and click on edit button
    Row1 = driver.find_element(By.XPATH, '//table//tbody//tr[1]')
    Cell1 = Row1.find_element(By.XPATH, './/td[2]')
    VarId = Cell1.text
    driver.find_element(By.XPATH, f'//*[@id="dropdownMenuLink-%s"]' % VarId).click()
    driver.find_element(By.XPATH, f'//*[@id="row-%s"]/td[9]/div/div/div/a[2]' % VarId).click()
    print("The Project searched successfully in the table")
    time.sleep(5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="project_name"]')))


@pytest.mark.order(20)
def test_EditAndSave(driver):
    global wait
    time.sleep(5)
    Project = driver.find_element(By.XPATH, '//*[@id="project_name"]')
    # Edit project name
    Project.clear()
    Project.send_keys("Project Testing")
    # Edit status of Project
    Status = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[10]/div/div/button')
    Status.click()
    StatusSrch = driver.find_element(By.XPATH, '//*[@id="save-project-data-form"]/div/div[1]/div[10]/div/div/div/div[1]/input')
    # Search for valid option
    StatusSrch.send_keys("In Progress")
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
    Save = driver.find_element(By.XPATH, '//*[@id="save-project-form"]')
    Save.click()
    # time.sleep(10)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="table-actions"]/a[1]')))
    AddProject = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a[1]')
    if AddProject.is_enabled():
        print("The Edit form Saved successfully.")
    # Close the web driver
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr')))
    time.sleep(5)


@pytest.mark.order(21)
def test_AddSprint(driver):
    global wait
    # find the Saved lead in table and click on edit button
    Row1 = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]')
    Cell1 = Row1.find_element(By.XPATH, './/td[2]')
    VarId = Cell1.text
    # driver.find_element(By.XPATH, f'//*[@id="dropdownMenuLink-%s"]' % VarId).click()
    try:
        driver.find_element(By.XPATH, f'//*[@id="row-%s"]/td[3]/div/div/h5/a' % VarId).click()
    except StaleElementReferenceException:
        time.sleep(2)
        driver.find_element(By.XPATH, f'//*[@id="row-%s"]/td[3]/div/div/h5/a' % VarId).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mob-client-detail"]/nav/ul/li[6]/a')))
    Sprint = driver.find_element(By.XPATH, '//*[@id="mob-client-detail"]/nav/ul/li[6]/a')
    Sprint.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="table-actions"]/a')))
    add_Sprint = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a')
    add_Sprint.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="heading"]')))
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
    Save = driver.find_element(By.XPATH, '//*[@id="save-task-form"]')
    Save.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="table-actions"]/a')))
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
    time.sleep(3)