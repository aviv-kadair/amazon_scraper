import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import random
from selenium import webdriver
import selenium as se
import re


class Scraper:
    PROXIES_LIST = ["128.199.109.241:8080", "113.53.230.195:3128", "125.141.200.53:80", "125.141.200.14:80",
                    "128.199.200.112:138", "149.56.123.99:3128", "128.199.200.112:80", "125.141.200.39:80",
                    "134.213.29.202:4444"]
    HEADERS = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    def __init__(self, link):
        self.url = link
        self.proxy = {'http': random.choice(Scraper.PROXIES_LIST)}
        self.web_page = requests.get(self.url, headers=Scraper.HEADERS, proxies=self.proxy)

        if self.web_page.status_code > 500:
            if "To discuss automated access to Amazon data please contact" in self.web_page.text:
                print("Page %s was blocked by Amazon. Please try using better proxies\n" % self.url)
            else:
                print("Page %s must have been blocked by Amazon as the status code was %d" % (
                self.url, self.web_page.status_code))
            self.soup = None
        else:
            content = self.web_page.content
            self.soup = BeautifulSoup(content, features="lxml")


class Search_Page(Scraper):
    def __init__(self, link):
        super().__init__(link)

    def get_data(self):
        dic = {}
        for d in self.soup.findAll('div', attrs={'class': 'sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28'}):
            name = d.find('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})
            review = d.find('span', attrs={'class': 'a-size-base'})
            price = d.find('span', attrs={'class': 'a-offscreen'})
            rating = d.find('span', attrs={'class': 'a-icon-alt'})

            if name is not None:
                link = d.find('a', {'class': "a-link-normal a-text-normal"})['href']
            else:
                link = None

            all_para = []

            if name is not None:
                all_para.append(name.text)

                if price is not None:
                    all_para.append(price.text[1::])
                else:
                    all_para.append('0')

                if rating is not None:
                    all_para.append(rating.text.split()[0])
                else:
                    all_para.append('-1')

                if review is not None:
                    all_para.append(review.text)
                else:
                    all_para.append('0')
                if link is not None:
                    all_para.append(link)
                else:
                    all_para.append('Empty')

                dic[name.text] = all_para
        return dic


class Parameters(Scraper):

    def __init__(self, link):
        super().__init__(link)

    def get_param(self):
        para = {}
        table2 = self.soup.find(attrs={'id': "productDetails_techSpec_section_2"})
        table2 = table2.findAll('tr')

        for tab in table2:
            str_paras = str(tab.findAll('th'))
            parameters_tab2 = BeautifulSoup(str_paras, features="lxml").get_text().replace('\n', '').replace('\r', "")
            characteristics = ['Screen Size', 'Max Screen Resolution', 'Chipset Brand', 'Card Description',
                               'Brand Name', 'Item Weight', 'Operating System', 'Computer Memory Type', 'Batteries']
            if parameters_tab2[1:-1] in characteristics:
                str_cells = str(tab.findAll('td'))
                para[parameters_tab2[1:-1]] = BeautifulSoup(str_cells, features="lxml").get_text().replace('\n', '')[
                                              1:-1]

        # Table3
        table3 = self.soup.find(attrs={'id': "productDetails_techSpec_section_1"})
        table3 = table3.findAll('tr')

        for tab in table3:
            str_paras = str(tab.findAll('th'))
            parameters_tab3 = BeautifulSoup(str_paras, features="lxml").get_text().replace('\n', '').replace('\r', "")
            characteristics = ['Screen Size', 'Max Screen Resolution', 'Chipset Brand', 'Card Description',
                               'Brand Name', 'Item Weight', 'Operating System', 'Computer Memory Type', 'Batteries']
            if parameters_tab3[1:-1] in characteristics:
                str_cells = str(tab.findAll('td'))
                para[parameters_tab3[1:-1]] = BeautifulSoup(str_cells, features="lxml").get_text().replace('\n', '')[
                                              1:-1]
        return para


class Reviews(Scraper):

    def __init__(self, link):
        super().__init__(link)

    def get_reviews(self):
        review = defaultdict(list)
        for d in self.soup.findAll('div', attrs={'class': "a-section review aok-relative"}):
            # get the name
            n = d.find('span', attrs={'class': 'a-profile-name'})
            name = n.get_text()
            # get the location and the date of the comment
            loc = d.find('span', attrs={'class': 'a-size-base a-color-secondary review-date'})
            location = loc.get_text().split(' on ')[0].split('Reviewed in ')[1]
            review.setdefault(name, []).append(location)
            date = loc.get_text().split(' on ')[1]
            review.setdefault(name, []).append(date)
            # get the rank that the user gives to the laptop
            rev = d.find('span', attrs={'class': 'a-icon-alt'}).get_text().split()[0]
            review.setdefault(name, []).append(rev)
            # get the profil link of the user
            review.setdefault(name, []).append(d.find('a', href=True, attrs={'class': 'a-profile'})['href'])

        return review


class Profile:

    options = se.webdriver.ChromeOptions()
    options.add_argument('headless chrome=83.0.4103.106')
    options.add_argument("enable-features=NetworkServiceInProcess")
    options.add_argument("disable-features=NetworkService")
    options.add_argument("--lang=en-US")
    driver = se.webdriver.Chrome("chromedriver.exe", options=options)

    def __init__(self, link):
        self.url = link
        self.driver = Profile.driver.get("https://www.amazon.com" + self.url)


    def user_profile(self):
        p_element = self.driver.find_element_by_id(id_='profile_v5')
        txt = p_element.text

        #Get Reviewer ranking
        match1 = re.findall(r'Reviewer ranking\n#([\d,]+)\n', txt)
        if match1:
            reviewer_ranking = match1[0]
        else:
            reviewer_ranking = 0

        #Get reviews
        match2 = re.findall(r'\n([\d,]+)\nreviews', txt)
        if match2:
            reviews = match2[0]
        else:
            reviews = 0

        #Get helpful votes
        match3 = re.findall(r'\n([\d,]+)\nhelpful votes', txt)
        if match3:
            votes = match3[0]
        else:
            votes = 0

        return reviewer_ranking,reviews,votes


# print(get_description('https://www.amazon.com/dp/B08173ZTJX/ref=sr_1_6?dchild=1&keywords=laptops&qid=1592682151&sr=8-6'))

url = 'https://www.amazon.com/dp/B08173ZTJX/ref=sr_1_6?dchild=1&keywords=laptops&qid=1592682151&sr=8-6'

scraper = Reviews(url)
print(scraper.get_reviews())
