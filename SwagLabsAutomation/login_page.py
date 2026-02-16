from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, context, username="standard_user", password="secret_sauce"):
    driver.get("https://www.saucedemo.com/")
    context.steps.append("Open Saucedemo website")

    driver.find_element(By.ID, "user-name").send_keys(username)
    context.steps.append(f"Enter username: {username}")

    driver.find_element(By.ID, "password").send_keys(password)
    context.steps.append("Enter password")

    driver.find_element(By.ID, "login-button").click()
    context.steps.append("Click Login button")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_container"))
    )
