"""
Define an OOP Review, with the corresponding attributes and functions.
Authors:
Aviv and Serah
"""

import contextlib
import sqlite3
from datetime import datetime
import config
from Logging import logger


DB_FILENAME = config.DB_FILENAME


class Review:
    def __init__(self, username, location, date, rank, profile):
        self.username = username
        self.location = location
        self.date = date
        self.rank = rank
        self.profile = profile

    def add_to_db(self, laptop_id):
        """Add the Review to the table reviews of the db"""
        try:
            with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
                with con:
                    cur = con.cursor()
                    cur.execute(
                        "INSERT INTO reviews ( Laptop_id, Username, Location, Date, UserRank, Profile_link, Created_At) VALUES ( ?, ?, ?, ?, ?,?,?)",
                        [laptop_id, self.username, self.location, self.date, self.rank, self.profile, datetime.now()])
                    con.commit()
            logger.info('Table features reviews: added -> ' + str(laptop_id))

        except Exception as e:
            logger.error(f'An error {e} occurs when adding the reviews of the laptop' + str(laptop_id))

    @staticmethod
    def get_arg_db(laptop_id, *args):
        """Retrieve info from the table reviews of the db for the specific Review"""
        query = ''
        for arg in args:
            query += f'{arg} ,'

        try:
            with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
                with con:
                    cur = con.cursor()

                    get_query = "SELECT " + query[0:-1] + " FROM reviews WHERE Laptop_id=:id"
                    cur.execute(get_query, {"id": laptop_id})
                    db_output = [item for item in cur.fetchall()]
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
            else:
                print('Write you arguments by using the following 5 options:\n\
                 Username, Location, Date, UserRank, Profile_link')
        return output

    def if_exist(self):
        """Check if the Review already exists in the table reviews of the db"""
        try:
            with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
                with con:
                    cur = con.cursor()
                    query = "SELECT COUNT(*) FROM reviews WHERE Username= :name AND Location=:loc AND Date=:date"
                    cur.execute(query, {'name': self.username, 'loc': self.location, 'date': self.date})
                    if cur.fetchone()[0] != 0:
                        return True
                    else:
                        return False
        except Exception as e:
            logger.error(f'An error {e} occurs when opening the table reviews')
