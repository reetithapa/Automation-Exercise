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

def login(driver):
    driver.get("https://www.automationexercise.com/")

    assert driver.find_element(By.CLASS_NAME, "container").is_displayed()
    print("Home page is displayed")

    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    driver.find_element(By.XPATH, "//h2[text()='New User Signup!']").is_displayed()
    print("Signup page is displayed")

    driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-name']").send_keys("hi")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys("john123john@gmail.com")

    driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()

    assert driver.find_element(By.XPATH, "//p[contains(text(), 'Email Address already exist!')]")
    print("Email address already exists")

def automation():
    driver = setup_driver()

    try:
        login(driver)

    except Exception as e:
        print("Test failed", str(e))

    finally:
        driver.quit()
        print("Test completed")

if __name__ == "__main__":
    automation()
