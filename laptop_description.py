"""Retrieve all the info: description + reviews from the description page of each laptop
Authors: Aviv & Serah
"""
import requests
from bs4 import BeautifulSoup
from collections import defaultdict


def get_description(laptop_link):
    """Get the laptop features and all the reviews

    :param
    laptop_link (str) the link of the laptop page

    :returns
    parameters (dict):  all the features of the laptop
    review (dict): details on the reviews of the laptop
    """

    review = defaultdict(list)
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    web_page = requests.get(laptop_link, headers=headers)  # , proxies=proxies)
    if not web_page.ok:
        print('Server responded: ', web_page.status_code)
    else:
        content = web_page.content
        soup = BeautifulSoup(content, features="lxml")
        # laptop characteristics
        # table2
        # Get the titles (parameters) and the corresponding values
        table2 = soup.findAll(id="productDetails_techSpec_section_2")
        parameters_tab2 = []
        values2 = []
        para2 = {}
        for tab in table2:
            t = tab.findAll('th')
            str_paras = str(t)
            parameters_tab2 = BeautifulSoup(str_paras, features="lxml").get_text().replace('\n', '').replace('\r', "")
            par = tab.findAll('td')
            str_cells = str(par)
            values2 = BeautifulSoup(str_cells, features="lxml").get_text().replace('\n', '')[1:-1].split(", ")

        if len(parameters_tab2) > 0:
            par2 = parameters_tab2[1:-1].split(", ")
            para2 = dict(zip(par2, values2))

        # Table3
        table3 = soup.findAll(id="productDetails_techSpec_section_1")
        parameters_tab3 = []
        values3 = []
        para3 = {}
        for tab in table3:
            t = tab.findAll('th')
            str_paras = str(t)
            parameters_tab3 = BeautifulSoup(str_paras, features="lxml").get_text().replace("\n", "").replace('\r', "")
            par = tab.findAll('td')
            str_cells = str(par)
            values3 = BeautifulSoup(str_cells, features="lxml").get_text().replace('\n', '')[1:-1].split(", ")

        if len(parameters_tab3) > 0:
            par3 = parameters_tab3[1:-1].split(", ")
            para3 = dict(zip(par3, values3))

        # reviews
        soup = BeautifulSoup(content, features="lxml")
        for d in soup.findAll('div', attrs={'class': "a-section review aok-relative"}):
            # get the name
            n = d.find('span', attrs={'class': 'a-profile-name'})
            name = n.get_text()
            # get the location and the date of the comment
            location = d.find('span', attrs={'class': 'a-size-base a-color-secondary review-date'})
            review.setdefault(name, []).append(location.get_text())
            # get the rank that the user gives to the laptop
            rev = d.find('span', attrs={'class': 'a-icon-alt'})
            review.setdefault(name, []).append(rev.get_text())
            # get the profil link of the user
            review.setdefault(name, []).append(d.find('a', href=True, attrs={'class': 'a-profile'})['href'])

        parameters = dict(para2, **para3)
        parameters['laptop_link'] = laptop_link
        return parameters, review

#print(get_description('https://www.amazon.com/dp/B08173ZTJX/ref=sr_1_6?dchild=1&keywords=laptops&qid=1592682151&sr=8-6'))
