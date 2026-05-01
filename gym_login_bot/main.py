from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os 

EMAIL = "your_name@test.com"
PASSWORD = "your_password"
GYM_URL = "https://appbrewery.github.io/gym/"
# keep browser open after program finishes
options = webdriver.FirefoxOptions()

try :
    driver = webdriver.Firefox()
except Exception as e :
    print(f"{e}: please run the code again!")
else:
    driver.get(GYM_URL)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # login button click
    log_in = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
    log_in.click()
    email = wait.until(ec.visibility_of_element_located((By.ID, "email-input")))
    email.clear()
    email.send_keys(EMAIL)
    password = driver.find_element(by=By.ID, value= "password-input")
    password.clear()
    password.send_keys(PASSWORD)
    submit = wait.until(ec.element_to_be_clickable((By.ID, "submit-button")))
    submit.click()
    # Wait for schedule page to load
    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

    driver.quit()