from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

# create a Service object for the ChromeDriver
service = Service('/home/addweb/PycharmProjects/FirstScript/Drivers/chromedriver.exe')

# create a webdriver object and pass the Service object
driver = webdriver.Chrome(service=service)

# Login to the site
driver.get('https://ttstage.addwebprojects.com/login')
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("saurabhdhariwal.com@gmail.com")
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("addweb123")
driver.find_element(By.XPATH, '//*[@id="submit-login"]').click()

time.sleep(3)
# Click on Leads button on dashboard
driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[2]/a/span').click()

# Click on Add Lead button on dashboard
driver.find_element(By.XPATH, '//*[@id="table-actions"]/a').click()

time.sleep(3)
# Fill the New Lead form

# find & click on Salutation dropdown button
select_btn = driver.find_element(By.XPATH, '//*[@id="save-lead-data-form"]/div/div[1]/div[1]/div/div/button')
select_btn.click()

# Find and select option from Salutation <select>
sel = Select(driver.find_element(By.XPATH, '//*[@id="salutation"]'))
sel.select_by_visible_text("Mr")

# Enter Lead name
driver.find_element(By.ID, 'client_name').send_keys("Johnny Harper")

# Enter Lead email
driver.find_element(By.ID, 'client_email').send_keys("johnnyharpertesting1@gmail.com")

# find & click on Choose Agents dropdown button
select_btn = driver.find_element(By.XPATH, '//*[@id="save-lead-data-form"]/div/div[1]/div[4]/div/div[1]/button')
select_btn.click()

# Find and select option from Choose Agents <select>
sel = Select(driver.find_element(By.ID, 'agent_id'))
sel.select_by_visible_text("Saurabh Dhariwal")

# find & click on Lead Source dropdown button
select_btn = driver.find_element(By.XPATH, '//*[@id="save-lead-data-form"]/div/div[1]/div[5]/div/div[1]/button')
select_btn.click()

# Find and select option from Lead Source <select>
sel = Select(driver.find_element(By.ID, 'source_id'))
sel.select_by_visible_text("Email")

# find & click on Lead Category dropdown button
select_btn = driver.find_element(By.XPATH, '//*[@id="save-lead-data-form"]/div/div[1]/div[6]/div/div[1]/button')
select_btn.click()

# Find and select option from Lead Category <select>
sel = Select(driver.find_element(By.ID, 'category_id'))
sel.select_by_visible_text("Xyz")

# Enter Lead Value
driver.find_element(By.ID, 'value').send_keys(0)

# find & click on Allow Follow Up dropdown button
select_btn = driver.find_element(By.XPATH, '//*[@id="save-lead-data-form"]/div/div[1]/div[8]/div/div/button')
select_btn.click()

# Find and select option from Allow Follow Up <select>
sel = Select(driver.find_element(By.ID, 'next_follow_up'))
sel.select_by_visible_text("Yes")

# find & click on Status dropdown button
select_btn = driver.find_element(By.XPATH, '//*[@id="save-lead-data-form"]/div/div[1]/div[9]/div/div/button')
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

# Save the form
# driver.find_element(By.ID, 'save-lead-form').click()

time.sleep(5)
