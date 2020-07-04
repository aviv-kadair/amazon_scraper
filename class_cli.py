import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import random
from selenium import webdriver
import selenium as se
import re
import sys, os, re, cmd, shlex, optparse, json, pprint
import argparse

class cli_tool(cmd.Cmd):
    prompt = 'Amazon Laptops Scraper> '

    def __init__(self, filename, **kw):
        self.filename = filename
        cmd.Cmd.__init__(self, **kw)

    def set_search_parameter(self, ):
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