from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic
from dotenv import load_dotenv
import os
import json

#getting API key from env file
load_dotenv()
geolocator = GoogleV3(api_key=os.getenv("GOOGLE_MAPS_API_KEY"))

def get_location(address):
    location = geolocator.geocode(address)
    if location is None:
        print(address + " could not be found")
        return 90,90
    return location.latitude, location.longitude

def calculate_distance(address1, address2):
    location1 = get_location(address1)
    location2 = get_location(address2)
    return geodesic(location1, location2).kilometers

def get_deals(user_zip_code):
    # Initializes a selenium webdriver for Chrome
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox") # linux only
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Opens the County Market website and maximizes the window
    driver.get("https://www2.mycountymarket.com/circulars/select_a_store/")


    # Searches for each tab to toggle visible store locations
    tabs = driver.find_elements(By.CLASS_NAME, "stores-states-link.nav-link")

    full_addresses = []
    for tab in tabs:
        tab.click()
        # Searches for all store addresses
        time.sleep(1)
        temp_addresses = driver.find_elements(By.CLASS_NAME, "store-list-item-address.col")
        temp_cities = driver.find_elements(By.CLASS_NAME, "store-list-item-city.col-auto")
        for i in range(len(temp_addresses)):
            if temp_addresses[i].text != "":
                full_addresses.append(temp_addresses[i].text + ', ' + temp_cities[i].text)

    min_dist = 100000000
    closest_store = ""
    user_location = get_location(user_zip_code)

    for full_address in full_addresses:
        cur_dist = geodesic(user_location, get_location(full_address)).kilometers
        if(cur_dist < min_dist):
            min_dist = cur_dist
            closest_store = full_address

    # Searches for all elements with a link
    links = driver.find_elements("xpath","//a[@href]")

    # Extract street address of closest store
    closest_store = closest_store.split(',')[0]
    print("The closest store to you is " + closest_store + ", " + str(min_dist) + " km away")

    # Searches for the closest store's link in each tab
    print("Now scraping " + closest_store + " for deals.")
    my_link = ""
    for tab in tabs:
        tab.click()
        found = False
        for link in links:
            if closest_store in link.text:
                my_link = link
                found = True
                break
        if found:
            break

    # Follows link
    my_link.click()

    # Waits for new page to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))

    # Modify the current URL to switch to the newsprint form of the website
    current_url = driver.current_url #"https://www2.mycountymarket.com/circulars/Page/1/Base/1/240220_NCM//?store=2641"
    split_url = current_url.split('?')
    new_url = split_url[0] + '?format=online'
    driver.get(new_url)
    #https://www2.mycountymarket.com/circulars/Page/1/Base/1/240220_NCM//?store=2641
    #https://www2.mycountymarket.com/circulars/Page/1/Base/1/240220_NCM//?format=newsprint

    # Wait for the modified URL page to load
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))

    #searches for the total page count
    span_elements = driver.find_elements(By.CLASS_NAME, "d-none")
    page_count = 0
    for span_element in span_elements:
        text = span_element.text
        if "Page 1 of " in text:
            page_count = int(text[10:])

    title = []
    description = []
    price = []
    for i in range(1, page_count):
        div_elements = driver.find_elements(By.CSS_SELECTOR, "div.circular-item-body.card-body")
        if div_elements:
            for div_element in div_elements:
                h3_element = div_element.find_element(By.CLASS_NAME, "circular-item-title")
                description_element = div_element.find_element(By.CLASS_NAME, "circular-item-description")
                price_element = ""
                try:
                    price_element = div_element.find_element(By.CLASS_NAME, "price-big-dollars")
                except:
                    try:
                        price_element = div_element.find_element(By.CLASS_NAME, "price-big-cents")
                    except:
                        continue
                # Print the text contents of the child elements
                #formatting the information into arrays
                title.append(h3_element.text)
                description.append(description_element.text)
                price.append(price_element.text)
        next_page_button = driver.find_element(By.CLASS_NAME, "paging-next-page")
        next_page_button.click()
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))


    deals = []
    for i in range(0, len(title)):
        price[i] = price[i].replace(" ","", 2)
        price[i] = price[i].replace(" "," per ", 1)
        deals.append({
            'title': title[i],
            'description': description[i],
            'price': price[i]
        })

    with open('./data/' + str(closest_store) + '.json', 'w') as json_file:
        json.dump(deals, json_file)
    return deals

