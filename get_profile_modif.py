"""Get info about amazon users with their profile link
Authors: Aviv & Serah"""

from selenium import webdriver
import selenium as se
import re
from bs4 import BeautifulSoup
import pandas as pd
import csv
import os


def user_profile(my_url):
    """Retrieve reviewers ranking, reviews, and helpful votes from the user's profile

    :param
    my_url (string) The link of a user profile

    :returns
    reviewer_ranking, reviews, votes (int)
    """
    #driver = webdriver.Chrome("chromedriver.exe")
    #driver.get(url)
    options = se.webdriver.ChromeOptions()
    options.add_argument('headless chrome=83.0.4103.106')
    options.add_argument("enable-features=NetworkServiceInProcess")
    options.add_argument("disable-features=NetworkService")
    options.add_argument("--lang=en-US")
    driver = se.webdriver.Chrome("chromedriver.exe", options=options)
    driver.get("https://www.amazon.com" + my_url)
    bs_obj = BeautifulSoup(driver.page_source, 'lxml')

    for d in bs_obj.findAll('div', attrs={'class': "dashboard-desktop-stat-value"}):
        if d.get_text() != "":
            print(d.get_text())
        else:
            print('blank page')

    for d in bs_obj.findAll('div', attrs={'class': "a-section a-spacing-top-base"}):
        print(d.get_text())




data2 = pd.read_csv("reviews_info.csv")
profile_links = data2['link'][9:16]
for i, url in enumerate(profile_links):
    user_profile(url)
    print(i)
