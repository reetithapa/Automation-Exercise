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
    driver.maximize_window()
    return driver

def checkout(driver):
    driver.get("https://automationexercise.com/")

    assert driver.find_element(By.CLASS_NAME, "container").is_displayed()
    print("Home page is visible successfully")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/products']"))
    )

    driver.find_element(By.XPATH, "//a[@href='/products']").click()

    #assert "products" in driver.current_url, "User is not navigated to Product page"

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/product_details/1']")))
    time.sleep(5)

    driver.find_element(By.XPATH, "//a[@href='/product_details/1']").click()

    driver.find_element(By.XPATH, "//a[@href='#reviews']").is_displayed()

    driver.find_element(By.ID, "name").send_keys("hello")
    driver.find_element(By.ID, "email").send_keys("hello@gmail.com")
    driver.find_element(By.ID, "review").send_keys("Add reviews")
    driver.find_element(By.ID, "button-review").click()

    assert driver.find_element(By.XPATH, "//span[text()='Thank you for your review.']").is_displayed()

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



