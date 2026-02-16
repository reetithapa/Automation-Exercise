from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def go_to_checkout(driver):
    driver.find_element(By.ID, "checkout").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/checkout-step-one.html"))
    print("Open Checkout Page")

def enter_checkout_details(driver):
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Mayor")
    driver.find_element(By.ID, "postal-code").send_keys("abc123")

    driver.find_element(By.ID, "continue").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/checkout-step-two.html"))
    print("Details Entered")

    driver.find_element(By.ID, "finish").click()
    assert "/checkout-complete.html" in driver.current_url, "Not redirected to checkout complete page"
    print("Redirected to Checkout Complete Page")

    driver.find_element(By.CLASS_NAME, "complete-header").is_displayed()
    driver.find_element(By.ID, "back-to-products").click()

    assert "/inventory.html" in driver.current_url, "Not redirected to inventory page"
    print("Redirected to Home page")
