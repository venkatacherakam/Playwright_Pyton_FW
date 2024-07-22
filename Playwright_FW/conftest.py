from datetime import datetime
from pathlib import Path
import os
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect, Error
from slugify import slugify

SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


@pytest.fixture(scope="function")
def setup(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://prokarma.myfreshworks.com/")
    yield page
    context.close()
    browser.close()


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     screen_file = ''
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         xfail = hasattr(report, "wasxfail")
#         if report.failed or xfail and "page" in item.funcargs:
#             page = item.funcargs["page"]
#             screenshot_dir = Path("screenshots")
#             screenshot_dir.mkdir(exist_ok=True)
#             screen_file = str(screenshot_dir / f"{slugify(item.nodeid)}.png")
#             page.screenshot(path=screen_file)
#
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             #add the screenshots to the html report
#             extra.append(pytest_html.extras.png(screen_file))
#         report.extra = extra

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call="call"):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Check if the test failed
    if rep.when == call and rep.failed:
        # Get a screenshot using Playwright
        try:
            screenshot_path = os.path.join(SCREENSHOT_DIR,
                                           f"{item.name}_{datetime.now().strftime('%Y%m%d%H%M%S%f')}.png")
            item.funcargs['playwright_context'].page.screenshot(path=screenshot_path)
            print(f"\nScreenshot saved: {screenshot_path}")
        except Error as e:
            print(f"\nFailed to take screenshot: {str(e)}")
