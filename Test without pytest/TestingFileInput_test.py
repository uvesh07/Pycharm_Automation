import time

from selenium.webdriver.common.by import By

# Global variables used for different methods POC-QA-Automation
valid_email = "saurabhdhariwal.com@gmail.com"
valid_pass = "addweb123"


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


def test_Click_on_Projects(driver, selenium):
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/a').click()
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/div/a[5]').click()
    time.sleep(4)
    if driver.title == "Engagement":
        print("Successfully reached at Engagement page")


def test_Click_file_input(driver):
    valid_addfile = "/home/addweb/PycharmProjects/Ticktalk leads automation/Images/bg color.jpeg"
    driver.find_element(By.XPATH, '//*[@id="fullscreen"]/div[5]/div[1]/span/button').click()
    time.sleep(3)
    element = driver.find_element(By.XPATH, '//*[@id="customFile"]')
    # driver.execute_script("arguments[0].type = 'file';", element)
    # time.sleep(20)
    element.send_keys(valid_addfile)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="myModal"]/div/div/div[2]/form/button').click()
    time.sleep(10)
