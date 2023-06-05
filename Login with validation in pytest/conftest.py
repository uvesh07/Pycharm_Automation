import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from rocketchat_API.rocketchat import RocketChat
import requests

message = "This is for testing purpose."


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
    global message

    outcome = call.excinfo is None

    # Determine the status message based on the outcome
    status = "Pass" if outcome else "Fail" if call.excinfo is not None else "Error"

    # Get the test case name
    test_case_name = item.nodeid

    # Get the test case execution time
    execution_time = call.duration

    # Print or process the collected information as per your requirement
    message += f"Test Case: {test_case_name} \n"
    message += f"Status: {status}\n"
    message += f"Execution Time: {execution_time} seconds \n"

    # print(message)


def send_to_channel():
    global message
    # Connect to Rocket.Chat instance
    rocket = RocketChat('riddhi@addwebsolution.in', 'Riddhi_chat_123', server_url='https://chat.addwebsolution.in/')

    # Set the channel or user to whom you want to send the test report
    team_room = 'team-circuit-breakers'

    # Specify the path to your test report file
    # test_report_path = 'Reports/Final_Report.html'

    # Upload and send the test report
    # rocket.chat_upload_file(room_id=channel, file_path=test_report_path)

    # Specify the message content
    # message = 'Hello, this is a test message.'

    # print(message)

    # Send the message to the channel
    response = rocket.chat_post_message(room_id=team_room, text=message)
    # print(response.content)
    message = ""


# Hook to display a summary after all tests have finished
def pytest_terminal_summary(terminalreporter):
    send_to_channel()

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

#
# def send_email(sender, password, receiver, subject, body, attachment_path):
#
#     msg = MIMEMultipart()
#     msg['From'] = sender
#     msg['To'] = receiver
#     msg['Subject'] = subject
#
#     msg.attach(MIMEText(body, 'plain'))
#
#     with open(attachment_path, 'rb') as attachment:
#         part = MIMEApplication(attachment.read())
#         part.add_header('Content-Disposition', 'attachment', filename= "Clock-in and Clock-out test report")
#         msg.attach(part)
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
#     # Usage
#     sender = 'puvesh2002@gmail.com'
#     password = 'oiuvigginniypkma'
#     receiver = 'psultan2002@gmail.com'
#     subject = 'Test Report'
#     body = 'Please find the attached test report.'
#
#     attachment_path = 'Reports/Final_Report.html'
#     # attachment_path_2 = 'Reports/assets/style.css'
#
#     send_email(sender, password, receiver, subject, body, attachment_path)


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
