from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

def cart(driver):
    driver.get("https://automationexercise.com/")

    assert driver.find_element(By.CLASS_NAME, "container").is_displayed()
    print("Home page is visible successfully")

    driver.find_element(By.LINK_TEXT, "Cart").click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    assert driver.find_element(By.XPATH, "//h2[text()='Subscription']").is_displayed()
    print("'SUBSCRIPTION' is displayed")

    driver.find_element(By.ID, "susbscribe_email").send_keys("abc@gmail.com")
    driver.find_element(By.ID, "subscribe").click()

    success_msg = driver.find_element(By.CSS_SELECTOR, "div.alert-success.alert")
    assert success_msg.is_displayed()
    assert success_msg.text == "You have been successfully subscribed!", "Subscription failed"
    print("'You have been successfully subscribed!' is visible")

def automation_exercise():
    driver = setup_driver()

    try:
        cart(driver)

    except Exception as e:
        print("Test failed", str(e))
    finally:
        driver.quit()
        print("Test completed")

if __name__ == "__main__":
    automation_exercise()

