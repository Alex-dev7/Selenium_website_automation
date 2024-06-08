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

products = driver.find_elements(by='xpath', value='//li[contains(@class, "productListItem")]')

for product in products:
    print(product.find_element(by='xpath', value='.//h3[contains(@class, "bc-heading")]').text)
    product.find_element(by='xpath', value='.//li[contains(@class, "authorLabel")]').text
    product.find_element(by='xpath', value='.//li[contains(@class, "runtimeLabel")]').text

# time.sleep(10)

driver.quit()

# //li[contains(@class, "productListItem")]
# //h3[contains(@class, "bc-heading")]
# //li[contains(@class, "authorLabel")]
# //li[contains(@class, "runtimeLabel")]

