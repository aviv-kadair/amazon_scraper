from running_functions.functions import *
from time import sleep
from random import randint

pages = config.NOPAGES

if __name__ == '__main__':
    laptops = search_results(pages)
    if set(laptops[1]) != {None}:
        reviews(laptops[1])
    if set(laptops[0]) != {None} and laptops[0] is not None:
        features_laptop(laptops[0])
    try:
        output = profile()
        for i, p in enumerate(output[0:3]):
            retrieve_profile(p)
            sleep(randint(1, 10))
            print(i + 1)
        valid_features()
    except sqlite3.OperationalError:
        print('The database is blocked, try to unblock it before running the main.')




