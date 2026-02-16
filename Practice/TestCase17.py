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

    driver.find_element(By.CSS_SELECTOR, "a.btn.btn-default.add-to-cart").click()

    driver.find_element(By.XPATH, "//a[@href='/view_cart']").click()

    assert "view_cart" in driver.current_url, "User is not redirected to Cart page"

    driver.find_element(By.CSS_SELECTOR, "i.fa.fa-times").click()

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
    driver = setup_driver()
    automation_exercise()

