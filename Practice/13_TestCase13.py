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


def products(driver):
    driver.get("https://automationexercise.com/")

    assert driver.find_element(By.CLASS_NAME, "container").is_displayed()
    print("Home page is visible successfully")

    driver.find_element(By.XPATH, "//a[@href='/product_details/1']").click()

    assert "/product_details/1" in driver.current_url, "Not redirected to product details page"
    print("User redirected to product details page")

    quantity = driver.find_element(By.ID, "quantity")
    quantity.clear()
    quantity.send_keys("4")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default.cart").click()

    driver.find_element(By.XPATH, "//a[@href='/view_cart']").click()
    print("Cart page displayed successfully")

    wait = WebDriverWait(driver, 10)

    cart_quantity = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.disabled"))).text
    assert cart_quantity == 4, f"Expected quantity is 4 but found{cart_quantity}"
    print("Product is displayed in cart page with exact quantity")

def automation_exercise():
    driver= setup_driver()

    try:
        products(driver)

    except Exception as e:
        print("Test failed", str(e))

    finally:
        driver.quit()
        print("Test completed")

if __name__ == "__main__":
    automation_exercise()

