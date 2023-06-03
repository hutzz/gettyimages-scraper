from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import os

NUM_PAGES = int(input("Enter number of pages to scrape: "))
URL = input("Enter URL of GettyImages search: ")

if not os.path.exists('images'):
    os.makedirs('images')

driver = webdriver.Chrome()
i = 0
for x in range(1, NUM_PAGES+1):
    page = f"{URL}&page={x}"
    driver.get(page)
    driver.implicitly_wait(4)
    print(f"page {x}")
    elements = driver.find_elements(By.CLASS_NAME, "BLA_wBUJrga_SkfJ8won")
    for f, e in enumerate(elements):
        try:
            print(e.get_attribute("src"))
            urllib.request.urlretrieve(e.get_attribute('src'), f'images/img{i}.jpg')
            i += 1
        except Exception:
            elements = driver.find_elements(By.CLASS_NAME, "BLA_wBUJrga_SkfJ8won")
            print(elements[f].get_attribute("src"))
            urllib.request.urlretrieve(elements[f].get_attribute('src'), f'images/img{i}.jpg')
            i += 1
