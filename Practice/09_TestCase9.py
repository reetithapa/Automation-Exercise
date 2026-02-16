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

    #assert driver.find_element(By.CLASS_NAME, "container").is_displayed()
    print("Home page is visible successfully")

    #wait = WebDriverWait(driver, 10)
    #products = wait.until(
      #  EC.element_to_be_clickable((By.XPATH, "//a[@href='/products']")) )
    driver.find_element(By.XPATH, "//a[@href='/products']").click()

   # driver.execute_script("arguments[0].scrollIntoView(true);", products)

    assert "/products" in driver.current_url, "User is not navigated to product page"
    print("user is navigated to ALL PRODUCTS page successfully")

    driver.find_element(By.ID, "search_product").send_keys("Tshirt")
    driver.find_element(By.CSS_SELECTOR, "i.fa.fa-search").click()

    driver.find_element(By.XPATH, "//h2[text()='Searched Products']").is_displayed()
    print(" 'SEARCHED PRODUCTS' is visible")

    product_list = driver.find_elements(By.CLASS_NAME, "features_items")

    assert len(product_list)>0
    print("Search products is visible successfully")


def automation_exercise():
    driver = setup_driver()

    try:
        products(driver)

    except Exception as e:
        print("Test failed", str(e))

    finally:
        driver.quit()
        print("Test completed")

if __name__ == "__main__":
    automation_exercise()