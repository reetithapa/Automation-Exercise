from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Locate username textbox
username = driver.find_element(By.ID, "user-name")

# Type into textbox
username.send_keys("standard_user")

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()




time.sleep(3)
driver.quit()

