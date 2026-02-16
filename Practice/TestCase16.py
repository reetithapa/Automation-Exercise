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

    driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']").send_keys("goodday@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']").send_keys("G00dd@y")

    driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()
    print("Logged in successfully")

    product_ids = [1, 2, 3]

    for pid in product_ids:
        driver.find_element(
            By.XPATH,
            f"//a[@data-product-id='{pid}']"
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[text()='Continue Shopping']")
            )
        ).click()

    driver.find_element(By.XPATH, "//a[@href='/view_cart']").click()

    assert "view_cart" in driver.current_url, "User is not redirected to Cart page"

    driver.find_element(By.CSS_SELECTOR, "a.btn.btn-default.check_out").click()

    delivery_address = driver.find_element(By.ID, "address_delivery").is_displayed()
    print("delivery_address")

    driver.find_element(By.CLASS_NAME, "form-control").send_keys("If you would like to add a comment about your order, please write it in the field below.")
    driver.find_element(By.CSS_SELECTOR, "a.btn.btn-default.check_out").click()

    driver.find_element(By.NAME, "name_on_card").send_keys("Hello")
    driver.find_element(By.NAME, "card_number").send_keys("123")
    driver.find_element(By.NAME, "cvc").send_keys("111")
    driver.find_element(By.NAME, "expiry_month").send_keys("02")
    driver.find_element(By.NAME, "expiry_year").send_keys("2026")
    driver.find_element(By.ID, "submit").click()

    #driver.find_element(By.XPATH, "//p[contains()='Congratulations! Your order has been confirmed!']").is_displayed()

    driver.find_element(By.XPATH, "//a[@href='/delete_account']").click()
    driver.find_element(By.XPATH, "//a[@href='/']").click()

def automation_exercise():
    driver = setup_driver()
    try:
        login(driver)

    except Exception as e:
        print("Test failed", str(e))

    finally:
        driver.quit()
        print("Test completed")

if __name__ == "__main__":
    automation_exercise()

