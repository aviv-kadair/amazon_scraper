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
import scraper_class

class cli_tool(argparse.Action):
    """This class builds a search query based on the user input"""
    prompt = 'Amazon Laptops Scraper> '

    def __call__(self, parser, namespace, filtering_choice, spec_param, option_string=None):
        self.print_action(parser, filtering_choice, spec_param)
        setattr(namespace, self.dest, filtering_choice, spec_param)



    @staticmethod
    def print_action(parser):
        print('Retrieving search results, please wait')



    def query_builder_ranking(parser, filtering_choice, spec_param):
        var_name = filtering_choice + '_' + spec_param
        #print(var_name)
        URL = queries_url.ranking.get(var_name)
        return URL


    def query_builder_manufacture(parser, filtering_choice, spec_param):
        var_name = filtering_choice+'_'+spec_param
        #print(var_name)
        URL = queries_url.manufacture.get(var_name)
        #print(URL)
        return URL


    def query_builder_screen(parser, filtering_choice, spec_param):
        var_name = (filtering_choice + '_' + spec_param).replace('-', '_2_')
        #print(var_name)
        URL = queries_url.screen.get(var_name)
        return URL


    def query_builder_RAM(parser, filtering_choice, spec_param):
        var_name = filtering_choice + '_' + spec_param
        #print(var_name)
        URL = queries_url.RAM.get(var_name)
        return URL


    def query_builder_weight(parser, filtering_choice, spec_param):
        var_name = filtering_choice + '_' + spec_param
        var_name = var_name.replace('-', '_2_')
        #print(var_name)
        URL = queries_url.weight.get(var_name)
        #print(URL)
        return URL


    def query_builder_HD_type(parser, filtering_choice, spec_param):
        var_name = filtering_choice + '_' + spec_param
        URL = queries_url.HD_type.get(var_name)
        return URL


