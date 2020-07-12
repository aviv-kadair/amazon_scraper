"""
This file contains all the scraping class
Authors:
Aviv and Serah
"""

import requests
from bs4 import BeautifulSoup
import random
from selenium import webdriver
import selenium as se
import re
from laptop_class import Laptop
from laptop_features_class import Features
from reviews_class import Review
from profile_class import Profile
import config
from Logging import logger
from time import sleep
from random import randint


class Scraper:
    proxies_list = config.PROXIES_LIST
    headers = config.HEADERS

    def __init__(self, link):
        self.url = link
        self.proxy = {'http': random.choice(Scraper.proxies_list)}
        self.web_page = requests.get(self.url, headers=Scraper.headers, proxies=self.proxy)

        if self.web_page.status_code > 500:
            if "To discuss automated access to Amazon data please contact" in self.web_page.text:
                logger.warning("Page %s was blocked by Amazon. Please try using better proxies\n" % self.url)
            else:
                logger.warning("Page %s must have been blocked by Amazon as the status code was %d" % (
                    self.url, self.web_page.status_code))
            self.soup = None
        else:
            content = self.web_page.content
            self.soup = BeautifulSoup(content, features="lxml")

    def get_soup(self):
        """Return the web content of our url after BeautifulSoup"""
        return self.soup


class SearchPage(Scraper):
    def __init__(self, link):
        super().__init__(link)

    def get_data(self):
        """Retrieve the data for all the laptops of the search page of amazon"""
        laptop_list = []
        for d in self.soup.findAll('div', attrs={'class': 'sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28'}):
            name = d.find('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})
            review = d.find('span', attrs={'class': 'a-size-base'})
            price = d.find('span', attrs={'class': 'a-offscreen'})
            rating = d.find('span', attrs={'class': 'a-icon-alt'})

            if name is not None:
                link = d.find('a', {'class': "a-link-normal a-text-normal"})['href']
            else:
                link = None

            if name is not None:
                name = name.text

                if price is not None:
                    price = price.text[1::]
                else:
                    price = 0

                if rating is not None:
                    rating = rating.text.split()[0]
                else:
                    rating = -1

                if review is not None:
                    reviews = review.text
                else:
                    reviews = 0
                if link is not None:
                    link = link
                else:
                    link = 'Empty'

                laptop_list.append(Laptop(name, price, rating, reviews, link))
        return laptop_list


class Parameters(Scraper):

    def __init__(self, link):
        super().__init__(link)

    def get_param(self):
        """Retrieve all the parameters of a laptop from the product page"""
        para = {}
        table2 = self.soup.find(attrs={'id': "productDetails_techSpec_section_2"})
        if table2 is not None:
            table2 = table2.findAll('tr')

            for tab in table2:
                str_paras = str(tab.findAll('th'))
                parameters_tab2 = BeautifulSoup(str_paras, features="lxml").get_text().replace('\n', '').replace('\r',
                                                                                                                 "")
                characteristics = ['Screen Size', 'Max Screen Resolution', 'Chipset Brand', 'Card Description',
                                   'Brand Name', 'Item Weight', 'Operating System', 'Computer Memory Type', 'Batteries']
                if parameters_tab2[1:-1] in characteristics:
                    str_cells = str(tab.findAll('td'))
                    para[parameters_tab2[1:-1]] = BeautifulSoup(str_cells, features="lxml").get_text().replace('\n',
                                                                                                               '')[
                                                  1:-1]
        else:
            logger.warning(f'{self.url}  doesn\'t return content for table2')
        # Table3
        table3 = self.soup.find(attrs={'id': "productDetails_techSpec_section_1"})
        if table3 is not None:
            table3 = table3.findAll('tr')

            for tab in table3:
                str_paras = str(tab.findAll('th'))
                parameters_tab3 = BeautifulSoup(str_paras, features="lxml").get_text().replace('\n', '').replace('\r',
                                                                                                                 "")
                characteristics = config.LAPTOP_FEATURES
                if parameters_tab3[1:-1] in characteristics:
                    str_cells = str(tab.findAll('td'))
                    para[parameters_tab3[1:-1]] = BeautifulSoup(str_cells, features="lxml").get_text().replace('\n',
                                                                                                               '')[1:-1]
        else:
            logger.warning(f'{self.url}  doesn\'t return content for table3')

        if table2 is not None and table3 is not None:
            new_para = {k.lower().replace(' ', '_'): v for k, v in para.items()}
            return Features(**new_para)


class Reviews(Scraper):

    def __init__(self, link):
        super().__init__(link)

    def get_reviews(self):
        """Get all the top reviews from the product page of the laptop"""
        reviews = []
        for d in self.soup.findAll('div', attrs={'class': "a-section review aok-relative"}):
            # get the name
            n = d.find('span', attrs={'class': 'a-profile-name'})
            name = n.get_text()
            # get the location and the date of the comment
            loc = d.find('span', attrs={'class': 'a-size-base a-color-secondary review-date'})
            location = loc.get_text().split(' on ')[0].split('Reviewed in ')[1]
            date = loc.get_text().split(' on ')[1]
            # get the rank that the user gives to the laptop
            rev = d.find('span', attrs={'class': 'a-icon-alt'}).get_text().split()[0]
            # get the profile link of the user
            link = d.find('a', href=True, attrs={'class': 'a-profile'})['href']

            reviews.append(Review(name, location, date, rev, link))
        return reviews


class ProfileScrapper:

    def __init__(self, link):
        options = se.webdriver.ChromeOptions()
        options.add_argument('headless chrome=83.0.4103.106')
        options.add_argument("enable-features=NetworkServiceInProcess")
        options.add_argument("disable-features=NetworkService")
        options.add_argument("--lang=en-US")
        self.driver = se.webdriver.Chrome(config.BROWSER, options=options)
        self.link = link
        try:
            self.driver.get(config.AMAZON + self.link)
        except TimeoutError:
            sleep(randint(1, 10))
            self.driver.back()

    def user_profile(self):
        """Get the user info from its profile"""

        p_element = self.driver.find_element_by_id(id_='profile_v5')
        txt = p_element.text

        # Get Reviewer ranking
        match1 = re.findall(r'Reviewer ranking\n#([\d,]+)\n', txt)
        if match1:
            reviewer_ranking = match1[0].replace(',', '')
        else:
            reviewer_ranking = 0

        # Get reviews
        match2 = re.findall(r'\n([\d,]+)\nreviews', txt)
        if match2:
            reviews = match2[0].replace(',', '')
        else:
            reviews = 0

        # Get helpful votes
        match3 = re.findall(r'\n([\d,]+)\nhelpful votes', txt)
        if match3:
            votes = match3[0].replace(',', '')
        else:
            votes = 0

        return Profile(self.link, reviewer_ranking, reviews, votes)

# print(get_description('https://www.amazon.com/dp/B08173ZTJX/ref=sr_1_6?dchild=1&keywords=laptops&qid=1592682151&sr=8-6'))

# url = 'https://www.amazon.com/dp/B08173ZTJX/ref=sr_1_6?dchild=1&keywords=laptops&qid=1592682151&sr=8-6'

# scraper = Reviews(url)
# print(scraper.get_reviews())
# scrap = ProfileScrapper('/gp/profile/amzn1.account.AEQQY4I75RA6VVZW5WQN2KUU4YRQ/ref=cm_cr_dp_d_gw_tr?ie=UTF8')
# print(scrap.user_profile().get_arg('Reviewer_Ranking'))
