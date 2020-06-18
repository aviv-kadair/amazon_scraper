import requests
from bs4 import BeautifulSoup

def get_data(pageNo):
    dic ={}
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    webpage = requests.get("https://www.amazon.com/s?k=laptops&page="+str(pageNo), headers=headers)#, proxies=proxies)
    if not webpage.ok:
        print('Server responded: ', webpage.status_code)
    else:
        content = webpage.content
        soup = BeautifulSoup(content,features="lxml")



    for d in soup.findAll('div', attrs={'class':'sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28'}):

        name = d.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})
        review = d.find('span', attrs = {'class':'a-size-base'})
        price = d.find('span', attrs={'class':'a-offscreen'})
        rating = d.find('span', attrs={'class':'a-icon-alt'})
        #link = d.select_one('.a-link-normal')['href']

        if name is not None:
            link = d.find('a', {'class':"a-link-normal a-text-normal"})['href']
        else:
            link=None

        all=[]


        if name is not None:
            all.append(name.text)

            if price is not None:
                all.append(price.text)
            else:
                all.append('$0')

            if rating is not None:
                all.append(rating.text)
            else:
                all.append('-1')

            if review is not None:
                all.append(review.text)
            else:
                all.append('0')
            if link is not None:
                all.append(link)

            else:
                all.append('No')


            dic[name.text] = all
    return dic

