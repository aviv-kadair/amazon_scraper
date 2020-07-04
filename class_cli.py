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
        parser_param.add_option(dest = 'ranking', type=str, help='minimal item ranking')
        parser_param.add_option(dest = 'manufacture', type=str, help='desired manufacture')
        parser_param.add_option(dest='screen_size', type=str, help='desired screen size')
        parser_param.add_option(dest='RAM_size', type=str, help='desired RAM size')