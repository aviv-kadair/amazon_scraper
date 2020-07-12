"""
Run the main function to update the db
Authors:
Aviv and Serah
"""

from functions import *
from time import sleep
from random import randint

pages = config.NOPAGES

if __name__ == '__main__':

    laptops = search_results(pages)
    if len(laptops[1]) > 0:
        reviews(laptops[1])
    if len(laptops[0]) > 0:
        features_laptop(laptops[0])

    try:
        output = profile()
        print(len(output))
        for i, p in enumerate(output[1:4]):

            retrieve_profile(p)
            sleep(randint(1, 10))
            print(i + 1)

        valid_features()
    except sqlite3.OperationalError:
        print('The database is blocked, try to unblock it before running the main.')
