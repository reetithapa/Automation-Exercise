from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver1 = webdriver.Chrome()
driver1.get("https://automationexercise.com/")

driver1.find_element(By.XPATH, "//a[@href='/login']")
#assert "/login" in driver1.current_url, "User not redirected to login page"

driver1.find_element(By.NAME, "email").send_keys("Test.1@gmail.com")
driver1.find_element(By.NAME, "password").send_keys("Test1")
driver1.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()
time.sleep(3)

assert driver1.current_url == "https://automationexercise.com/", "Login not successful"
print("Login successful")
time.sleep(2)

driver1.find_element(By.CSS_SELECTOR, "a.btn.btn-default.add-to-cart").click()
driver1.find_element(By.CSS_SELECTOR, "button.btn.btn-success.close-modal.btn-block").click()
time.sleep(2)


driver2 = webdriver.Chrome()
driver2.get("https://automationexercise.com/")

driver2.find_element(By.XPATH, "//a[@href='/login']")
assert "/login" in driver1.current_url, "User not redirected to login page"

driver2.find_element(By.NAME, "email").send_keys("Test.2@gmail.com")
driver2.find_element(By.NAME, "password").send_keys("Test2")
driver2.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()
time.sleep(3)

assert driver2.current_url == "https://automationexercise.com/", "Login not successful"
print("Login successful")
time.sleep(2)

driver2.find_element(By.CSS_SELECTOR, "a.btn.btn-default.add-to-cart").click()
driver2.find_element(By.CSS_SELECTOR, "button.btn.btn-success.close-modal.btn-block").click()
time.sleep(2)


driver1.find_element(By.XPATH, "//a[@href='/view_card']").click()
cart_items_Test1=[item.text for item in driver1.find_element(By.ID, "cart_items")]

driver2.find_element(By.XPATH, "//a[@href='/view_card']").click()
cart_items_Test2=[item.text for item in driver2.find_element(By.ID, "cart_items")]

assert "Product1" in cart_items_Test1 and "Product2" not in cart_items_Test1
assert "Product2" in cart_items_Test2 and "Product1" not in cart_items_Test2

print("Test passed")

driver1.quit
driver2.quit
