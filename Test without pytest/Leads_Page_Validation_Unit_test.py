import unittest
import os
# import testRunner as testRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
import HtmlTestRunner


class Testing(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("Starting the class setUpClass....")
        # create a Service object for the ChromeDriver
        service = Service('/home/addweb/PycharmProjects/FirstScript/Drivers/chromedriver.exe')

        # create a webdriver object and pass the Service object
        cls.driver = webdriver.Chrome(service=service)

        # Login to the site
        cls.driver.get('https://ttstage.addwebprojects.com/login')
        cls.driver.maximize_window()
        cls.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("saurabhdhariwal.com@gmail.com")
        cls.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("addweb123")

        cls.driver.save_screenshot(os.path.join(os.getcwd(), "Screenshots", "Login.png"))

        cls.driver.find_element(By.XPATH, '//*[@id="submit-login"]').click()
        time.sleep(3)

    def test_dashboard(self):
        # Verify that the user is on Dashboard page then Click on Leads button on dashboard
        expected_title = "Dashboard"
        actual_title = self.driver.title

        if actual_title == expected_title:
            print("Successfully Logged in")
            self.driver.save_screenshot(os.path.join(os.getcwd(), "Screenshots", "Dashboard.png"))
            self.driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[2]/a').click()
        else:
            print("Failed to Login")
            self.driver.quit()

        time.sleep(3)

    def test_leads(self):
        # Verify that the user is on Dashboard page then Click on Leads button on dashboard
        expected_title = "Leads"
        actual_title = self.driver.title

        if actual_title == expected_title:
            print("Successfully reached on Leads page")
            self.driver.save_screenshot(os.path.join(os.getcwd(), "Screenshots", "Leads.png"))
        else:
            print("Failed to reach")
            self.driver.quit()

    def test_buttons(self):
        # Check that all buttons are active or not on Leads page
        Testing.add_button = self.driver.find_element(By.XPATH, '//*[@id="table-actions"]/a')
        time.sleep(3)

        # Click on Add Lead button on Leads page
        Testing.add_button.click()
        time.sleep(3)

    def test_newlead(self):
        # Fill the New Lead form
        self.driver.save_screenshot(os.path.join(os.getcwd(), "Screenshots", "NewLead.png"))
        # find & click on Salutation dropdown button
        select_btn = self.driver.find_element(By.XPATH,
                                              '//*[@id="save-lead-data-form"]/div/div[1]/div[1]/div/div/button')
        select_btn.click()

        # Find and select option from Salutation <select>
        sel = Select(self.driver.find_element(By.XPATH, '//*[@id="salutation"]'))
        sel.select_by_visible_text("Mr")

        # Enter Lead name
        self.driver.find_element(By.ID, 'client_name').send_keys("Johnny Harper")

        # Enter Lead email
        self.driver.find_element(By.ID, 'client_email').send_keys("johnnyharpertesting1@gmail.com")

        # find & click on Choose Agents dropdown button
        select_btn = self.driver.find_element(By.XPATH,
                                              '//*[@id="save-lead-data-form"]/div/div[1]/div[4]/div/div[1]/button')
        select_btn.click()

        # Find and select option from Choose Agents <select>
        sel = Select(self.driver.find_element(By.ID, 'agent_id'))
        sel.select_by_visible_text("Saurabh Dhariwal")

        # find & click on Lead Source dropdown button
        select_btn = self.driver.find_element(By.XPATH,
                                              '//*[@id="save-lead-data-form"]/div/div[1]/div[5]/div/div[1]/button')
        select_btn.click()

        # Find and select option from Lead Source <select>
        sel = Select(self.driver.find_element(By.ID, 'source_id'))
        sel.select_by_visible_text("Email")

        # find & click on Lead Category dropdown button
        select_btn = self.driver.find_element(By.XPATH,
                                              '//*[@id="save-lead-data-form"]/div/div[1]/div[6]/div/div[1]/button')
        select_btn.click()

        # Find and select option from Lead Category <select>
        sel = Select(self.driver.find_element(By.ID, 'category_id'))
        sel.select_by_visible_text("Xyz")

        # Enter Lead Value
        self.driver.find_element(By.ID, 'value').send_keys(0)

        # find & click on Allow Follow Up dropdown button
        select_btn = self.driver.find_element(By.XPATH,
                                              '//*[@id="save-lead-data-form"]/div/div[1]/div[8]/div/div/button')
        select_btn.click()

        # Find and select option from Allow Follow Up <select>
        sel = Select(self.driver.find_element(By.ID, 'next_follow_up'))
        sel.select_by_visible_text("Yes")

        # find & click on Status dropdown button
        select_btn = self.driver.find_element(By.XPATH,
                                              '//*[@id="save-lead-data-form"]/div/div[1]/div[9]/div/div/button')
        select_btn.click()

        # Find and select option from Status <select>
        sel = Select(self.driver.find_element(By.ID, 'status'))
        sel.select_by_visible_text("Pending")

        # Click on  Company Details link
        self.driver.find_element(By.XPATH, '//*[@id="save-lead-data-form"]/div/h4[2]/a').click()

        # Enter Company Name
        self.driver.find_element(By.ID, 'company_name').send_keys("Information Synergies")

        # Enter Website
        self.driver.find_element(By.ID, 'website').send_keys("https://www.addwebsolution.com/")

        # Enter Mobile number
        self.driver.find_element(By.ID, 'mobile').send_keys("9702347651")

        # Enter Office Phone Number
        self.driver.find_element(By.ID, 'office').send_keys("9802335625")

        # find & click on Country dropdown button
        select_btn = self.driver.find_element(By.XPATH, '//*[@id="other-details"]/div[5]/div/div/button')
        select_btn.click()

        # Find and select option from Country <select>
        sel = Select(self.driver.find_element(By.ID, 'country'))
        sel.select_by_visible_text("India")

        # Enter State
        self.driver.find_element(By.ID, 'state').send_keys("Gujarat")

        # Enter City
        self.driver.find_element(By.ID, 'city').send_keys("Ahmedabad")

        # Enter Postal code
        self.driver.find_element(By.ID, 'postal_code').send_keys("380009")

        self.driver.save_screenshot(os.path.join(os.getcwd(), "Screenshots", "FilledForm.png"))

        # Check the validations and Save the form
        client_name = self.driver.find_element(By.ID, 'client_name')
        client_email = self.driver.find_element(By.ID, 'client_email')

        if client_name.get_attribute('value') == "":
            print("The Lead name is required")
            self.driver.quit()

        elif client_email.get_attribute('value') == "":
            print("The Lead email is required")
            self.driver.quit()
        else:
            self.driver.find_element(By.ID, "save-lead-form").click()

        time.sleep(5)

    def test_search_new_lead(self):
        # find the saved lead in table and click on edit button
        row1 = self.driver.find_element(By.XPATH, '//table//tbody//tr[1]')
        cell1 = row1.find_element(By.XPATH, './/td[2]')
        var_id = cell1.text

        self.driver.find_element(By.XPATH, f'//*[@id="dropdownMenuLink-%s"]' % var_id).click()
        time.sleep(2)

        self.driver.save_screenshot(os.path.join(os.getcwd(), "Screenshots", "LeadsonTable.png"))

        self.driver.find_element(By.XPATH, f'//*[@id="row-%s"]/td[9]/div/div/div/a[2]' % var_id).click()
        time.sleep(2)

    def test_edit_form(self):
        # Change some fields in form and save
        self.driver.find_element(By.ID, 'client_name').clear()
        self.driver.find_element(By.ID, 'client_name').send_keys("testing")
        self.driver.find_element(By.ID, 'client_email').clear()
        self.driver.find_element(By.ID, 'client_email').send_keys("test1@gmail.com")

        self.driver.save_screenshot(os.path.join(os.getcwd(), "Screenshots", "EditForm.png"))

        self.driver.find_element(By.XPATH, '//*[@id="save-lead-form"]').click()
        time.sleep(5)


if __name__ == "__main__":
    os.makedirs("Screenshots", exist_ok=True)
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(Testing('test_dashboard'))
    suite.addTest(Testing('test_leads'))
    suite.addTest(Testing('test_buttons'))
    suite.addTest(Testing('test_newlead'))
    suite.addTest(Testing('test_search_new_lead'))
    suite.addTest(Testing('test_edit_form'))
    runner = HtmlTestRunner.HTMLTestRunner(output='..//Reports')
    runner.run(suite)
