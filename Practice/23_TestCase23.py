from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

def checkout(driver):
    driver.get("https://automationexercise.com/")

    assert driver.find_element(By.CLASS_NAME, "container").is_displayed()
    print("Home page is visible successfully")

    driver.find_element(By.XPATH, "//a[@href='/login']").click()

    assert "New User Signup!" in driver.find_element(By.XPATH, "//h2[text()='New User Signup!']").text
    print("New user signup visible")

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

    # assert "Enter Account Information" in driver.find_element(By.XPATH, "//h2[contains(., 'Enter Account Information')]").text
    # print("Enter Account Information visible")

    driver.find_element(By.ID, "id_gender2").click()
    driver.find_element(By.ID, "password").send_keys("hello321")

    Select(driver.find_element(By.ID, "days")).select_by_value("14")
    Select(driver.find_element(By.ID, "months")).select_by_value("12")
    Select(driver.find_element(By.ID, "years")).select_by_value("2020")

    driver.find_element(By.ID, "newsletter").click()
    driver.find_element(By.ID, "optin").click()

    driver.find_element(By.ID, "first_name").send_keys("Hello")
    driver.find_element(By.ID, "last_name").send_keys("world")

    registration_address = driver.find_element(By.ID, "address1").send_keys("Kathmandu")

    country = Select(driver.find_element(By.ID, "country")).select_by_visible_text("India")

    state = driver.find_element(By.ID, "state").send_keys("UP")
    city = driver.find_element(By.ID, "city").send_keys("abc")
    zipcode = driver.find_element(By.ID, "zipcode").send_keys("12345")
    mobile_number = driver.find_element(By.ID, "mobile_number").send_keys("100000000")

    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
    print("Account created")

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary")))

    # assert driver.find_element(By.XPATH, "//h2[text()='Account Created!']").is_displayed()
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    ("Home page is visible successfully")

    time.sleep(10)

    driver.find_element(By.XPATH, "//a[text()='Add to cart']").click()
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success.close-modal.btn-block").click()

    driver.find_element(By.XPATH, "//a[@href='/view_cart']").click()
    assert "view_cart" in driver.current_url, "User not navigated to cart page"

    driver.find_element(By.CSS_SELECTOR, "a.btn.btn-default.check_out")

    delivery_address = driver.find_elements(By.ID, "address_delivery").is_displayed()
    print(delivery_address)

    billing_address = driver.find_element(By.ID, "address_invoice").is_displayed()
    print(billing_address)

    assert registration_address in delivery_address
    assert country in delivery_address
    assert state in delivery_address
    assert city in delivery_address
    assert zipcode in delivery_address
    print("Delivery address verified")

    assert registration_address in billing_address
    assert country in billing_address
    assert state in billing_address
    assert city in billing_address
    assert zipcode in billing_address
    print("Billing address verified")

    driver.find_element(By.XPATH, "//a[@href='/delete_account']").click()

    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

def automation_exercise():
    driver = setup_driver()

    try:
        checkout(driver)

    except Exception as e:
        print("Test failed", str(e))

    finally:
        print("Test completed")

if __name__ == "__main__":
    automation_exercise()
