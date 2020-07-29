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
    def __init__(self,user_id, username, location, date, rank, profile, cont):
        self.user_id = user_id
        self.username = username
        self.location = location
        self.date = date
        self.rank = rank
        self.profile = profile
        self.content = cont

    def add_to_db(self, laptop_id):
        """Add the Review to the table reviews of the db"""
        try:
            con=connect_to_db()
            cur = con.cursor()
            cur.execute(
                "INSERT INTO reviews ( Laptop_id, User_id, Username, Location, Date, UserRank, Profile_link, Content, Created_At) VALUES (?, ?, ?, ?, ?, ?, ?,?,?)",
                [laptop_id, self.user_id, self.username, self.location, self.date, self.rank, self.profile, self.content, datetime.now()])
            con.commit()
            con.close()
            logger.info('Reviews added for laptop:-> ' + str(laptop_id))

        except Exception as e:
            logger.error(f'An error {e} occurs when adding the reviews of the laptop' + str(laptop_id))

    @staticmethod
    def get_arg_db(laptop_id, *args):
        """Retrieve info from the table reviews of the db for the specific Review"""
        query = ''
        for arg in args:
            query += f'{arg} ,'

        try:
            con=connect_to_db()
            cur = con.cursor()

            get_query = "SELECT " + query[0:-1] + " FROM reviews WHERE Laptop_id=:id"
            cur.execute(get_query, {"id": laptop_id})
            db_output = [item for item in cur.fetchall()]
            con.close()
            return db_output

        except Exception as e:
            logger.error(f'An error {e} occurs when selecting the reviews of the laptop' + str(laptop_id))

    def get_arg(self, *args):
        """Get the values of my Review attributes"""
        output = []
        for option in args:
            if option == 'Username':
                output.append(self.username)
            elif option == 'Location':
                output.append(self.location)
            elif option == 'Date':
                output.append(self.date)
            elif option == 'UserRank':
                output.append(self.rank)
            elif option == 'Profile_link':
                output.append(self.profile)
            elif option == 'Content':
                output.append(self.content)
            else:
                print('Write you arguments by using the following 5 options:\n\
                 Username, Location, Date, UserRank, Profile_link')
        return output

    def if_exist(self):
        """Check if the Review already exists in the table reviews of the db"""
        try:
            con=connect_to_db()
            cur = con.cursor()
            query = "SELECT COUNT(*) FROM reviews WHERE Username= :name AND Location=:loc AND Date=:date"
            cur.execute(query, {'name': self.username, 'loc': self.location, 'date': self.date})
            con.close()
            if cur.fetchone()[0] != 0:
                return True
            else:
                return False
        except Exception as e:
            logger.error(f'An error {e} occurs when opening the table reviews')
