import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta
import HtmlTestRunner

total_hrs = 0
total_min = 0
user = "Krimit Shah"


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

        # cls.driver.save_screenshot(os.path.join(os.getcwd(), "screenshots", "Login.png"))

        cls.driver.find_element(By.XPATH, '//*[@id="submit-login"]').click()
        time.sleep(3)

    def test_dashboard(self):
        # Verify that the user is on Dashboard page then Click on Time Log button on dashboard
        expected_title = "Dashboard"
        actual_title = self.driver.title

        if actual_title == expected_title:
            print("Successfully Logged in")
            # self.driver.save_screenshot(os.path.join(os.getcwd(), "screenshots", "Dashboard.png"))
            self.driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/a').click()
            self.driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/div/a[4]').click()
        else:
            print("Failed to Login")
            self.driver.quit()

        time.sleep(3)

    def test_logs(self):
        # Verify that the user is on Dashboard page then Click on Leads button on dashboard
        expected_title = "Time Logs"
        actual_title = self.driver.title

        if actual_title == expected_title:
            print("Successfully reached on Time Logs page")
            time.sleep(3)
            # self.driver.save_screenshot(os.path.join(os.getcwd(), "screenshots", "Leads.png"))
        else:
            print("Failed to reach")
            self.driver.quit()

    def test_date_log(self):
        global user
        # // *[ @ id = "row-55702"] / td[5]
        # Check that all buttons are active or not on Leads page
        select_btn = self.driver.find_element(By.XPATH,
                                              '//*[@id="filter-form"]/div/div[2]/div/div/button')
        select_btn.click()

        # Find and select option from Salutation <select>
        sel = Select(self.driver.find_element(By.XPATH, '//*[@id="employee"]'))
        sel.select_by_visible_text(user)

        time.sleep(3)

    def test_search_by_date(self):
        global total_hrs
        global total_min
        # Find the table element
        table = self.driver.find_element(By.XPATH, '//*[@id="timelogs-table"]/tbody')

        # Find all rows within the table
        rows = table.find_elements(By.TAG_NAME, "tr")

        flag = 0
        # Loop through each row and extract the data
        for row in rows:
            # Find all cell 5 within the row
            date = row.find_element(By.XPATH, './/td[5]')
            Actual_date = date.text[0:10]
            Expected_date = "29-03-2023"
            hrs = 0
            min = 0
            if Actual_date == Expected_date:
                flag = 1
                sel_hrs = row.find_element(By.XPATH, './/td[7]')
                ext_hrs = int(sel_hrs.text[0:1])
                hrs += ext_hrs
                ext_min = int(sel_hrs.text[6:8])
                min += ext_min
                if min > 60:
                    min = min - 60
                    hrs += 1

                # print(ext_hrs , ext_min)

            total_hrs += hrs
            total_min += min

        while total_min >= 60:
            total_hrs += 1
            total_min -= 60

        extra_hrs = total_hrs - 8
        total_time_worked = timedelta(hours=total_hrs, minutes=total_min)

        if flag == 0:
            print(f"The {Expected_date} date is not there in the table.")
        elif total_time_worked > timedelta(hours=8):
            print(f"{user} worked {extra_hrs} hour and {total_min} minutes extra on {Expected_date}")

        self.driver.quit()


if __name__ == "__main__":
    # os.makedirs("screenshots", exist_ok=True)
    if not os.path.exists('reports'):
        os.makedirs('reports')

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(Testing('test_dashboard'))
    suite.addTest(Testing('test_logs'))
    suite.addTest(Testing('test_date_log'))
    suite.addTest(Testing('test_search_by_date'))
    runner = HtmlTestRunner.HTMLTestRunner(output='..//reports', report_title='Logs validation report')
    runner.run(suite)