#get_deals(61820):
def get_cached_deals(user_zip_code):
    full_addresses = []
    with open('full_addresses.json', 'r') as json_file:
        data = json.load(json_file)
        full_addresses = data['addresses']
        
    with open('cached_locations.json', 'r') as json_file:
        location_dict = json.load(json_file)

    min_dist = 100000000
    closest_store = ""
    user_location = get_location(user_zip_code)

    for full_address in full_addresses:
        cur_dist = geodesic(user_location, location_dict[full_address]).kilometers
        if(cur_dist < min_dist):
            min_dist = cur_dist
            closest_store = full_address

    full_closest_store = closest_store
    closest_store = closest_store.split(',')[0]

    with open('./data/' + str(closest_store) + '.json', 'r') as json_file:
        # Load the data from the file
        loaded_data = json.load(json_file)
        to_return = {'distance': min_dist, 'address': full_closest_store, 'deals': loaded_data}
        return to_return
    

def scrape_by_address(closest_store):

    chrome_options = Options()
    
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox") # linux only
    chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get("https://www2.mycountymarket.com/circulars/select_a_store/")
    tabs = driver.find_elements(By.CLASS_NAME, "stores-states-link.nav-link")
    links = driver.find_elements("xpath","//a[@href]")

    # Searches for the closest store's link in each tab
    print("Now scraping " + closest_store + " for deals.")
    my_link = "potasd"
    for tab in tabs:
        tab.click()
        found = False
        for link in links:
            if closest_store[0:6] in link.text:
                my_link = link
                found = True
                break
        if found:
            break
    if my_link == "potasd":
        print(str(closest_store) + ' not found')
        return

    # Follows link
    my_link.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))

    current_url = driver.current_url #"https://www2.mycountymarket.com/circulars/Page/1/Base/1/240220_NCM//?store=2641"
    split_url = current_url.split('?')
    new_url = split_url[0] + '?format=online'
    driver.get(new_url)
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))

    #searches for the total page count
    span_elements = driver.find_elements(By.CLASS_NAME, "d-none")
    page_count = 0
    for span_element in span_elements:
        text = span_element.text
        if "Page 1 of " in text:
            page_count = int(text[10:])

    title = []
    description = []
    price = []
    for i in range(1, page_count):
        div_elements = driver.find_elements(By.CSS_SELECTOR, "div.circular-item-body.card-body")
        if div_elements:
            for div_element in div_elements:
                h3_element = div_element.find_element(By.CLASS_NAME, "circular-item-title")
                description_element = div_element.find_element(By.CLASS_NAME, "circular-item-description")
                price_element = ""
                try:
                    price_element = div_element.find_element(By.CLASS_NAME, "price-big-dollars")
                except:
                    try:
                        price_element = div_element.find_element(By.CLASS_NAME, "price-big-cents")
                    except:
                        continue
                title.append(h3_element.text)
                description.append(description_element.text)
                price.append(price_element.text)
        next_page_button = driver.find_element(By.CLASS_NAME, "paging-next-page")
        next_page_button.click()
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))


    deals = []
    for i in range(0, len(title)):
        price[i] = price[i].replace(" ","", 2)
        price[i] = price[i].replace(" "," per ", 1)
        deals.append({
            'title': title[i],
            'description': description[i],
            'price': price[i]
        })

    with open('./data/' + str(closest_store) + '.json', 'w') as json_file:
        json.dump(deals, json_file)

def scrape_all():
    full_addresses = []
    with open('full_addresses.json', 'r') as json_file:
        data = json.load(json_file)
        full_addresses = data['addresses']

    for full_address in full_addresses:
        print("now scraping " + str(full_address))
        temp = full_address.split(',')[0]
        scrape_by_address(temp)
        print("done scraping " + str(full_address))