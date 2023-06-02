from pathlib import Path

import pytest
import slugify as slugify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


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

def pytest_html_report_title(report):
    report.title = "Automation Report"

