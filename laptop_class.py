"""
Define an OOP Laptop, with the corresponding attributes and functions.
Author: Serah
"""

from Createdb import connect_to_db
from datetime import datetime
import config
from Logging import logger
import sys

sys.path.append('../')

DB_FILENAME = config.DB_FILENAME


class Laptop:
    def __init__(self, name, price, rating, reviews, link):

        self.name = str(name.encode('utf-8', errors='ignore').decode('utf-8'))

        self.price = price
        self.rating = rating
        self.reviews = reviews
        self.link = link

        # Check if we didn't get empty values from the scraping.
        # If valid is 0, I will retry the scraping.
        if self.price != 0 or self.rating != -1 or self.reviews != 0:
            self.valid = 1
        else:
            self.valid = 0

        self.con = connect_to_db()
        self.cur = self.con.cursor()

    def add_to_db(self):
        """Add the Laptop to the table laptop of the db"""
        try:
            query = config.QUERY_INSERT_LAPTOP
            records = (self.name, self.price, self.rating, self.reviews, self.link, datetime.now(), None, self.valid)
            self.cur.execute(query, records)
            self.con.commit()
            logger.info('Table laptop: added -> ' + self.name)
        except Exception as e:
            logger.error(f'Adding record to table laptop: {e} ')

    def update_db(self):
        """Update the Laptop in the table laptop of the db"""
        try:
            query = config.QUERY_UPDATE_LAPTOP
            self.cur.execute(query, (self.price, self.rating, self.reviews, datetime.now(), self.name))
            self.con.commit()
            logger.info('Table laptop: updated -> ' + self.name)
        except Exception as e:
            logger.error(f'Updating table laptop: {e} ')

    def get_arg_db(self):
        """Retrieve info from the table laptop of the db for the specific laptop"""
        try:
            get_query = config.QUERY_GET_ARG
            self.cur.execute(get_query, (self.name,))
            db_output = [item for item in self.cur.fetchall()]
            return db_output
        except Exception as e:
            logger.error(f'Selecting arguments from laptop table: {e} ')

    def if_exist(self):
        """Check if the Laptop already exists in the table laptop of the db"""
        try:
            query = config.QUERY_LAPTOP_EXIST
            self.cur.execute(query, (self.name,))
            result = self.cur.fetchone()[0]
            if result != 0:
                return True
            else:
                return False

        except Exception as e:
            logger.error(f'Checking existence: {e} ')
