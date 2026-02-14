from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time






#Full path to Top 10 vulnerabilites : class="md-nav_title" and ul class="md-nav_list" then 
#li class="md-nav_item" and This path is used for each vulnerabilities:
# a class="md-nav_link" href="https://owasp.org/Top10/2025/A"

#Set up the Selenium Webdriver
options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)


#website 
url = "https://owasp.org/Top10/2025/"

driver.get(url)
time.sleep(5)
print("Title:", driver.title)
print("Total <a> tags:", len(driver.find_elements(By.TAG_NAME, "a")))

#Using the X path that selects all 10 hrefs links 
elements = driver.find_elements(
    By.XPATH,
    "//a[contains(@href, '/A0') or contains(@href, '/A10')]"
)

print("Elements found:", len(elements))
#getting the top 10 list 
top10_list = []
seen = set()

for element in elements[:10]:
    
   title = element.text.strip()
   href = element.get_attribute("href")
   
   if title and href and href not in seen:
       top10_list.append({
           "title": title,
           "href": href
       })
       seen.add(href)
print("Total Vulnerabilites Found:", len(top10_list))
for item in top10_list:
    print(item)





#write to CSV
with open("owasp_top_10.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "href"])
    writer.writeheader()
    writer.writerows(top10_list)
print("Owasp_top_10 data appeared and created successfully.")   

