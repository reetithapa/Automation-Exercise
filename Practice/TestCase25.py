from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

def arrow_button(driver):
    driver.get("https://automationexercise.com/")

    assert driver.find_element(By.CLASS_NAME, "container").is_displayed()
    print("Home page is displayed")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    driver.find_element(By.XPATH, "//h2[text()='Subscription']").is_displayed()
    print("Subscription is displayed")

    driver.find_element(By.CSS_SELECTOR, "i.fa.fa-angle-up").click()

    assert driver.find_element(By.XPATH, "//h2[text()='Full-Fledged practice website for Automation Engineers']").is_displayed()
    print("Full-Fledged practice website for Automation Engineers is displayed")

def automation_exercise():
    driver = setup_driver()

    try:
        arrow_button(driver)

    except Exception as e:
        print("Test failed", str(e))

    finally:
        driver.quit()
        print("Test completed")

if __name__ == "__main__":
    automation_exercise()



