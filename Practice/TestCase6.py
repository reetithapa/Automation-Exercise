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

def contact_us(driver):
    driver.get("https://www.automationexercise.com/")

    wait = WebDriverWait(driver, 10)

    assert driver.find_element(By.CLASS_NAME, "container").is_displayed()
    print("Home page is displayed")

    driver.find_element(By.LINK_TEXT, "Contact us").click()
    print("Contact us")

    assert driver.find_element(By.XPATH, "//h2[text()='Get In Touch']").is_displayed(), "Get In Touch is not visible"
    print("'GET IN TOUCH' is visible")

    driver.find_element(By.NAME, "name").send_keys("hello")
    driver.find_element(By.NAME, "email").send_keys("hellowwww@gmail.com")
    driver.find_element(By.NAME, "subject").send_keys("automation")
    driver.find_element(By.NAME, "message").send_keys("automation testing using selenium")
    #driver.find_element(By.NAME, "upload_file").send_keys(r"C:\Users\\Desktop\automation\automation.exe")

    driver.find_element(By.NAME, "submit").click()

    alert = driver.switch_to.alert
    alert.accept()

    assert driver.find_element(By.CSS_SELECTOR, "div.status.alert.alert-success").is_displayed()
    print("'Success! Your details have been submitted successfully.' is visible")

    driver.find_element(By.XPATH, "//span[normalize-space()='Home']").click()
    print("Home clicked successfully")

    wait.until(EC.url_to_be("https://automationexercise.com/"))
    assert driver.current_url == "https://automationexercise.com/"
    print("landed to home page successfully")

def automation():
    driver = setup_driver()

    try:
        contact_us(driver)

    except Exception as e:
        print("Test failed", str(e))

    finally:
        driver.quit()
        print("Test completed")

if __name__ == "__main__":
    automation()