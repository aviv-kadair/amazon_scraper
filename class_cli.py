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

    def __call__(self, parser, namespace, value, option_string=None):
        self.print_action(parser, value)
        setattr(namespace, self.dest, value)


    @staticmethod
    def print_action(parser,value):
        print(value)

    @staticmethod
    def query_builder(parser, value):
        URL = 'https://www.amazon.com/s?k=laptops&page='


parser = argparse.ArgumentParser()
parser.add_argument('-filterQ', action=cli_tool)
args = parser.parse_args()
args.filterQ = input('Would you like to filter results?Y/N : ')
if args.filterQ == 'Y':
    cli_tool.print_action(parser,args.filterQ)
    parser.add_argument('-parameter', action=cli_tool)
    filtering_choice = {'ranking':1, 'manufacture':2, 'screen':3 , 'RAM':4, 'Weight':5, 'HD type':6}
    args.parameter = input(f'Choose a filter from the following list: {filtering_choice}')
    parser.add_argument('-spec_param', action=cli_tool)
    if args.parameter == '1':
        args.spec_param = input('Choose a minimal item ranking, from 1 to 5 ')
        # TODO insert while loop to ensure data integrity, relevant for all conditions
        """while args.spec_param not in range(1,5):
            args.spec_param = input('Choose a minimal item ranking, from 1 to 5 ')
            if args.spec_param in range(1,5):
                break"""
    elif args.parameter == '2':
        manufactures = ['Acer', 'Dell','HP', 'Samsung','Lenovo','Asus','Apple']
        args.spec_param = input(f'Choose a manufacture, from the following list: {manufactures}')
    elif args.parameter == '3':
        screen_sizes = ['11', '11-12','12-13', '13-14','14-15', '15-16', '17']
        args.spec_param = input(f'Choose a screen size, from the following list: {screen_sizes}')
    elif args.parameter == '4':
        RAM_sizes = ['4', '8', '12', '16','32']
        args.spec_param = input(f'Choose RAM size, from the following list: {RAM_sizes}')
    elif args.parameter == '5':
        weights = ['3-', '3-4', '4-5', '5-6', '7-8', '8+']
        args.spec_param = input(f'Choose desired weight, from the following list: {weights}')
    elif args.parameter == '5':
        HD_type = ['SSD', 'HDD', 'Hybrid']
        args.spec_param = input(f'Choose desired weight, from the following list: {HD_type}')
    cli_tool.print_action(parser,args.spec_param)

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
