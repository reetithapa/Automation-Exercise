from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def go_to_cart(driver, context):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    context.steps.append("Navigate to Cart page")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cart_contents_container"))
    )

def get_cart_products(driver, context):
    cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    cart_products = [item.text for item in cart_items]
    context.steps.append(f"Verify cart contains {len(cart_products)} products")
    return cart_products
