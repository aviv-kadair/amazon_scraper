from running_functions.functions import *
from time import sleep
from random import randint

pages = config.NOPAGES

if __name__ == '__main__':
    laptops = search_results(pages)

    reviews(laptops[1])
    features_laptop(laptops[0])
    output = profile()
    for i, p in enumerate(output[0:3]):
        retrieve_profile(p)
        sleep(randint(10, 100))
        print(i + 1)

    valid_features()
