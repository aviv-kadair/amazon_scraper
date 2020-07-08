import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import random
from selenium import webdriver
import selenium as se
import re
import sys, os, re, cmd, shlex, optparse, json, pprint
import argparse
import click


class cli_tool(argparse.Action):
    prompt = 'Amazon Laptops Scraper> '

    def __call__(self, parser, namespace, value, option_string=None):
        self.print_action(parser, value)
        setattr(namespace, self.dest, value)


    @staticmethod
    def print_action(parser,value):
        print(value)

    @staticmethod
    def query_builder():
        pass


parser = argparse.ArgumentParser()
parser.add_argument('-filterQ', action=cli_tool)
args = parser.parse_args()
args.filterQ = input('Would you like to filter results?Y/N : ')
if args.filterQ == 'Y':
    cli_tool.print_action(parser,args.filterQ)
    parser.add_argument('-parameter', action=cli_tool)
    filtering_choice = {'ranking':1, 'manufacture':2, 'screen':3 , 'RAM':4, 'Weight':5, 'HD type':6}
    args.parameter = input(f'Choose a filter from the following list: {filtering_choice}')
    cli_tool.print_action(parser,args.parameter)

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
