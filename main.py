from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request

NUM_PAGES = int(input("Enter number of pages to scrape: "))
URL = input("Enter URL of GettyImages search: ")
driver = webdriver.Chrome()
i = 0
for x in range(1, NUM_PAGES+1):
    page = f"{URL}&page={x}"
    driver.get(page)
    driver.implicitly_wait(2)
    print(f"page {x}")
    elements = driver.find_elements(By.CLASS_NAME, "MosaicAsset-module__thumb___yvFP5")
    for f, e in enumerate(elements):
        try:
            print(e.get_attribute("src"))
            urllib.request.urlretrieve(e.get_attribute('src'), f'images/img{i}.jpg')
            i += 1
        except Exception:
            elements = driver.find_elements(By.CLASS_NAME, "MosaicAsset-module__thumb___yvFP5")
            print(elements[f].get_attribute("src"))
            urllib.request.urlretrieve(elements[f].get_attribute('src'), f'images/img{i}.jpg')
            i += 1
