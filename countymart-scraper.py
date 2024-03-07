from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys




# Initializes a selenium webdriver for Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Opens the County Market website and maximizes the window
driver.get("https://www2.mycountymarket.com/circulars/select_a_store/")
driver.maximize_window()

# Searches for all elements with a link
links = driver.find_elements("xpath","//a[@href]")

# NOTE: I'm hard coding for a certain location right now, but I'll add functionality to choose stores later
my_link = ""
for link in links:
    if "331 Stoughton Street" in link.text:
        my_link = link
print(my_link.get_attribute("href"))

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
    url_parts = new_url.split("/")
    index_page = url_parts.index("Page")
    url_parts[index_page + 1] = str(i)
    new_url = "/".join(url_parts)
    driver.get(new_url)
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
    # Find the <div> element with the specified class
    div_elements = driver.find_elements(By.CSS_SELECTOR, "div.circular-item-body.card-body")
    if div_elements:
        for div_element in div_elements:
            # If the element is found, find its child elements
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

for i in range(0, len(title)):
    price[i] = price[i].replace(" ","", 2)
    price[i] = price[i].replace(" "," per ", 1)
    print("Title: " + title[i])
    print("Description: " + description[i])
    print("Price: " + price[i])


while(True):
    pass