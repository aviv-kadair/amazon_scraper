import requests
from bs4 import BeautifulSoup
from collections import defaultdict
para1={}
re={}

review = defaultdict(list)
def get_description(laptop_link):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    webpage = requests.get(laptop_link, headers=headers)#, proxies=proxies)
    if not webpage.ok:
        print('Server responded: ', webpage.status_code)
    else:
        content = webpage.content
        soup = BeautifulSoup(content)

        #Table1
        #val1 = soup.findAll('th', attrs={'class':'a-span3 comparison_attribute_name_column comparison_table_first_col'})
        #str_vals = str(val1)
        #par1=re.sub('\n','',BeautifulSoup(str_vals).get_text()).split(", ")[1:-1]

        #table1 = soup.findAll('td', attrs={'class':'comparison_baseitem_column'})
        #str_cells = str(table1)
        #print(str_cells)
        #values1=re.sub('\n','',BeautifulSoup(str_cells).get_text())[1:-1]

        #para1 = dict(zip(par1, values1))
        #print(values1)


        #laptop characteristics
        #table2
        table2 = soup.findAll(id="productDetails_techSpec_section_2")
        for tab in table2:
            t = tab.findAll('th')
            str_paras = str(t)

            parameters_tab2 =  BeautifulSoup(str_paras).get_text().replace('\n', '')
            par = tab.findAll('td')
            str_cells = str(par)
            values2=BeautifulSoup(str_cells).get_text().replace('\n', '')[1:-1].split(", ")


        par2 = parameters_tab2[1:-1].split(", ")
        para2 = dict(zip(par2, values2))


        #Table3
        table3 = soup.findAll(id="productDetails_techSpec_section_1")
        for tab in table3:
            t = tab.findAll('th')
            str_paras = str(t)
            parameters_tab3 =  BeautifulSoup(str_paras).get_text().replace("\n","")
            par = tab.findAll('td')
            str_cells = str(par)
            values3=BeautifulSoup(str_cells).get_text().replace('\n','')[1:-1].split(", ")


        par3 = parameters_tab3[1:-1].split(", ")
        para3 = dict(zip(par3, values3))


        #reviews

        soup = BeautifulSoup(content)
        for d in soup.findAll('div', attrs={'class':"a-section review aok-relative"}):
            #get the name
            n = d.find('span', attrs={'class':'a-profile-name'})
            name = n.get_text()
            #get the location and the date of the comment
            loca = d.find('span', attrs={'class':'a-size-base a-color-secondary review-date'})
            review.setdefault(name, []).append(loca.get_text())
            #review[name].append(loca.get_text())
            #get the rank that the user gives to the laptop
            rev=d.find('span', attrs = {'class':'a-icon-alt'})
            review.setdefault(name, []).append(rev.get_text())

            #get the profil link of the user
            review.setdefault(name, []).append(d.find('a',href=True,attrs={'class':'a-profile'})['href'])






        parameters = dict(para2, **para3)
        parameters['laptop_link']=laptop_link
        return  parameters,review




