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

class cli_tool_test(argparse.Action):
    """This class builds a search query based on the user input"""
    prompt = 'Amazon Laptops Scraper> '

    def __call__(self, parser, namespace, filtering_choice, spec_param, option_string=None):
        self.print_action(parser, filtering_choice, spec_param)
        setattr(namespace, self.dest, filtering_choice, spec_param)

    def choose_filter(self):
        """This method gets an input from the user stating the required search filter"""
        parameter = input(f'Choose a filter from the following list: {queries_url.filtering_choice} ')
        if parameter.isdigit():
            parameter = int(parameter)
            if parameter ==1:
                user_filter = input('Please choose a minimal item ranking, from 1 to 4: ')
                if user_filter not in range(1,5):
                    user_filter = input('Ranking was not recognised, please try again: ')
            elif 2 <= parameter <= 6:
                filter_list = self.get_choice(parameter)
                user_filter  = input(f'Please refine you search: {filter_list}')
                if user_filter not in filter_list:
                    user_filter = input('Your choice was not recognised, please try again: ')
            else:
                print('Your filter was not recognised, exiting')
                quit()
            return parameter, user_filter
        else:
            print('Chosen parameter is not recognised, exiting')

    @staticmethod
    def get_choice(choice):
        """This function imports the relevant choice list"""
        choices = {2: queries_url.manufactures_list, 3: queries_url.screen_sizes, 4: queries_url.RAM_sizes,
                   5: queries_url.weights_list, 6: queries_url.HD_type_list}
        choice_list = choices.get(choice)
        return choice_list



    def function_map(self, parameter, user_filter):
        """This function is designed to call the appropriate function from the function map"""
        function_map = {1: self.query_builder_ranking(user_filter),
                2: self.query_builder_manufacture(user_filter),
                3: self.query_builder_screen(user_filter),
                4: self.query_builder_RAM(user_filter),
                5: self.query_builder_weight(user_filter),
                6: self.query_builder_HD_type(user_filter)
                }
        if parameter in function_map.keys():
            return function_map.get(parameter)


    @staticmethod
    def print_action(parser):
        print('Retrieving search results, please wait')



    def query_builder_ranking(self, spec_param):
        var_name = 'ranking_' + spec_param
        #print(var_name)
        URL = queries_url.ranking.get(var_name)
        return URL


    def query_builder_manufacture(self, spec_param):
        var_name = 'manufacture_'+spec_param
        #print(var_name)
        URL = queries_url.manufacture.get(var_name)
        #print(URL)
        return URL


    def query_builder_screen(self, spec_param):
        var_name = ('screen_' + spec_param).replace('-', '_2_')
        #print(var_name)
        URL = queries_url.screen.get(var_name)
        return URL


    def query_builder_RAM(self, spec_param):
        var_name = 'RAM_' + spec_param
        #print(var_name)
        URL = queries_url.RAM.get(var_name)
        return URL


    def query_builder_weight(self, spec_param):
        var_name = 'weight_' + spec_param
        var_name = var_name.replace('-', '_2_')
        #print(var_name)
        URL = queries_url.weight.get(var_name)
        #print(URL)
        return URL


    def query_builder_HD_type(self, spec_param):
        var_name = 'HD_type_' + spec_param
        URL = queries_url.HD_type.get(var_name)
        return URL



"""
choice = 2
choices = {2: queries_url.manufactures_list, 3: queries_url.screen_sizes, 4: queries_url.RAM_sizes,
                   5: queries_url.weights_list, 6: queries_url.HD_type_list}
choice_list = choices.get(choice)
print(choice_list)"""