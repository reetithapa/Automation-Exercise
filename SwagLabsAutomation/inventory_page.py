from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def list_product(driver, context):
    products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    context.steps.append(f"List all products ({len(products)} found)")
    return [p.text for p in products]

def open_each_product_and_add_to_cart(driver, context):
    added_products = []

    products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    for index in range(len(products)):
        products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        product_name = products[index].text

        context.steps.append(f"Open product: {product_name}")
        products[index].click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_details_container"))
        )

        driver.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()
        context.steps.append(f"Add product to cart: {product_name}")

        added_products.append(product_name)

        driver.find_element(By.ID, "back-to-products").click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_container"))
        )

    return added_products
