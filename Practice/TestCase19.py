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

    driver.find_element(By.XPATH, "//a[@href='/products']").click()

    assert driver.find_elements(By.CLASS_NAME, "brands-name"), "Brand products are not displayed"

    time.sleep(10)
    driver.find_element(By.XPATH, "//a[@href='/brand_products/H&M']").click()

    assert "brand_products/H&M" in driver.current_url, "User is not navigated to brand page"

    assert driver.find_element(By.CSS_SELECTOR, "h2.title.text-center").is_displayed(), "Brand products are not displayed"

    driver.find_element(By.XPATH, "//a[@href='/brand_products/Polo']").click()

def automation_test():
    driver = setup_driver()

    try:
        checkout(driver)

    except Exception as e:
        print("automation test failed", str(e))

    finally:
        driver.quit()
        print("automation test completed")

if __name__ == "__main__":
    automation_test()