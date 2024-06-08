from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


web = 'https://www.audible.com/search'

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

driver.get(web)

time.sleep(10)

driver.quit()