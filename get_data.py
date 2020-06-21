"""Code to retrieve data from laptop search page on amazon
Authors: Aviv & Serah
"""

import requests
from bs4 import BeautifulSoup

def get_data(page_no):
    """Get the name, price, rating, link of the laptop from the search page

    :param
    page_no (int): The number of the page we want to analyze in the laptop search

    :return
    dict with the name of the laptop as the key and all its info (price, rating..) in a list for the value
    """

    dic = {}
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    web_page = requests.get("https://www.amazon.com/s?k=laptops&page=" + str(page_no), headers=headers) #, proxies=proxies)
    if not web_page.ok:
        print('Server responded: ', web_page.status_code)
    else:
        content = web_page.content
        soup = BeautifulSoup(content, features = "lxml")

        for d in soup.findAll('div', attrs={'class': 'sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28'}):
            name = d.find('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})
            review = d.find('span', attrs={'class': 'a-size-base'})
            price = d.find('span', attrs={'class': 'a-offscreen'})
            rating = d.find('span', attrs={'class': 'a-icon-alt'})
            #link = d.select_one('.a-link-normal')['href']

            if name is not None:
                link = d.find('a', {'class': "a-link-normal a-text-normal"})['href']
            else:
                link = None

            all_para = []

            if name is not None:
                all_para.append(name.text)

                if price is not None:
                    all_para.append(price.text)
                else:
                    all_para.append('$0')

                if rating is not None:
                    all_para.append(rating.text)
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

