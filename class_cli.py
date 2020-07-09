import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import random
from selenium import webdriver
import selenium as se
import re
import sys, os, re, cmd, shlex, optparse, json, pprint
import argparse
import queries_url


class cli_tool(argparse.Action):
    prompt = 'Amazon Laptops Scraper> '

    def __call__(self, parser, namespace, filtering_choice, spec_param, option_string=None):
        self.print_action(parser, filtering_choice, spec_param)
        setattr(namespace, self.dest, filtering_choice, spec_param)


    @staticmethod
    def print_action(parser,filtering_choice, spec_param):
        print(f'The following search parameters are applied: parameter:{filtering_choice}, specification:{spec_param}')


    @staticmethod
    def query_builder_ranking(parser, filtering_choice, spec_param):
        var_name = filtering_choice + '_' + spec_param
        print(var_name)
        URL = queries_url.ranking.get(var_name)
        return URL

    @staticmethod
    def query_builder_manufacture(parser, filtering_choice, spec_param):
        var_name = filtering_choice+'_'+spec_param
        URL = queries_url.manufacture.get(var_name)
        return URL
        #print(f'{queries_url}.'+f'{var_name}')

    @staticmethod
    def query_builder_screen(parser, filtering_choice, spec_param):
        var_name = filtering_choice + '_' + spec_param
        var_name.replace('-', '_2_')
        URL = queries_url.screen.get(var_name)
        return URL

    @staticmethod
    def query_builder_RAM(parser, filtering_choice, spec_param):
        var_name = filtering_choice + '_' + spec_param
        #print(var_name)
        URL = queries_url.RAM.get(var_name)
        return URL

    @staticmethod
    def query_builder_weight(parser, filtering_choice, spec_param):
        var_name = filtering_choice + '_' + spec_param
        var_name.replace('-', '_2_')
        URL = queries_url.weight.get(var_name)
        return URL

    @staticmethod
    def query_builder_HD_type(parser, filtering_choice, spec_param):
        var_name = filtering_choice + '_' + spec_param
        URL = queries_url.HD_type.get(var_name)
        return URL




class filtered_search():
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
        self.proxy = {'http': random.choice(filtered_search.PROXIES_LIST)}
        self.web_page = requests.get(self.url, headers=filtered_search.HEADERS, proxies=self.proxy)

        if self.web_page.status_code > 500:
            if "To discuss automated access to Amazon data please contact" in self.web_page.text:
                print("The page was blocked by Amazon. Please try using better proxies\n" % self.url)
            else:
                print("The page must have been blocked by Amazon as the status code was %d" % (
                    self.url, self.web_page.status_code))
            self.soup = None
        else:
            content = self.web_page.content
            self.soup = BeautifulSoup(content, features="lxml")


class filtered_results(filtered_search):
    def __init__(self, link):
        super().__init__(link)

    def get_data(self):
        dic = {}
        for d in self.soup.findAll('div', attrs={
            'class': 'sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28'}):
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



parser = argparse.ArgumentParser()
parser.add_argument('-filterQ', action=cli_tool)
args = parser.parse_args()
args.filterQ = input('Would you like to filter results?Y/N : ')
if args.filterQ == 'Y':
    #cli_tool.print_action(parser,args.filterQ)
    parser.add_argument('-parameter', action=cli_tool)
    filtering_choice = {'ranking':1, 'manufacture':2, 'screen':3 , 'RAM':4, 'Weight':5, 'HD type':6}
    args.parameter = input(f'Choose a filter from the following list: {filtering_choice}')
    parser.add_argument('-spec_param', action=cli_tool)
    if args.parameter == '1':
        args.spec_param = input('Choose a minimal item ranking, from 1 to 4 ')
        #cli_tool.print_action(parser, args.parameter, args.spec_param)
        URL = cli_tool.query_builder_ranking(parser,'ranking', args.spec_param)
        # TODO insert while loop to ensure data integrity, relevant for all conditions
        """while args.spec_param not in range(1,5):
            args.spec_param = input('Choose a minimal item ranking, from 1 to 5 ')
            if args.spec_param in range(1,5):
                break"""
    elif args.parameter == '2':
        manufactures = ['Acer', 'Dell','HP', 'Samsung','Lenovo','Asus','Apple']
        args.spec_param = input(f'Choose a manufacture, from the following list: {manufactures} ')
        URL = cli_tool.query_builder_manufacture(parser,'manufacture', args.spec_param)
    elif args.parameter == '3':
        screen_sizes = ['11', '11-12','12-13', '13-14','14-15', '15-16', '17']
        args.spec_param = input(f'Choose a screen size, from the following list: {screen_sizes} ')
        URL = cli_tool.query_builder_screen(parser,'screen', args.spec_param)
    elif args.parameter == '4':
        RAM_sizes = ['4', '8', '12', '16','32']
        args.spec_param = input(f'Choose RAM size, from the following list: {RAM_sizes} ')
        URL = cli_tool.query_builder_RAM(parser,'RAM', args.spec_param)
    elif args.parameter == '5':
        weights = ['3-', '3-4', '4-5', '5-6', '7-8', '8']
        args.spec_param = input(f'Choose desired weight, from the following list: {weights} ')
        URL = cli_tool.query_builder_weight(parser,'weight', args.spec_param)
    elif args.parameter == '6':
        HD_type = ['SSD', 'HDD', 'Hybrid']
        args.spec_param = input(f'Choose desired hard drive type, from the following list: {HD_type} ')
        URL = cli_tool.query_builder_HD_type(parser,'HD_type', args.spec_param)
else:
    print('No')





"""

class cli_tool(cmd.Cmd):
    prompt = 'Amazon Laptops Scraper> '

    def __init__(self,**kw):
        #self.filename = filename
        cmd.Cmd.__init__(self, **kw)

    def set_search_parameter(self):
        parser_param = argparse.ArgumentParser
        parser_param.add_option(dest = 'ranking', type=int, help='minimal item ranking', choices=(1, 2, 3, 4, 5))
        parser_param.add_option(dest = 'manufacture', type=str, help='desired manufacture', choices=('Acer', 'Dell',
                                                                                                     'HP', 'Samsung',
                                                                                                     'Lenovo','Asus',
                                                                                                     'Apple'))
        parser_param.add_option(dest='screen_size', type=str, help='desired screen size', choices=('11-', '11-12',
                                                                                                   '12-13', '13-14',
                                                                                                   '14-15', '15-16',
                                                                                                   '16-17', '17+'))
        parser_param.add_option(dest='RAM_size', type=str, help='desired RAM size', choices=('4', '8', '12', '16',
                                                                                             '32', '64'))
        parser_param.add_option(dest='weight', type=str, help='desired laptop weight in pounds',
                                choices=('3-', '3-4', '4-5', '5-6', '7-8', '8+'))
        parser_param.add_option(dest='HD_type', type=str, help='desired hard drive type',
                                choices=('SSD', 'HDD', 'Hybrid'))


filter_response = input('Would you like to filter the results? Y/N ')
if filter_response == 'Y':
    print('Yes')
    cl_tool = cli_tool()
    cl_tool.set_search_parameter()
else:
    print('No')
"""
