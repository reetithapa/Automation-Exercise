from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

def test_cases(driver):
    driver.get("https://www.automationexercise.com/")

    assert driver.find_element(By.CLASS_NAME, "container").is_displayed()
    print("Home page is displayed")

    driver.find_element(By.LINK_TEXT, "Test Cases").click()
    print("Test cases clicked")

    WebDriverWait(driver, 10).until(
        EC.url_contains("/test_case")
    )

    assert "/test_cases" in driver.current_url, "User is not navigated to test cases page"
    print("User is navigated to test cases page")

def automation():
    driver = setup_driver()

    try:
        test_cases(driver)

    except Exception as e:
        print("Test Case failed", str(e))

    finally:
        driver.quit()
        print("Test Case completed")

if __name__ == "__main__":
    automation()

