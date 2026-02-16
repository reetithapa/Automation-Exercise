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

    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

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
    driver.find_element(By.ID, "address1").send_keys("Kathmandu")

    Select(driver.find_element(By.ID, "country")).select_by_visible_text("India")

    driver.find_element(By.ID, "state").send_keys("UP")
    driver.find_element(By.ID, "city").send_keys("abc")
    driver.find_element(By.ID, "zipcode").send_keys("12345")
    driver.find_element(By.ID, "mobile_number").send_keys("100000000")

    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
    print("Account created")

    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
   #driver.find_element(By.CSS_SELECTOR, "input[data-qa='continue-button']").click()

    #driver.find_element(By.XPATH, "//a[text()='Logged in as hello']").is_displayed()

    product_ids = [1, 2, 3]

    for pid in product_ids:
        driver.find_element(
            By.XPATH,
            f"//a[@data-product-id='{pid}']"
        ).click()

        # handle popup if appears
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[text()='Continue Shopping']")
            )
        ).click()

    driver.find_element(By.XPATH, "//a[@href='/view_cart']").click()

    assert "view_cart" in driver.current_url, "User is not redirected to Cart page"

    driver.find_element(By.CSS_SELECTOR, "a.btn.btn-default.check_out").click()

    delivery_address =  driver.find_element(By.ID, "address_delivery").is_displayed()
    print(delivery_address)


def automation_exercise():
    driver = setup_driver()
    try:
        checkout(driver)

    except Exception as e:
        print("Test failed", str(e))

    finally:
        driver.quit()
        print("Test completed")

if __name__ == "__main__":
    automation_exercise()

