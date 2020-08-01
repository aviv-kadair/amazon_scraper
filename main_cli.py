"""
Run this file to scrape using the cli
Author: Aviv
"""
import cli_functions
from api_sentiment_analysis import *
import argparse
from functions import *
import queries_url
from cli_functions_db import *
from time import sleep
from random import randint
import sys
import sqlite3
sys.path.append('../DB')
sys.path.append('../Cli_command')

def main():
    """This main function should run in order to activate the CLI"""

    parser = argparse.ArgumentParser(description='Command Line Interface for AMAZON Laptop Search')
    args = parser.parse_args()
    parser.add_argument(dest='-filterQ')
    args.filterQ = cli_functions.filter_not()
    if args.filterQ == 'Y':
        parser.add_argument(dest='-parameter')
        parser.add_argument(dest='-user_filter')
        args.parameter, args.user_filter = cli_functions.choose_filter()
        parser.add_argument(dest='-url')
        args.url = cli_functions.function_map(args.parameter, args.user_filter)
        my_url = args.url
    else:
        my_url = queries_url.default_url

    laptops = search_results(my_url)
    if len(laptops[1]) > 0:
        reviews(laptops[1])
    if len(laptops[0]) > 0:
        features_laptop(laptops[0])

    dboutput = get_reviews_content()

    for review_id, text in dboutput:
        if sentiment_analyser(text) is not None:
            polarity, subjectivity, polarity_conf, subjectivity_conf = sentiment_analyser(text)
            add_sentiment_to_db(review_id, polarity, subjectivity, polarity_conf, subjectivity_conf)

    try:
        output = profile()
        for i, p in enumerate(output[0:4]):
            retrieve_profile(p)
            sleep(randint(1, 10))
            print(i + 1)
        valid_features()
    except sqlite3.OperationalError:
        print('The database is blocked, try to unblock it before running the main.')


if __name__ == '__main__':
    main()
