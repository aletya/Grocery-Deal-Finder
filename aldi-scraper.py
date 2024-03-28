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


#original_window = driver.current_window_handle

driver.get("https://www.aldi.us/weekly-specials/our-weekly-ads/")
#new_window = driver.current_window_handle

# UNCOMMENT LINE BELOW IF WANTING TO HIDE WINDOW
#driver.set_window_position(-2000,-2000)


#driver.maximize_window()
driver.implicitly_wait(10)
#driver.switch_to.window(original_window)
#currentWindow = driver.windowHandle()

zipcode = input("Please enter your zip code: ")
#driver.switchTo().window(currentWindow)

#driver.switch_to.window(new_window)

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
# for future reference

# see details button XPath: /html/body/div/div/div[5]/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[3]/button[2]
# see_details = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[3]/button[2]")
# print(see_details.text)

dict = {}
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
            # item_names.append(details)
            # item_prices.append(price)
            dict[details] = price
            print("\n")
        #print(sentence)
    count += 1
    
sorted_dict = (sorted(dict.items(), key=lambda item: item[1]))
print(sorted_dict)

print("\n")

categories_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div/a[2]")

categories_button.click()

alcohol_button = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div/div/div/div[1]/a/div[1]/img")

alcohol_button.click()

element_container = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div[2]/div[2]")

alcohol_products = element_container.find_elements(By.CLASS_NAME, "ListingMini_ItemContainer")

for product in alcohol_products:
    title = product.find_element(By.CLASS_NAME, "ListingMini__Title-sc-18yoxcs-9").text
    price = product.find_element(By.CLASS_NAME, "sc-169d9gp-0-styled__Deal-kAKkkm").text
    validity_dates = product.find_element(By.CLASS_NAME, "ListingMini__Dates-sc-18yoxcs-14").text
    
    # title_element = product.find_element(By.CLASS_NAME, "ListingMini__Title-sc-18yoxcs-9")
    # title_spans = title_element.find_elements(By.TAG_NAME, "span")
    # title = title_spans[0].text + " " + title_spans[1].text if len(title_spans) > 1 else title_spans[0].text
    # price = product.find_element(By.CLASS_NAME, "sc-169d9gp-0-styled__Deal-kAKkkm").text
    # validity_dates = product.find_element(By.CLASS_NAME, "ListingMini__Dates-sc-18yoxcs-14").text
    
    if (title != ""):
        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Validity Dates: {validity_dates}")
        print("-" * 50)
        
###### NEW CATEGORY

categories_button.click()

chilled_button = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div/div/div/div[2]/a/div[1]/img")
chilled_button.click()

element_container = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div[2]/div[2]")

chilled_products = element_container.find_elements(By.CLASS_NAME, "ListingMini_ItemContainer")

for product in chilled_products:
    title = product.find_element(By.CLASS_NAME, "ListingMini__Title-sc-18yoxcs-9").text
    price = product.find_element(By.CLASS_NAME, "sc-169d9gp-0-styled__Deal-kAKkkm").text
    validity_dates = product.find_element(By.CLASS_NAME, "ListingMini__Dates-sc-18yoxcs-14").text
    
    # title_element = product.find_element(By.CLASS_NAME, "ListingMini__Title-sc-18yoxcs-9")
    # title_spans = title_element.find_elements(By.TAG_NAME, "span")
    # title = title_spans[0].text + " " + title_spans[1].text if len(title_spans) > 1 else title_spans[0].text
    # price = product.find_element(By.CLASS_NAME, "sc-169d9gp-0-styled__Deal-kAKkkm").text
    # validity_dates = product.find_element(By.CLASS_NAME, "ListingMini__Dates-sc-18yoxcs-14").text
    
    if (title != ""):
        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Validity Dates: {validity_dates}")
        print("-" * 50)
        
        
### NEW CATEGORY
categories_button.click()

meat_button = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div/div/div/div[3]/a/div[1]/img")
meat_button.click()

element_container = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div[2]/div[2]")

meat_products = element_container.find_elements(By.CLASS_NAME, "ListingMini_ItemContainer")

for product in meat_products:
    title = product.find_element(By.CLASS_NAME, "ListingMini__Title-sc-18yoxcs-9").text
    price = product.find_element(By.CLASS_NAME, "sc-169d9gp-0-styled__Deal-kAKkkm").text
    validity_dates = product.find_element(By.CLASS_NAME, "ListingMini__Dates-sc-18yoxcs-14").text
    
    # title_element = product.find_element(By.CLASS_NAME, "ListingMini__Title-sc-18yoxcs-9")
    # title_spans = title_element.find_elements(By.TAG_NAME, "span")
    # title = title_spans[0].text + " " + title_spans[1].text if len(title_spans) > 1 else title_spans[0].text
    # price = product.find_element(By.CLASS_NAME, "sc-169d9gp-0-styled__Deal-kAKkkm").text
    # validity_dates = product.find_element(By.CLASS_NAME, "ListingMini__Dates-sc-18yoxcs-14").text
    
    if (title != ""):
        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Validity Dates: {validity_dates}")
        print("-" * 50)

### NEW CATEGORY
categories_button.click()

produce_button = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div/div/div/div[4]/a/div[1]/img")
produce_button.click()

