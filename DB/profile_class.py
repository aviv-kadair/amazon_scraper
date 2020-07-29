"""
Define an OOP Profile, with the corresponding attributes and functions for the profile of a user
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


class Profile:
    def __init__(self,user_id, ranking='', review='', votes=''):
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

    def add_to_db(self):
        """Add the Profile to the table profile of the db"""
        try:
            con=connect_to_db()
            cur = con.cursor()
            cur.execute(
                "INSERT INTO profile ( User_id, Reviewer_Ranking, Reviews, Helpful_votes, Created_at,Last_Update, Valid) VALUES ( ?, ?, ?, ?, ?,?,?)",
                [self.username, self.ranking, self.review, self.votes, datetime.now(), None, self.valid])
            con.commit()
            con.close()
            logger.info('Table profile: added -> ' + self.username)

        except Exception as e:
            logger.error(f'An error {e} occurs when adding the profile' + self.username)

    def get_arg_db(self, *args):
        """Retrieve info from the table profile of the db for this specific user """
        query = ''
        for arg in args:
            query += f'{arg} ,'

        try:
            con=connect_to_db()
            cur = con.cursor()

            get_query = "SELECT " + query[0:-1] + " FROM profile WHERE User_id=:username"
            cur.execute(get_query, {"username": self.username})
            db_output = [item for item in cur.fetchall()[0]]
            con.close()
            return db_output
        except Exception as e:
            logger.error(f'An error {e} occurs when selecting the profile' + self.username)

    def get_arg(self, *args):
        """Get the values of my Profile attributes"""
        output = []
        for option in args:
            if option == 'User_id':
                output.append(self.username)
            elif option == 'Reviewer_Ranking':
                output.append(self.ranking)
            elif option == 'Reviews':
                output.append(self.review)
            elif option == 'Helpful_votes':
                output.append(self.votes)
            elif option == 'Valid':
                output.append(self.valid)
            else:
                print('Write you arguments by using the following 10 options:\n\
                 User_id, Reviewer_Ranking, Reviews, Helpful_votes, Valid')
        return output

    def if_exist(self):
        """Check if the Profile already exists in the table profile of the db"""
        try:
            con=connect_to_db()
            cur = con.cursor()
            query = "SELECT COUNT(*) FROM profile WHERE User_id= :username"
            cur.execute(query, {'username': self.username})
            con.close()
            if cur.fetchone()[0] != 0:
                return True
            else:
                return False

        except Exception as e:
            logger.error(f'An error {e} occurs when opening the table profile')

    def update_db(self, *args):
        """Update the Profile in the table profile of the db"""
        q = ''
        val = {}
        parameters = {'Reviewer_Ranking': self.ranking, 'Reviews': self.review, 'Helpful_votes': self.votes}
        for arg in args:
            val[arg] = parameters[arg]
            q += f'{arg} = :{arg},'

        q += 'Last_Update = :date'
        val['date'] = datetime.now()
        val['username'] = self.username

        try:
            con=connect_to_db()
            cur = con.cursor()
            query = "UPDATE profile SET " + q + " WHERE User_id = :username"
            cur.execute(query, val)
            con.commit()
            con.close()
            logger.info('Table profile: updated -> ' + self.username)
        except Exception as e:
            logger.error(f'An error {e} occurs when updating the profile' + self.username)
