from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time


web = 'https://www.audible.com/search'

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

driver.get(web)

products = driver.find_elements(by='xpath', value='//li[contains(@class, "productListItem")]')

book_title = []
book_author = []
book_length = []

for product in products:
    book_title.append(product.find_element(by='xpath', value='.//h3[contains(@class, "bc-heading")]').text)
    book_author.append(product.find_element(by='xpath', value='.//li[contains(@class, "authorLabel")]').text)
    book_length.append(product.find_element(by='xpath', value='.//li[contains(@class, "runtimeLabel")]').text)

# time.sleep(10)

driver.quit()

# create a dataframe
df_books  = pd.DataFrame({
    'title': book_title,
    'author': book_author,
    'length': book_length
})

# save the dataframe to a csv file
df_books.to_csv('books.csv', index=False)

# //li[contains(@class, "productListItem")]
# //h3[contains(@class, "bc-heading")]
# //li[contains(@class, "authorLabel")]
# //li[contains(@class, "runtimeLabel")]

