from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

input_element = driver.find_element(By.CLASS_NAME, "")

time.sleep(10)

driver.quit()