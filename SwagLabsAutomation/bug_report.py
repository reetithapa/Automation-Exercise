from openpyxl import Workbook
import platform
import os

if not os.path.exists("screenshots"):
    os.mkdir("screenshots")

if not os.path.exists("reports"):
    os.mkdir("reports")

class BugReport:
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append([
            "Test Case ID",
            "Steps to Reproduce",
            "Expected Result",
            "Actual Result",
            "Environment",
            "Screenshot"
        ])

    def add_result(self, driver, context, screenshot_name=None):
        capabilities = driver.capabilities
        environment = (
            f"Browser: {capabilities['browserName']} {capabilities['browserVersion']}, "
            f"OS: {platform.system()} {platform.release()}"
        )

        screenshot_path = ""
        if screenshot_name:
            screenshot_path = f"screenshots/{screenshot_name}"
            driver.save_screenshot(screenshot_path)

        self.ws.append([
            context.test_case_id,
            "\n".join([f"{i+1}. {s}" for i, s in enumerate(context.steps)]),
            context.expected,
            context.actual,
            environment,
            screenshot_path
        ])

    def save(self):
        self.wb.save("reports/bug_reports.xlsx")
