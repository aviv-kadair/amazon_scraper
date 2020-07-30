"""
Define an OOP Profile, with the corresponding attributes and functions for the profile of a user
Author: Serah
"""

from Createdb import connect_to_db
from datetime import datetime
import config
from Logging import logger
import sys

sys.path.append('../')

DB_FILENAME = config.DB_FILENAME


class Profile:
    def __init__(self, user_id, ranking='', review='', votes=''):
        self.username = user_id
        self.ranking = ranking
        self.review = review
        self.votes = votes

        # Check if we didn't get empty values from the scraping.
        # If valid is 0, I will retry the scraping.
        if self.review == 0 and self.ranking == 0 and self.ranking == 0:
            self.valid = 0
        else:
            self.valid = 1
        self.con = connect_to_db()
        self.cur = self.con.cursor()

    def add_to_db(self):
        """Add the Profile to the table profile of the db"""
        try:
            query = config.QUERY_INSERT_PROFILE
            records = (self.username, self.ranking, self.review, self.votes, datetime.now(), None, self.valid)
            self.cur.execute(query, records)
            self.con.commit()
            logger.info('Table profile: added -> ' + self.username)

        except Exception as e:
            logger.error(f'Adding to Profile table: {e}')

    def if_exist(self):
        """Check if the Profile already exists in the table profile of the db"""
        try:
            query = config.QUERY_PROFILE_EXIST
            self.cur.execute(query, (self.username,))
            if self.cur.fetchone()[0] != 0:
                return True
            else:
                return False

        except Exception as e:
            logger.error(f'Checking existence: {e}')

    def update_db(self):
        """Update the Profile in the table profile of the db"""
        try:
            query = config.QUERY_UPDATE_PROFILE
            records = (self.ranking, self.review, self.votes, datetime.now(), self.username)
            self.cur.execute(query, records)
            self.con.commit()
            logger.info('Table profile: updated -> ' + self.username)
        except Exception as e:
            logger.error(f'Updating table Profile {e}')
