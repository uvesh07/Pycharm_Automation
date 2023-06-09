import os
import shutil
from email import encoders
from email.mime.base import MIMEBase

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from rocketchat_API.rocketchat import RocketChat
import requests

# Global variables to store test results
message = "This is for testing purpose."

total_tests = 0
num_passed = 0
num_failed = 0
num_errors = 0
num_skipped = 0


# In conftest.py
def pytest_collection_modifyitems(config, items):
    # Sort the test items based on the marker order
    items.sort(key=lambda x: int(x.get_closest_marker("order").args[0]))


@pytest.fixture(scope="session", autouse=True, name="driver")
def setup():
    # create a Service object for the ChromeDriver
    service = Service('/home/addweb/PycharmProjects/FirstScript/Drivers/chromedriver.exe')

    # create a webdriver object and pass the Service object
    global driver
    driver = webdriver.Chrome(service=service)

    # Login to the site
    driver.get('https://ttstage.addwebprojects.com/login')
    driver.maximize_window()

    print("Launch browser")

    return driver


def pytest_runtest_makereport(item, call):

    global total_tests, num_passed, num_failed, num_errors, num_skipped

    if call.when == "call":  # Called after each test execution

        # Increment the total test count
        total_tests += 1

        # Check the outcome of the test
        if call.excinfo is None:
            # Test passed
            num_passed += 1
        elif call.excinfo.errisinstance(pytest.fail.Exception):
            # Test failed
            num_failed += 1
        elif call.excinfo.errisinstance(Exception):
            # Test resulted in an error
            num_errors += 1
        elif call.excinfo.errisinstance(pytest.skip.Exception):
            # Test was skipped
            num_skipped += 1

    # outcome = call.excinfo is None
    #
    # # Determine the status message based on the outcome
    # status = "Pass" if outcome else "Fail" if call.excinfo is not None else "Error"
    #
    # # Get the test case name
    # test_case_name = item.nodeid
    #
    # # Get the test case execution time
    # execution_time = call.duration
    #
    # # Print or process the collected information as per your requirement
    # message += f"Test Case: {test_case_name} \n"
    # message += f"Status: {status}\n"
    # message += f"Execution Time: {execution_time} seconds \n"

    # print(message)


def send_to_channel(message):

    # Set the Rocket.Chat server URL
    server_url = 'https://chat.addwebsolution.in/'

    # Set the authentication details
    username = 'uvesh@addwebsolution.in'
    password = 'Uvesh@890'

    # Set the channel or user to whom you want to send the zip file
    team_room = 'team-circuit-breakers'
    # team_room = 'uvesh'

    # attachment_path = attachment_path + ".zip"

    # Prepare the file payload
    # file_name = os.path.basename(attachment_path)
    # files = {
    #     "file": (file_name, open(attachment_path, "rb"), "application/zip")
    # }

    rocket = RocketChat('uvesh@addwebsolution.in', 'Uvesh@890', server_url='https://chat.addwebsolution.in/')

    rocket.chat_post_message(room_id=team_room, text=message)


def pytest_terminal_summary(terminalreporter):
    global total_tests, num_passed, num_failed, num_errors, num_skipped
    global message

    message = "Test summary \n"
    message += f"Total Tests: {total_tests} \n"
    message += f"Passed: {num_passed} \n"
    message += f"Failed: {num_failed} \n"
    message += f"Errors: {num_errors} \n"
    message += f"Skipped: {num_skipped} \n"

    send_to_channel(message)


# def zip_folder(folder_path, zip_file_path):
#     shutil.make_archive(zip_file_path, 'zip', folder_path)
#
#
# def upload_file_to_rocket_chat(api_token, user_id, channel_id, file_path, file_name):
#     # Set the Rocket.Chat API endpoint
#     api_endpoint = 'https://chat.addwebsolution.in/api/v1/rooms.upload'
#
#     # Set the headers with API token and user ID
#     headers = {
#         'X-Auth-Token': api_token,
#         'X-User-Id': user_id
#     }
#
#     # Set the payload with channel ID and file details
#     payload = {
#         'roomId': channel_id
#     }
#
#     # Open the file in binary mode and upload it
#     with open(file_path, 'rb') as file:
#         files = {
#             'file': (file_name, file)
#         }
#
#         # Send the request to upload the file
#         response = requests.post(api_endpoint, headers=headers, data=payload, files=files)
#
#         # Check the response status
#         if response.status_code == 200:
#             print('File uploaded successfully to Rocket.Chat!')
#         else:
#             print('Failed to upload file to Rocket.Chat. Error:', response.content)
#
#
# def pytest_terminal_summary(terminalreporter):
#     # Specify the folder path and zip file path
#     folder_path = 'Reports'  # Replace with the actual folder path
#     zip_file_path = 'Report'  # Replace with the desired zip file path
#
#     # Zip the folder
#     zip_folder(folder_path, zip_file_path)
#
#     # Example usage
#     api_token = 'ZnQW277ZcrrW-zIkPZ4G4truRA7fNs0w6DxIK8lVgRo'
#     user_id = 'mwno8n76GtDgGeL6u'
#     channel_id = 'team-circuit-breakers'
#     file_path = 'Report.zip'
#     file_name = 'Report.zip'
#
#     upload_file_to_rocket_chat(api_token, user_id, channel_id, file_path, file_name)


