import pytest_html
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time


# @pytest.mark.screenshot
def test_login(driver, selenium):
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("saurabhdhariwal.com@gmail.com")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("addweb123")
    driver.find_element(By.XPATH, '//*[@id="submit-login"]').click()
    selenium.save_screenshot('screenshot.png')
    with open('screenshot.png', 'rb') as image:
        pytest_html.extras.image(image.read(), "Screenshot")

    time.sleep(5)


# @pytest.mark.screenshot
def test_dashboard(driver):
    # Verify that the user is on Dashboard page then Click on Leads button on dashboard
    expected_title = "Dashboard"
    actual_title = driver.title

    if actual_title == expected_title:
        print("Successfully Logged in")
        driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[2]/a').click()
    else:
        print("Failed to Login")
        driver.quit()

    time.sleep(3)


# @pytest.mark.screenshot
def test_leads(driver):
    # Verify that the user is on Dashboard page then Click on Leads button on dashboard
    expected_title = "Leads"
    actual_title = driver.title

    if actual_title == expected_title:
        print("Successfully reached on Leads page")
    else:
        print("Failed to reach")
        driver.quit()


# @pytest.mark.screenshot
def test_buttons(driver):
    # Check that all buttons are active or not on Leads page
    add_button = driver.find_element(By.XPATH, '//*[@id="table-actions"]/a')
    time.sleep(3)

    # Click on Add Lead button on Leads page
    add_button.click()
    time.sleep(3)


# @pytest.mark.screenshot
def test_newlead(driver):
    # Fill the New Lead form

    # find & click on Salutation dropdown button
    select_btn = driver.find_element(By.XPATH,
                                     '//*[@id="save-lead-data-form"]/div/div[1]/div[1]/div/div/button')
    select_btn.click()

    # Find and select option from Salutation <select>
    sel = Select(driver.find_element(By.XPATH, '//*[@id="salutation"]'))
    sel.select_by_visible_text("Mr")

    # Enter Lead name
    driver.find_element(By.ID, 'client_name').send_keys("Johnny Harper")

    # Enter Lead email
    driver.find_element(By.ID, 'client_email').send_keys("johnnyharpertesting1@gmail.com")

    # find & click on Choose Agents dropdown button
    select_btn = driver.find_element(By.XPATH,
                                     '//*[@id="save-lead-data-form"]/div/div[1]/div[4]/div/div[1]/button')
    select_btn.click()

    # Find and select option from Choose Agents <select>
    sel = Select(driver.find_element(By.ID, 'agent_id'))
    sel.select_by_visible_text("Saurabh Dhariwal")

    # find & click on Lead Source dropdown button
    select_btn = driver.find_element(By.XPATH,
                                     '//*[@id="save-lead-data-form"]/div/div[1]/div[5]/div/div[1]/button')
    select_btn.click()

    # Find and select option from Lead Source <select>
    sel = Select(driver.find_element(By.ID, 'source_id'))
    sel.select_by_visible_text("Email")

    # find & click on Lead Category dropdown button
    select_btn = driver.find_element(By.XPATH,
                                     '//*[@id="save-lead-data-form"]/div/div[1]/div[6]/div/div[1]/button')
    select_btn.click()

    # Find and select option from Lead Category <select>
    sel = Select(driver.find_element(By.ID, 'category_id'))
    sel.select_by_visible_text("Xyz")

    # Enter Lead Value
    driver.find_element(By.ID, 'value').send_keys(0)

    # find & click on Allow Follow Up dropdown button
    select_btn = driver.find_element(By.XPATH,
                                     '//*[@id="save-lead-data-form"]/div/div[1]/div[8]/div/div/button')
    select_btn.click()

    # Find and select option from Allow Follow Up <select>
    sel = Select(driver.find_element(By.ID, 'next_follow_up'))
    sel.select_by_visible_text("Yes")

    # find & click on Status dropdown button
    select_btn = driver.find_element(By.XPATH,
                                     '//*[@id="save-lead-data-form"]/div/div[1]/div[9]/div/div/button')
    select_btn.click()

    # Find and select option from Status <select>
    sel = Select(driver.find_element(By.ID, 'status'))
    sel.select_by_visible_text("Pending")

    # Click on  Company Details link
    driver.find_element(By.XPATH, '//*[@id="save-lead-data-form"]/div/h4[2]/a').click()

    # Enter Company Name
    driver.find_element(By.ID, 'company_name').send_keys("Information Synergies")

    # Enter Website
    driver.find_element(By.ID, 'website').send_keys("https://www.addwebsolution.com/")

    # Enter Mobile number
    driver.find_element(By.ID, 'mobile').send_keys("9702347651")

    # Enter Office Phone Number
    driver.find_element(By.ID, 'office').send_keys("9802335625")

    # find & click on Country dropdown button
    select_btn = driver.find_element(By.XPATH, '//*[@id="other-details"]/div[5]/div/div/button')
    select_btn.click()

    # Find and select option from Country <select>
    sel = Select(driver.find_element(By.ID, 'country'))
    sel.select_by_visible_text("India")

    # Enter State
    driver.find_element(By.ID, 'state').send_keys("Gujarat")

    # Enter City
    driver.find_element(By.ID, 'city').send_keys("Ahmedabad")

    # Enter Postal code
    driver.find_element(By.ID, 'postal_code').send_keys("380009")

    # Check the validations and Save the form
    client_name = driver.find_element(By.ID, 'client_name')
    client_email = driver.find_element(By.ID, 'client_email')

    if client_name.get_attribute('value') == "":
        print("The Lead name is required")
        driver.quit()

    elif client_email.get_attribute('value') == "":
        print("The Lead email is required")
        driver.quit()
    else:
        driver.find_element(By.ID, "save-lead-form").click()

    time.sleep(5)


# @pytest.mark.screenshot
def test_search_new_lead(driver):
    # find the saved lead in table and click on edit button
    row1 = driver.find_element(By.XPATH, '//table//tbody//tr[1]')
    cell1 = row1.find_element(By.XPATH, './/td[2]')
    var_id = cell1.text

    driver.find_element(By.XPATH, f'//*[@id="dropdownMenuLink-%s"]' % var_id).click()
    time.sleep(2)

    driver.find_element(By.XPATH, f'//*[@id="row-%s"]/td[9]/div/div/div/a[2]' % var_id).click()
    time.sleep(2)


# @pytest.mark.screenshot
def test_edit_form(driver):
    # Change some fields in form and save
    driver.find_element(By.ID, 'client_name').clear()
    driver.find_element(By.ID, 'client_name').send_keys("testing")
    driver.find_element(By.ID, 'client_email').clear()
    driver.find_element(By.ID, 'client_email').send_keys("test1@gmail.com")

    driver.find_element(By.XPATH, '//*[@id="save-lead-form"]').click()
    time.sleep(5)


