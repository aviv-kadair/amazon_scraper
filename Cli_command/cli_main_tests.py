import requests
import argparse
import queries_url
import scraper_class
import class_cli
import cli_class_tests
import requests
from cli_functions_db import *
import argparse
import queries_url
import scraper_class
import class_cli
import csv
from time import sleep
from random import randint

def main():
    """This main function should run in order to activate the CLI"""
    #parser = cli_class_tests.cli_tool_test()
    parser = argparse.ArgumentParser()
    parser.add_argument('-filterQ', action=cli_class_tests.cli_tool_test)
    args = parser.parse_args()
    args.filterQ = input('Would you like to filter results? Y/N : ').upper()
    if args.filterQ == 'Y':
        #cli_tool.print_action(parser,args.filterQ)
        parser.add_argument('-parameter', action=cli_class_tests.cli_tool_test)
        parser.add_argument('-spec', action=cli_class_tests.cli_tool_test)
        args.parameter, args.spec = cli_class_tests.cli_tool_test.choose_filter(parser)
        URL = cli_class_tests.cli_tool_test.function_map(args.parameter, args.spec)
        print(URL)
    else:
        URL = queries_url.default_url
    try:
        res = scraper_class.SearchPage(URL)
        class_cli.cli_tool.print_action(parser)
    except requests.exceptions.MissingSchema:
        print('Filtering choice was not recognised, exiting')
        quit()
    items = res.get_data()
    if items:
        link_list = []
        print('The following results match your search parameters: ')
        laptop_names = []
        for result in items:
            print(f'Laptop name: {result.name}')

            laptop_names.append(result.name)
            link_list.append(result.link)


"""
        #args.parameter = input(f'Choose a filter from the following list: {queries_url.filtering_choice} ')
        parser.add_argument('-spec_param', action=class_cli.cli_tool)
        if args.parameter == '1':
            args.spec_param = input('Choose a minimal item ranking, from 1 to 4: ')
            if args.spec_param not in range(1,5):
                args.spec_param = input('Ranking was not recognised, please try again: ')
            URL = class_cli.cli_tool.query_builder_ranking(parser,'ranking', args.spec_param)
        elif args.parameter == '2':
            manufactures = queries_url.manufactures_list
            args.spec_param = input(f'Choose a manufacturer, from the following list: {manufactures} ')
            if args.spec_param not in manufactures:
                args.spec_param = input('Manufacturer was not recognised, please try again: ')
            URL = class_cli.cli_tool.query_builder_manufacture(parser,'manufacture', args.spec_param)

        elif args.parameter == '3':
            screen_sizes = queries_url.screen_sizes
            args.spec_param = input(f'Choose a screen size, from the following list: {screen_sizes} ')
            if args.spec_param not in screen_sizes:
                args.spec_param = input('Screen size was not recognised, please try again: ')
            URL = class_cli.cli_tool.query_builder_screen(parser,'screen', args.spec_param)
        elif args.parameter == '4':
            RAM_sizes = queries_url.RAM_sizes
            args.spec_param = input(f'Choose RAM size, from the following list: {RAM_sizes} ')
            if args.spec_param not in RAM_sizes:
                args.spec_param = input('RAM size was not recognised, please try again: ')
            URL = class_cli.cli_tool.query_builder_RAM(parser,'RAM', args.spec_param)
        elif args.parameter == '5':
            weights = queries_url.weights_list
            args.spec_param = input(f'Choose desired weight, from the following list: {weights} ')
            if args.spec_param not in weights:
                args.spec_param = input('Weight was not recognised, please try again: ')
            URL = class_cli.cli_tool.query_builder_weight(parser,'weight', args.spec_param)
        elif args.parameter == '6':
            HD_type = queries_url.HD_type_list
            args.spec_param = input(f'Choose desired hard drive type, from the following list: {HD_type} ')
            if args.spec_param not in HD_type:
                args.spec_param = input('HD type was not recognised, please try again: ')
            URL = class_cli.cli_tool.query_builder_HD_type(parser,'HD_type', args.spec_param)"""



if __name__ == '__main__':
    main()