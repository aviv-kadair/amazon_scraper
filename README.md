
# Amazon Laptops and Reviewers Scraper

<p align="center">
  <img src="http://static1.businessinsider.com/image/539f3ffbecad044276726c01-960/amazon-com-logo.jpg" width="200"><br><br>
</p>

## Features:
-   **Scrape laptops from the search results**
-   **Scrape laptop specs**
-   **Scrape reviewers profile**
-   Results are saved into csv files
-   Scraping 20 pages of products

## Requirements:
- BeautifulSoup4
- lxml parser
- pandas
- Selenium with correspodning webdriver
- Requests

## Installation:
  ```
  git clone https://github.com/thewizardofozz/amazon_scraper.git
  pip3 install -r requirements.txt
  ```
  
 ## Run:
 ```
 run main.py
 ```

 ## Current Status:
 - Stable: version 1.0
    - Scrapes laptop specs and reviewers details.
 ## Issues:
 - Amazon server occasionally blocks the ip address. 
    
 ## In Development:
 - Transition to classes
 - User based filtered results:
    - User may filter the reuslts based on specs, price or manufacture
 - SQL database:
    - Detection of product availability date
 
 
