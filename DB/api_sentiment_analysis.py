"""We add columns to the reviews table with the result of the sentiment analysis using aylien api
Author: Serah"""

import re
import requests
import config
import sys
from Createdb import connect_to_db
sys.path.append('../')

DB_FILENAME = config.DB_FILENAME




def get_reviews_content():
    """Select all the profiles of the users from the reviews table"""
    con = connect_to_db()
    cur = con.cursor()
    cur.execute("SELECT Review_id, Content FROM reviews")
    db_output = [item for item in cur.fetchall()]
    return db_output


def sentiment_analyser(review):
    url = "https://aylien-text.p.rapidapi.com/sentiment"

    querystring = {"text": review, "mode": "tweet"}

    headers = {
        'x-rapidapi-host': "aylien-text.p.rapidapi.com",
        'x-rapidapi-key': "59e71f2ca2msh163b97bedf8febbp1d0d70jsn7f90e95f54ab"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    try:
        polarity = re.findall(r'\"polarity\": \"([\w]+)\"', response.text)[0]
        subjectivity = re.findall(r'\"subjectivity\": \"([\w]+)\"', response.text)[0]
        polarity_confidence = round(float(re.findall(r'\"polarity_confidence\": ([\d.]+)', response.text)[0]), 3)
        subjectivity_confidence = round(float(re.findall(r'\"subjectivity_confidence\": ([\d.]+)', response.text)[0]), 3)
        return polarity, subjectivity, polarity_confidence, subjectivity_confidence

    except IndexError:
        print('Review too Large')
        querystring = {"text": review[:500], "mode": "tweet"}

        headers = {
            'x-rapidapi-host': "aylien-text.p.rapidapi.com",
            'x-rapidapi-key': "59e71f2ca2msh163b97bedf8febbp1d0d70jsn7f90e95f54ab"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        polarity = re.findall(r'\"polarity\": \"([\w]+)\"', response.text)[0]
        subjectivity = re.findall(r'\"subjectivity\": \"([\w]+)\"', response.text)[0]
        polarity_confidence = round(float(re.findall(r'\"polarity_confidence\": ([\d.]+)', response.text)[0]), 3)
        subjectivity_confidence = round(float(re.findall(r'\"subjectivity_confidence\": ([\d.]+)', response.text)[0]), 3)
        return polarity, subjectivity, polarity_confidence, subjectivity_confidence





def add_sentiment_to_db(review_id, polarity, subjectivity, polarity_conf, subjectivity_conf):
    con = connect_to_db()
    cur = con.cursor()
    cur.execute("""UPDATE reviews 
           SET Polarity=%s, Subjectivity=%s, Polarity_confidence=%s, Subjectivity_confidence=%s 
           WHERE Review_id =%s""",(polarity, subjectivity, polarity_conf, subjectivity_conf, review_id))
    con.commit()
    con.close()


