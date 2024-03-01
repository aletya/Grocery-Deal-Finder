from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.aldi.us/weekly-specials/our-weekly-ads/")
driver.maximize_window()
driver.implicitly_wait(10)
zipcode = 61801

#ezip = driver.find
driver.switch_to.frame(0)
enter_zip = driver.find_element(By.XPATH, '//*[@id="locationInput"]')
enter_zip.send_keys(zipcode)
enter_zip.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, '//*[@id="StoreListContainer"]/div[1]/div[3]/button').click()

driver.implicitly_wait(3)

map = driver.find_element(By.XPATH, '/html/body/div/div/div[5]/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/map')
area_elements = map.find_elements(By.TAG_NAME, "area")

item_names = []
item_prices = []
# item_sizes = []

count = 0
for area in area_elements:
    if (count%4 == 0):
        sentence = area.get_attribute("aria-label")
        #words = sentence.split('$')
        parts = sentence.split("$")
        if len(parts) >= 2:
        # Get the words after "See Details on" but before the "$"
            details = parts[0].split("See Details on ")[1]

            # Get the dollar value after "$"
            price = parts[1].strip()

            print("Details:", details)
            print("Price:", price)
            item_names.append(details)
            item_prices.append(price)
            print("\n")
        #print(sentence)
    count += 1

driver.close()