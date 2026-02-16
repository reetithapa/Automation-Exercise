from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

def checkout(driver):
    driver.get("https://automationexercise.com/")

    assert driver.find_element(By.CLASS_NAME, "container").is_displayed()
    print("Home page is visible successfully")

    driver.find_element(By.LINK_TEXT, "Cart").click()
    print("Cart page is visible successfully")

    driver.find_element(By.LINK_TEXT, "here").click()

    assert "products" in driver.current_url, "Product page is not visible"

    driver.find_element(By.LINK_TEXT, "Add to cart").click()
    print("sucessfully added to cart")

    driver.find_element(By.XPATH, "//a[@href='/view_cart']").click()
    print("Cart page opened")

    assert "/view_cart" in driver.current_url, "Cart page is not visible"

    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
    print("proceed to checkout successful")

    driver.find_element(By.XPATH, "//a[@href='/login']").click()
    print("Proceed to login successful")

    driver.find_element(By.NAME, "name").send_keys("Hello world")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys("helloo112211@gmail.com")

    driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()
    print("Signup successful")

    WebDriverWait(driver, 15).until(
        EC.url_contains("/signup")
    )

    assert "/signup" in driver.current_url, "signup unsuccessful"
    print("Success")

    #assert "Enter Account Information" in driver.find_element(By.XPATH, "//h2[contains(., 'Enter Account Information')]").text
    # print("Enter Account Information visible")

    driver.find_element(By.ID, "id_gender1").click()
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

    # assert driver.find_element(By.XPATH, "//h2[text()='Account Created!']").is_displayed()
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()


def automation_exercise():
    driver = setup_driver()

    try:
        checkout(driver)

    except Exception as e:
        print("Test failed", str(e))

    finally:
        driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    automation_exercise()