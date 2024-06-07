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
driver.get("https://orteil.dashnet.org/cookieclicker/")


cookie_id = 'bigCookie'
cookies_count_id = 'cookies'
product_price_prefix = 'productPrice'
product_prefix = 'product'


# wait for the element 5s to be present in the DOM
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

# get the element by class XPATH
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()



# wait for the element 5s to be present in the DOM
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

# get the element by class name
cookie = driver.find_element(By.ID, cookie_id)

time.sleep(10)



while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_count_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))
    print(cookies_count)

    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")
        
        if not product_price.isdigit():
            continue
        
        product_price = int(product_price)
        
        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break