# def send_to_channel(attachment_path):
#     global message
#
#     # Set the Rocket.Chat server URL
#     server_url = 'https://chat.addwebsolution.in/'
#
#     # Set the authentication details
#     username = 'uvesh@addwebsolution.in'
#     password = 'Uvesh@890'
#
#     # Set the channel or user to whom you want to send the zip file
#     team_room = 'team-circuit-breakers'
#
#     attachment_path = attachment_path + ".zip"
#
#     # Prepare the file payload
#     file_name = os.path.basename(attachment_path)
#     files = {
#         "file": (file_name, open(attachment_path, "rb"), "application/zip")
#     }
#
#     # Authenticate and get the token
#     auth_response = RocketChat('uvesh@addwebsolution.in', 'Uvesh@890', server_url='https://chat.addwebsolution.in/')
#     # if auth_response.status_code != 200:
#     #     print('Failed to authenticate with Rocket.Chat. Error:', auth_response.content)
#     #     return
#
#     # token = auth_response.json().get('data').get('authToken')
#     token = "ZnQW277ZcrrW-zIkPZ4G4truRA7fNs0w6DxIK8lVgRo"
#
#     # Upload the zip file to Rocket.Chat
#     upload_response = requests.post(
#         f"{server_url}api/v1/rooms.upload/{team_room}",
#         headers={"X-Auth-Token": token},
#         files=files
#     )
#     if upload_response.status_code != 200:
#         print('Failed to upload zip file to Rocket.Chat. Error:', upload_response.content)
#         return
#
#     # Get the uploaded file details
#     file_id = upload_response.json().get('file').get('_id')
#     file_url = f"{server_url}file-upload/{file_id}"
#
#     # Specify the message content
#     message = 'Hello, this is a test message with a zip file attachment.'
#
#     # Send the message with the zip file attachment to the channel
#     message_payload = {
#         "channel": team_room,
#         "text": message,
#         "attachments": [{"title": file_name, "title_link": file_url}]
#     }
#     message_response = requests.post(
#         f"{server_url}api/v1/chat.postMessage",
#         headers={"X-Auth-Token": token},
#         json=message_payload
#     )
#     if message_response.status_code != 200:
#         print('Failed to send message to Rocket.Chat. Error:', message_response.content)
#         return
#
#     print('Zip file uploaded and message sent successfully.')

    # # Upload the zip file to Rocket.Chat
    # response = rocket.upload_file(room_id=team_room, file_path=attachment_path, description='Test Report')
    # if response.status_code == 200:
    #     # Get the file ID from the response
    #     file_id = response.json().get('file').get('_id')
    #
    #     # Specify the message content
    #     message = 'Hello, this is a test message with a zip file attachment.'
    #
    #     # Send the message with the zip file attachment to the channel
    #     rocket.chat_post_message(room_id=team_room, text=message,
    #                              attachments=[{"title": file_name, "title_link": file_id}])
    # else:
    #     print('Failed to upload zip file to Rocket.Chat. Error:', response.content)

    # Specify the path to your test report file
    # test_report_path = 'Reports/Final_Report.html'

    # Upload and send the test report
    # rocket.chat_upload_file(room_id=channel, file_path=test_report_path)

    # Specify the message content
    # message = 'Hello, this is a test message.'

    # # print(message)
    # message = "This is for Testing purpose"
    #
    # # Send the message to the channel
    # response = rocket.chat_post_message(room_id=team_room, text=message)
    # print(response.content)
    #
    # message = ""


# Hook to display a summary after all tests have finished
# def pytest_terminal_summary(terminalreporter):
#     # Specify the folder path and zip file path
#     folder_path = 'Reports'  # Replace with the actual folder path
#     zip_file_path = 'Report'  # Replace with the desired zip file path
#
#     # Zip the folder
#     zip_folder(folder_path, zip_file_path)
#
#     send_to_channel(zip_file_path)


