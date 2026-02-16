from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

def products(driver):
    driver.get("https://automationexercise.com/")

    assert driver.find_element(By.CLASS_NAME, "container").is_displayed()
    print("Home page is visible successfully")

    wait = WebDriverWait(driver, 10)
    products = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/products']"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", products)
    products.click()

    assert "/products" in driver.current_url, "User is not navigated to product page"

    driver.find_element(By.XPATH, "//h2[text()='All Products']").is_displayed()
    print("Product list is visible")

    driver.find_element(By.LINK_TEXT, "View Product").click()
    assert "/product_details/1" in driver.current_url, "User is not navigated to product page"

    driver.find_element(By.XPATH, "//h2[text()='Blue Top']").is_displayed()
    driver.find_element(By.XPATH, "//p[text()='Category: Women > Tops']").is_displayed()

    driver.find_element(By.XPATH, "//b[text()='Availability:']").is_displayed()
    print("Product detail is visible")

def product_page():
    driver = setup_driver()

    try:

        products(driver)

    except Exception as e:
        print("Test failed", str(e))

    finally:
        driver.quit()
        print("Test completed")

if __name__ == "__main__":
    product_page()
