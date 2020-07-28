import requests
from bs4 import BeautifulSoup
import random
from selenium import webdriver
import selenium as se
import re
import config
from Logging import logger
from time import sleep
from random import randint

from Scraping.scraper_class import Scraper

proxies_list = config.PROXIES_LIST
headers = config.HEADERS
proxy = {'http': random.choice(Scraper.proxies_list)}
url = 'https://www.amazon.com/s?k=laptop&qid=1591707465&ref=sr_pg_2'
web_page = requests.get(url, headers=Scraper.headers, proxies=proxy)
content = web_page.content
print(content)
