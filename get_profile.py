from selenium import webdriver
import selenium as se
import re
import csv
import os


def user_profile(my_url):
    cwd = os.getcwd()
    options = se.webdriver.ChromeOptions()
    options.add_argument('headless chrome=83.0.4103.106')
    driver = se.webdriver.Chrome(cwd + "\\chromedriver.exe", options=options)
    driver.get("https://www.amazon.com" + my_url)
    p_element = driver.find_element_by_id(id_='profile_v5')
    txt = p_element.text

    #Get Reviewer ranking
    match1 = re.findall(r'Reviewer ranking\n#(\d+)\n', txt)
    if match1:
        reviewer_ranking = match1[0]
    else:
        reviewer_ranking = 0

    #Get reviews
    match2 = re.findall(r'\n([\d\,]+)\nreviews', txt)
    if match2:
        reviews = match2[0]
    else:
        reviews = 0

    #Get helpful votes
    match3 = re.findall(r'\n([\d\,]+)\nhelpful votes', txt)
    if match3:
        votes = match3[0]
    else:
        votes = 0

    return reviewer_ranking,reviews,votes


my_url = '//gp/profile//amzn1.account.AEMRAZPNN2NBBUDV4YGGYMGPFC6A//ref=cm_cr_dp_d_gw_tr?ie=UTF8'
print(user_profile(my_url))
