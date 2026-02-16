from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome (service = service)
    return driver

def login_signup(driver):
    driver.maximize_window()
    driver.get("https://www.automationexercise.com/")
    print("Website launched")

    assert driver.find_element(By.XPATH, "//img[@alt='Website for automation practice']").is_displayed()
    print("Displayed")

    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    assert "New User Signup!" in driver.find_element(By.XPATH, "//h2[text()='New User Signup!']").text
    print("'New User Signup!' is visible")

    driver.find_element(By.NAME, "name").send_keys("Hello world")
    email = f"test_{int(time.time())}@gmail.com"
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys(email)

    driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()
    print("Signup successful")

    WebDriverWait(driver, 15).until(
        EC.url_contains("/signup")
    )

    assert "/signup" in driver.current_url, "signup unsuccessful"
    print("Success")

    assert driver.find_element(By.XPATH, "//h2[contains(., 'Enter Account Information')]").is_displayed()
    print("'ENTER ACCOUNT INFORMATION' is visible")

    driver.find_element(By.ID, "id_gender2").click()
    driver.find_element(By.ID, "password").send_keys("hello321")

    Select(driver.find_element(By.ID, "days")).select_by_value("14")
    Select(driver.find_element(By.ID, "months")).select_by_value("12")
    Select(driver.find_element(By.ID, "years")).select_by_value("2020")

    driver.find_element(By.ID, "newsletter").click()
    driver.find_element(By.ID, "optin").click()

    driver.find_element(By.ID, "first_name").send_keys("Hello")
    driver.find_element(By.ID, "last_name").send_keys("world")
    driver.find_element(By.ID, "address1").send_keys("Kathmandu")

    Select(driver.find_element(By.ID, "country")).select_by_visible_text("India")

    driver.find_element(By.ID, "state").send_keys("UP")
    driver.find_element(By.ID, "city").send_keys("abc")
    driver.find_element(By.ID, "zipcode").send_keys("12345")
    driver.find_element(By.ID, "mobile_number").send_keys("100000000")

    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
    print("Account created")

    #assert driver.find_element(By.XPATH, "//h2[text()='Account Created!']").is_displayed()
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

    #assert driver.find_element(By.PARTIAL_LINK_TEXT, "Logged in as").is_displayed()

    driver.find_element(By.XPATH, "//a[@href='/delete_account']").click()
    print("Account deleted")

    #assert driver.find_element(By.XPATH, "//h2[text()='Account Deleted!']").is_displayed()
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

def automation_exercise():
    driver = setup_driver()

    try:
        login_signup(driver)
        time.sleep(10)

    except Exception as e:
        print("Test Failed", str(e))

    finally:
        driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    automation_exercise()




