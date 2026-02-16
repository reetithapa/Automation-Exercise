from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

def products(driver):
    driver.get("https://automationexercise.com/")

    assert driver.find_element(By.CLASS_NAME, "container").is_displayed()
    print("Home page is visible successfully")

    time.sleep(4)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/products']")))

    driver.find_element(By.XPATH, "//a[@href='/products']").click()

    #driver.execute_script("arguments[0].scrollIntoView(true);", products)
    #product.click()

    assert "/products" in driver.current_url, "User is not navigated to product page"

    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)

    first_product = wait.until(
        EC.visibility_of_element_located((By.XPATH, "(//div[@class='productinfo text-center'])[1]"))
    )
    actions.move_to_element(first_product).perform()
    first_product.find_element(By.XPATH, ".//a[@class='btn btn-default add-to-cart']").click()

    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue Shopping']"))
    ).click()

    second_product = wait.until(
        EC.visibility_of_element_located((By.XPATH, "(//div[@class='productinfo text-center'])[2]"))
    )
    actions.move_to_element(second_product).perform()
    second_product.find_element(By.XPATH, ".//a[@class='btn btn-default add-to-cart']").click()

    driver.find_element(By.XPATH, "//u[text()='View Cart']").click()
    time.sleep(2)

    cart_items = driver.find_elements(By.XPATH, "//tr[contains(@id,'product-')]")
    assert len(cart_items) == 2, "All added products are not displayed in cart"
    print("Both products are added to cart")

    for item in cart_items:
        price = item.find_element(By.CLASS_NAME, "cart_price").text
        quantity = item.find_element(By.CLASS_NAME, "cart_quantity").text
        total = item.find_element(By.CLASS_NAME, "cart_total").text

        print("Price:", price, "Quantity:", quantity, "Total:", total)

        assert price != ""
        assert quantity == "1"
        assert total != ""

    print("Price, quantity and total verified")

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