# def send_to_channel(attachment_path):
#     # Set the Rocket.Chat server URL
#     server_url = 'https://chat.addwebsolution.in/'
#
#     # Set the authentication details
#     username = 'uvesh@addwebsolution.in'
#     password = 'Uvesh@890'
#
#     # Set the channel or user to whom you want to send the zip file
#     # team_room = 'team-circuit-breakers'
#     team_room = 'uvesh'
#
#     attachment_path = attachment_path + ".zip"
#
#     # Prepare the file payload
#     file_name = os.path.basename(attachment_path)
#     files = {
#         "file": (file_name, open(attachment_path, "rb"), "application/zip")
#     }
#
#     # rocket = RocketChat('uvesh@addwebsolution.in', 'Uvesh@890', server_url='https://chat.addwebsolution.in/')
#
#     # Authenticate and get the token
#     auth_response = requests.post(f"{server_url}api/v1/login", json={"user": username, "password": password})
#     if auth_response.status_code != 200:
#         print('Failed to authenticate with Rocket.Chat. Error:', auth_response.content)
#         return
#
#     token = auth_response.json().get('data').get('authToken')
#
#     # Upload the zip file to Rocket.Chat
#     upload_response = requests.post(
#         f"{server_url}api/v1/rooms.upload/{team_room}",
#         headers={"X-Auth-Token": token},
#         files=files
#     )
#     if upload_response.status_code != 200:
#         print('Failed to upload zip file to Rocket.Chat. Error:', upload_response.content)
#         return
#
#     # Get the uploaded file details
#     file_id = upload_response.json().get('file').get('_id')
#     file_url = f"{server_url}file-upload/{file_id}"
#
#     # Specify the message content
#     message = 'Hello, this is a test message with a zip file attachment.'
#
#     # Send the message with the zip file attachment to the channel
#     message_payload = {
#         "channel": team_room,
#         "text": message,
#         "attachments": [{"title": file_name, "title_link": file_url}]
#     }
#     message_response = requests.post(
#         f"{server_url}api/v1/chat.postMessage",
#         headers={"X-Auth-Token": token},
#         json=message_payload
#     )
#     if message_response.status_code != 200:
#         print('Failed to send message to Rocket.Chat. Error:', message_response.content)
#         return
#
#     print('Zip file uploaded and message sent successfully.')
#
#
# # Hook to display a summary after all tests have finished
# def pytest_terminal_summary(terminalreporter):
#     # Specify the folder path and zip file path
#     folder_path = 'Reports'  # Replace with the actual folder path
#     zip_file_path = 'Report'  # Replace with the desired zip file path
#
#     # Zip the folder
#     zip_folder(folder_path, zip_file_path)
#
#     send_to_channel(zip_file_path)


# Optionally, you can also capture the stdout and stderr of each test case
# @pytest.hookimpl(tryfirst=True)
# def pytest_runtest_protocol(item, nextitem):
#     # Capture stdout and stderr for each test case
#     capture = pytest.stdout_capture.getcapture(item.config)
#     outcome = yield
#     capture.reset()
#

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     setattr(item, "rep_" + report.when, report)


# @pytest.fixture(autouse=True)
# def after_test(request):
#     # Connect to Rocket.Chat instance
#     rocket = RocketChat('riddhi@addwebsolution.in', 'Riddhi_chat_123', server_url='https://chat.addwebsolution.in/')
#
#     # Set the channel or user to whom you want to send the test report
#     team_room = 'team-circuit-breakers'
#
#     yield
#     report = request.node.rep_call
#     test_case_name = request.node.name
#     test_case_print_statements = request.node.user_properties
#     if report.failed:
#         print(f"Test case '{test_case_name}' failed!")
#         message = f"Test case '{test_case_name}' failed!"
#         # Send the message to the channel
#         response = rocket.chat_post_message(room_id=team_room, text=message)
#         print(response.content)
#
#     elif report.passed:
#         print(f"Test case '{test_case_name}' passed!")
#         # if test_case_print_statements:
#         #     print(f"Print statements in '{test_case_name}':")
#         #     for statement in test_case_print_statements:
#         #         print(statement)
#         message = f"Test case '{test_case_name}' passed!"
#         # Send the message to the channel
#         response = rocket.chat_post_message(room_id=team_room, text=message)
#         print(response.content)
#
#     elif report.skipped:
#         print(f"Test case '{test_case_name}' skipped!")
#         message = f"Test case '{test_case_name}' skipped!"
#         # Send the message to the channel
#         response = rocket.chat_post_message(room_id=team_room, text=message)
#         print(response.content)
#
#     elif report.outcome == "error":
#         print(f"Test case '{test_case_name}' encountered an error!")
#         message = f"Test case '{test_case_name}' encountered an error!"
#         # Send the message to the channel
#         response = rocket.chat_post_message(room_id=team_room, text=message)
#         print(response.content)


