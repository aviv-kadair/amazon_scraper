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


    @staticmethod
    def query_builder_ranking(parser, filtering_choice, spec_param):
        var_name = filtering_choice + '_' + spec_param
        #print(var_name)
        URL = queries_url.ranking.get(var_name)
        return URL

    @staticmethod
    def query_builder_manufacture(parser, filtering_choice, spec_param):
        var_name = filtering_choice+'_'+spec_param
        URL = queries_url.manufacture.get(var_name)
        return URL

        #print(f'{queries_url}.'+f'{var_name}')
#####
    @staticmethod
    def query_builder_screen(parser, filtering_choice, spec_param):
        var_name = (filtering_choice + '_' + spec_param).replace('-', '_2_')
        print(var_name)
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-filterQ', action=cli_tool)
    args = parser.parse_args()
    args.filterQ = input('Would you like to filter results? Y/N : ').upper()
    if args.filterQ == 'Y':
        #cli_tool.print_action(parser,args.filterQ)
        parser.add_argument('-parameter', action=cli_tool)
        filtering_choice = {'ranking':1, 'manufacturer':2, 'screen':3 , 'RAM':4, 'Weight':5, 'HD type':6}
        args.parameter = input(f'Choose a filter from the following list: {filtering_choice} ')
        parser.add_argument('-spec_param', action=cli_tool)
        if args.parameter == '1':
            args.spec_param = input('Choose a minimal item ranking, from 1 to 4 ')
            if args.spec_param not in range(1,5):
                args.spec_param = input('Ranking was not recognised, please try again: ')
            #cli_tool.print_action(parser, args.parameter, args.spec_param)
            URL = cli_tool.query_builder_ranking(parser,'ranking', args.spec_param)
            # TODO insert while loop to ensure data integrity, relevant for all conditions

        elif args.parameter == '2':
            manufactures = ['Acer', 'Dell','HP', 'Samsung','Lenovo','Asus','Apple']
            args.spec_param = input(f'Choose a manufacturer, from the following list: {manufactures} ')
            if args.spec_param not in manufactures:
                args.spec_param = input('Manufacturer was not recognised, please try again: ')
            URL = cli_tool.query_builder_manufacture(parser,'manufacture', args.spec_param)

        elif args.parameter == '3':
            screen_sizes = ['11', '11-12','12-13', '13-14','14-15', '15-16', '17']
            args.spec_param = input(f'Choose a screen size, from the following list: {screen_sizes} ')
            if args.spec_param not in screen_sizes:
                args.spec_param = input('Screen size was not recognised, please try again: ')
            URL = cli_tool.query_builder_screen(parser,'screen', args.spec_param)
        elif args.parameter == '4':
            RAM_sizes = ['4', '8', '12', '16','32']
            args.spec_param = input(f'Choose RAM size, from the following list: {RAM_sizes} ')
            if args.spec_param not in RAM_sizes:
                args.spec_param = input('RAM size was not recognised, please try again: ')
            URL = cli_tool.query_builder_RAM(parser,'RAM', args.spec_param)
        elif args.parameter == '5':
            weights = ['3-', '3-4', '4-5', '5-6', '7-8', '8']
            args.spec_param = input(f'Choose desired weight, from the following list: {weights} ')
            if args.spec_param not in weights:
                args.spec_param = input('Weight was not recognised, please try again: ')
            URL = cli_tool.query_builder_weight(parser,'weight', args.spec_param)
        elif args.parameter == '6':
            HD_type = ['SSD', 'HDD', 'Hybrid']
            args.spec_param = input(f'Choose desired hard drive type, from the following list: {HD_type} ')
            if args.spec_param not in HD_type:
                args.spec_param = input('HD type was not recognised, please try again: ')
            URL = cli_tool.query_builder_HD_type(parser,'HD_type', args.spec_param)
    cli_tool.print_action(parser)
    try:
        res = scraper_class.Search_Page(URL)
    except requests.exceptions.MissingSchema:
        print('Filtering choice was not recognised, exiting')
        quit()
    items = res.get_data()
    print('The following results match your search parameters: ')
    for result in items:
        splitter = result.split(',')
        print(f'Laptop name: {splitter[0]}')
        print(f'Specs: {splitter[1:]}')


if __name__ == '__main__':
    main()