"""
Run the main function to update the db
Authors:
Aviv and Serah
"""

from DB.functions import *
from time import sleep
from random import randint
from DB.api_sentiment_analysis import *

pages = config.NOPAGES

if __name__ == '__main__':

    laptops = search_results(pages)

    if len(laptops[0]) > 0:
        features_laptop(laptops[0])

    if len(laptops[1]) > 0:
        reviews(laptops[1])

    dboutput = get_reviews_content()

    for review_id, text in dboutput:
        if sentiment_analyser(text) is not None:
            polarity, subjectivity, polarity_conf, subjectivity_conf = sentiment_analyser(text)
            add_sentiment_to_db(review_id, polarity, subjectivity, polarity_conf, subjectivity_conf)

    try:
        output = profile()
        # print(len(output))
        for i, p in enumerate(output):
            retrieve_profile(p)
            sleep(randint(1, 10))
            print(i + 1)

        valid_features()
    except sqlite3.OperationalError:
        print('The database is blocked, try to unblock it before running the main.')
