from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

def setup_driver():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

def purchase_order(driver):
    driver.get("https://automationexercise.com/")

    assert driver.find_element(By.CLASS_NAME, "container").is_displayed()
    print("Home page is displayed")

    driver.find_element(By.CSS_SELECTOR, "a.btn.btn-default.add-to-cart").click()
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success.close-modal.btn-block")
    driver.find_element(By.CSS_SELECTOR, "a.btn.btn-default.add-to-cart").click()

    driver.find_element(By.LINK_TEXT, "Cart").click()
    assert "view_cart" in driver.current_url, "User not navigated to cart page"
    print("User is navigated to cart page")

    driver.find_element(By.CSS_SELECTOR, "a.btn.btn-default.check_out").click()

    driver.find_element(By.XPATH, "//a[text()='Register / Login']").click()

    #assert "New User Signup!" in driver.find_element(By.XPATH, "//h2[text()='New User Signup!']").text
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

    Select(driver.find_element(By.ID, "country")).select_by_visible_text("India")

    driver.find_element(By.ID, "state").send_keys("UP")
    driver.find_element(By.ID, "city").send_keys("abc")
    driver.find_element(By.ID, "zipcode").send_keys("12345")
    driver.find_element(By.ID, "mobile_number").send_keys("100000000")

    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
    print("Account created")

    # assert driver.find_element(By.XPATH, "//h2[text()='Account Created!']").is_displayed()
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

    driver.find_element(By.XPATH, "//a[@href='/view_cart']").click()

    driver.find_element(By.CSS_SELECTOR, "a.btn.btn-default.check_out").click()

    driver.find_element(By.NAME, "message").send_keys("Hello Hello")

    driver.find_element(By.CSS_SELECTOR, "a.btn.btn-default.check_out").click()

    driver.find_element(By.NAME, "name_on_card").send_keys("Hello")
    driver.find_element(By.NAME, "card_number").send_keys("111")
    driver.find_element(By.NAME, "cvc").send_keys("123")
    driver.find_element(By.NAME, "expiry_month").send_keys_("02")
    driver.find_element(By.NAME, "expiry_year").send_keys("2026")
    driver.find_element(By.ID, "submit").click()

    driver.find_element(By.XPATH, "//a[@href='/download_invoice/3200']").click()
    driver.find_element(By.XPATH, "//a[@href='/']").click()

    driver.find_element(By.XPATH, "/delete_account").click()

def automation_exercise():
    driver = setup_driver()

    try:
        purchase_order(driver)

    except Exception as e:
        print("Test Failed", str(e))

    finally:
        print("Test completed")

if __name__ == "__main__":
    automation_exercise()














