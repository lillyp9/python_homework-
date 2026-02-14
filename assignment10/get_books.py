from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd 
import json
import time

#using a function in the begining and end of the code to have it inported for task4
def get_books():
  
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(
           service=ChromeService(ChromeDriverManager().install()),
           options=options
           )
        url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
        driver.get(url)
         #Give Javascript time to render page
        time.sleep(3)

         #Find all book results <li> elements 
        book_items = driver.find_elements(By.TAG_NAME, "li")

         #Optional filter if the page has many <li> elements 
        book_items = [
            li for li in book_items
            if "cp-search-result-item" in li.get_attribute("class")
         ]
        print("Number of books found:", len(book_items))

        results = []

        for book in book_items:
            # ---- TITLE ---- 
            try:
               title_element = book.find_element(
                  By.CLASS_NAME, "cp-title"
               )
               title = title_element.text.strip()
            except:
               title = None 

            # Debug 
            print("Title:", title)

            # ----- Authors ----
            try:
               author_elements = book.find_elements(
                  By.CLASS_NAME, "cp-author-link")
               authors = [a.text.strip() for a in author_elements]
               author_text = "; ".join(authors) if authors else None 
            except:
               author_text = None 

            print("Author(s):", author_text)

            #------ Format + Year ----
            
            format_text = None
            year = None
            
            try:
               format_div = book.find_element(By.CLASS_NAME, "cp-format-info")
               text = format_div.text.strip()
               
               parts = text.split("_")
               if len(parts) == 2:
                   format_text = parts[0].strip()
                   year = parts[1].strip()
            except:
                pass

         #------Build a dictionary ---
            book_data = {
                "title": title,
                "authors": author_text,
                "format": format_text,
                "year": year
            }
            results.append(book_data)
        driver.quit()
        return results


if __name__ == "__main__":
    results = get_books() 
#task4 convert DataFrame then save CSV and JSON

df = pd.DataFrame(results)

df.to_csv("get_books.csv", index=False)

with open("get_books.json", "w") as f:
    json.dump(results, f, indent=4)
       
