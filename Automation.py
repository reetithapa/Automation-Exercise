from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import Workbook
import platform
import os

if not os.path.exists("screenshots"):
    os.mkdir("screenshots")

element_map = {
    "user-name": "username field",
    "password": "password field",
    "login-button": "login button",
    "error-message-container": "error message"
}

test_cases = [
    {"username": "standard_user", "password": "wrong_password", "expected": "Epic sadface: Username and password do not match any user in this service"},
    {"username": "locked_out_user", "password": "secret_sauce", "expected": "Epic sadface: Sorry, this user has been locked out."},
    {"username": "standard_user", "password": "secret_sauce", "expected": "Redirected to Inventory Page"}
]

wb = Workbook()
ws = wb.active
ws.append(["Test Case ID", "Steps to Reproduce", "Expected Result", "Actual Result", "Environment", "Screenshot"])

for idx, test in enumerate(test_cases, 1):
    test_case_id = f"TC_{idx:03}"
    steps = []
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://www.saucedemo.com")
        steps.append(f"Open {"https://www.saucedemo.com"}")

        driver.find_element(By.ID, "user-name").send_keys(test["username"])
        steps.append(f'Enter "{test["username"]}" in {element_map["user-name"]}')

        driver.find_element(By.ID, "password").send_keys(test["password"])
        steps.append(f'Enter "{test["password"]}" in {element_map["password"]}')

        driver.find_element(By.ID, "login-button").click()
        steps.append(f'Click the {element_map["login-button"]}')

        try:
            error_message_element = WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
            )
            actual_result = error_message_element.text
        except TimeoutException:
            actual_result = "No error message displayed"

        capabilities = driver.capabilities
        environment = f"Browser: {capabilities['browserName']} {capabilities['browserVersion']}, OS: {platform.system()} {platform.release()}"

        screenshot_file = ""
        if actual_result != test["expected"]:
            screenshot_file = f"screenshots/bug_{idx}.png"
            driver.save_screenshot(screenshot_file)
            print(f"Bug detected for username={test['username']}, screenshot saved as {screenshot_file}")

        ws.append([
            test_case_id,
            "\n\n".join([f"{i + 1}. {s}" for i, s in enumerate(steps)]),
            test["expected"],
            actual_result,
            environment,
            screenshot_file
        ])

    finally:
        driver.quit()

wb.save("bug_reports.xlsx")
print("Bug reports saved to bug_reports.xlsx with screenshots!")