#
# def pytest_terminal_summary(terminalreporter, exitstatus, config):
#     # send_to_channel()
#     print(my_variable)


# def zip_folder(folder_path, zip_file_path):
#     shutil.make_archive(zip_file_path, 'zip', folder_path)
#
#
# def send_email(sender, password, receiver, subject, body, attachment_path):
#
#     msg = MIMEMultipart()
#     msg['From'] = sender
#     msg['To'] = receiver
#     msg['Subject'] = subject
#     attachment_path = attachment_path + ".zip"
#
#     # Attach the zip file
#     attachment = open(attachment_path, 'rb')
#     part = MIMEBase('application', 'octet-stream')
#     part.set_payload((attachment).read())
#     encoders.encode_base64(part)
#     part.add_header('Content-Disposition', "attachment; filename= %s" % attachment_path)
#     msg.attach(part)
#
#     msg.attach(MIMEText(body, 'plain'))
#
#     # with open(attachment_path, 'rb') as attachment:
#     #     part = MIMEApplication(attachment.read())
#     #     part.add_header('Content-Disposition', 'attachment', filename= "Clock-in and Clock-out test report")
#     #     msg.attach(part)
#
#     # with open(attachment_path, 'rb') as attachment:
#     #     part = MIMEApplication(attachment.read())
#     #     part.add_header('Content-Disposition', 'attachment', filename= attachment_path_2)
#     #     msg.attach(part)
#
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(sender, password)
#     server.send_message(msg)
#     server.quit()
#
#
# def pytest_terminal_summary(terminalreporter, exitstatus, config):
#
#     # Specify the folder path and zip file path
#     folder_path = 'Reports'  # Replace with the actual folder path
#     zip_file_path = 'Report'  # Replace with the desired zip file path
#
#     # Zip the folder
#     zip_folder(folder_path, zip_file_path)
#
#     sender = 'puvesh2002@gmail.com'
#     password = 'oiuvigginniypkma'
#     receiver = 'psultan2002@gmail.com'
#     subject = 'Test Report'
#     body = 'Please find the attached test report.'
#
#     # attachment_path = 'Reports/Final_Report.html'
#     # attachment_path_2 = 'Reports/assets/style.css'
#
#     send_email(sender, password, receiver, subject, body, zip_file_path)
#

def pytest_html_report_title(report):
    report.title = "Automation Report"



# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     screen_file = ''
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#
#     if report.when == "call":
#         # always add url to report
#         # extra.append(pytest_html.extras.url("http://www.addwebsolution.com/"))
#         xfail = hasattr(report, "wasxfail")
#         if report.failed or xfail and "page" in item.funcargs:
#             page = item.funcargs["page"]
#             screenshot_dir = Path("screenshots")
#             screenshot_dir.mkdir(exist_ok=True)
#             screen_file = str(screenshot_dir / f"{slugify(item.nodeid)}.png")
#             page.screenshot(path=screen_file)
#
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             extra.append(pytest_html.extras.png(screen_file))
#         report.extra = extra
#
#         #     # only add additional html on failiur
#         #     report_directory = os.path.dirname(item.config.option.htmlpath)
#         #
#         #     file_name = report.nodeid.replace("::", "_") + ".png"
#         #     destination_file = os.path.join(report_directory, file_name)
#         #     driver.save_screenshot(destination_file)
#         #     # _capture_screenshot(file_name)
#         #     if file_name:
#         #         html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#         #                 'onclick="window.open(this.src)" align="right"/></div>'%file_name
#         #         # only add additional html on failure
#         #     extra.append(pytest_html.extras.html(html))
#         # report.extra = extra
#
#
# # def _capture_screenshot(name):
# #     driver.get_screenshot_as_file(name)
#

# def pytest_collection_modifyitems(config, items):
#     # Define the desired sequence of test files
#     desired_sequence = ['login_page_validation_test.py', 'projects_page_validation_test.py',
#                         'tasks_page_validations_test.py', 'time_log_page_validation_test.py']
#
#     # Sort the test items based on their position in the desired sequence
#     items.sort(key=lambda item: (desired_sequence.index(item.nodeid.split("::")[0]), item.nodeid))
