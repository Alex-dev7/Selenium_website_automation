from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

# get the website
driver.get("https://www.google.com")

# wait for the element 5s to be present in the DOM
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

# get the element by class name
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
# clear the input field first
input_element.clear()
# send keys to the input element
input_element.send_keys("Hello World" + Keys.ENTER)


# wait for the element 5s to be present in the DOM
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Hello World"))
)
# find the link by partial text and click it
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Hello World")
link.click()


time.sleep(10)

driver.quit()