element_container = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div[2]/div[2]")

produce_products = element_container.find_elements(By.CLASS_NAME, "ListingMini_ItemContainer")

for product in produce_products:
    title = product.find_element(By.CLASS_NAME, "ListingMini__Title-sc-18yoxcs-9").text
    price = product.find_element(By.CLASS_NAME, "sc-169d9gp-0-styled__Deal-kAKkkm").text
    validity_dates = product.find_element(By.CLASS_NAME, "ListingMini__Dates-sc-18yoxcs-14").text
    
    # title_element = product.find_element(By.CLASS_NAME, "ListingMini__Title-sc-18yoxcs-9")
    # title_spans = title_element.find_elements(By.TAG_NAME, "span")
    # title = title_spans[0].text + " " + title_spans[1].text if len(title_spans) > 1 else title_spans[0].text
    # price = product.find_element(By.CLASS_NAME, "sc-169d9gp-0-styled__Deal-kAKkkm").text
    # validity_dates = product.find_element(By.CLASS_NAME, "ListingMini__Dates-sc-18yoxcs-14").text
    
    if (title != ""):
        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Validity Dates: {validity_dates}")
        print("-" * 50)

### NEW CATEGORY
categories_button.click()

nonfood_button = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div/div/div/div[5]/a/div[1]/img")
nonfood_button.click()

element_container = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div[2]/div[2]")

nonfood_products = element_container.find_elements(By.CLASS_NAME, "ListingMini_ItemContainer")

for product in nonfood_products:
    title = product.find_element(By.CLASS_NAME, "ListingMini__Title-sc-18yoxcs-9").text
    price = product.find_element(By.CLASS_NAME, "sc-169d9gp-0-styled__Deal-kAKkkm").text
    validity_dates = product.find_element(By.CLASS_NAME, "ListingMini__Dates-sc-18yoxcs-14").text
    
    # title_element = product.find_element(By.CLASS_NAME, "ListingMini__Title-sc-18yoxcs-9")
    # title_spans = title_element.find_elements(By.TAG_NAME, "span")
    # title = title_spans[0].text + " " + title_spans[1].text if len(title_spans) > 1 else title_spans[0].text
    # price = product.find_element(By.CLASS_NAME, "sc-169d9gp-0-styled__Deal-kAKkkm").text
    # validity_dates = product.find_element(By.CLASS_NAME, "ListingMini__Dates-sc-18yoxcs-14").text
    
    if (title != ""):
        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Validity Dates: {validity_dates}")
        print("-" * 50)
        
### NEW CATEGORY
categories_button.click()

dry_button = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div/div/div/div[6]/a/div[1]/img")
dry_button.click()

element_container = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div[2]/div[2]")

dry_products = element_container.find_elements(By.CLASS_NAME, "ListingMini_ItemContainer")

for product in dry_products:
    title = product.find_element(By.CLASS_NAME, "ListingMini__Title-sc-18yoxcs-9").text
    price = product.find_element(By.CLASS_NAME, "sc-169d9gp-0-styled__Deal-kAKkkm").text
    validity_dates = product.find_element(By.CLASS_NAME, "ListingMini__Dates-sc-18yoxcs-14").text
    
    # title_element = product.find_element(By.CLASS_NAME, "ListingMini__Title-sc-18yoxcs-9")
    # title_spans = title_element.find_elements(By.TAG_NAME, "span")
    # title = title_spans[0].text + " " + title_spans[1].text if len(title_spans) > 1 else title_spans[0].text
    # price = product.find_element(By.CLASS_NAME, "sc-169d9gp-0-styled__Deal-kAKkkm").text
    # validity_dates = product.find_element(By.CLASS_NAME, "ListingMini__Dates-sc-18yoxcs-14").text
    
    if (title != ""):
        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Validity Dates: {validity_dates}")
        print("-" * 50)


### NEW CATEGORY
categories_button.click()

frozen_button = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div/div/div/div[7]/a/div[1]/img")
frozen_button.click()

element_container = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div[2]/div[2]")

frozen_products = element_container.find_elements(By.CLASS_NAME, "ListingMini_ItemContainer")

for product in frozen_products:
    title = product.find_element(By.CLASS_NAME, "ListingMini__Title-sc-18yoxcs-9").text
    price = product.find_element(By.CLASS_NAME, "sc-169d9gp-0-styled__Deal-kAKkkm").text
    validity_dates = product.find_element(By.CLASS_NAME, "ListingMini__Dates-sc-18yoxcs-14").text
    
    # title_element = product.find_element(By.CLASS_NAME, "ListingMini__Title-sc-18yoxcs-9")
    # title_spans = title_element.find_elements(By.TAG_NAME, "span")
    # title = title_spans[0].text + " " + title_spans[1].text if len(title_spans) > 1 else title_spans[0].text
    # price = product.find_element(By.CLASS_NAME, "sc-169d9gp-0-styled__Deal-kAKkkm").text
    # validity_dates = product.find_element(By.CLASS_NAME, "ListingMini__Dates-sc-18yoxcs-14").text
    
    if (title != ""):
        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Validity Dates: {validity_dates}")
        print("-" * 50)
        

driver.close()