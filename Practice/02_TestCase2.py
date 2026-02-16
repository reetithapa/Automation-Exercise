from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service = service)
    return driver

def login(driver):
    driver.get("https://www.automationexercise.com/")
    assert driver.find_element(By.CLASS_NAME, "container").is_displayed()
    print("Home page is visible successfully")

    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    assert "Login to your account" in driver.find_element(By.XPATH, "//h2[text()='Login to your account']").text
    print("Login to your account is visible")

    driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']").send_keys("Test.2@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']").send_keys("Test2")

    driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()

    #assert driver.find_element(By.ID, "slider-carousel").is_displayed()
    print("Logged in successfully")

    driver.find_element(By.XPATH, "//a[@href='/delete_account']").click()

    assert driver.find_element(By.XPATH, "//b[text()='Account Deleted!']").is_displayed()
    print("Account deleted successfully")

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







