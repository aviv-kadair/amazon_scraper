"""
Define an OOP Review, with the corresponding attributes and functions.
Author: Serah
"""

import contextlib
from Createdb import connect_to_db
from datetime import datetime
import config
from Logging import logger
import sys
sys.path.append('../')

DB_FILENAME = config.DB_FILENAME


class Review:
    def __init__(self, user_id, username, location, date, rank, profile, cont):

        self.user_id = user_id
        self.username = username
        self.location = location
        self.date = date
        self.rank = rank
        self.profile = profile
        self.content = cont
        self.con = connect_to_db()
        self.cur = self.con.cursor()


    def add_to_db(self, laptop_id):
        """Add the Review to the table reviews of the db"""
        try:
            query = config.QUERY_INSERT_REVIEWS
            records = (laptop_id, self.user_id, self.username, self.location, self.date, self.rank, self.profile, self.content, datetime.now())
            self.cur.execute(query, records)
            self.con.commit()
            logger.info('Reviews added for laptop:-> ' + str(laptop_id))

        except Exception as e:
            logger.error(f'Adding record to the table Review: {e}')


    def if_exist(self):
        """Check if the Review already exists in the table reviews of the db"""
        try:
            query = config.QUERY_REVIEW_EXIST
            self.cur.execute(query, (self.username, self.location, self.date))
            result = self.cur.fetchone()[0]
            if result != 0:
                return True
            else:
                return False
        except Exception as e:
            logger.error(f'Checking existence: {e}')
