from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys




options = Options()
options.add_experimental_option("detatch", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www2.mycountymarket.com/circulars/select_a_store/")
driver.maximize_window()

links = driver.find_elements("xpath","//a[@href]")

#note: I'm hard coding for a certain location right now, but I'll add functionality to choose stores later
my_link = ""

for link in links:
    if "331 Stoughton Street" in link.text:
        my_link = link
print(my_link.get_attribute("href"))
my_link.click()

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))

current_url = driver.current_url
new_url = current_url + '//?format=online'

driver.get(new_url)

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))

details = driver.find_elements("xpath","//*[contains(text(), 'Details')]")

#note: we only need to click one deal to load the details for all deals into the webpage
for detail in details:
    print(detail)
    detail.click()
    break

deals = driver.find_elements("xpath", "//div[@class='circular-item-body  modal-body']")

for deal in deals:
    print(deal)

while True:
    pass

#site content -> circulars -> circular -> search-hidden -> circular-content ->