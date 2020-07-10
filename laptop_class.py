import contextlib
import sqlite3
from datetime import datetime
import config
from Logging import logger
import sys

DB_FILENAME = config.DB_FILENAME


class Laptop:
    def __init__(self, name, price, rating, reviews, link):
        self.name = name
        self.price = price
        self.rating = rating
        self.reviews = reviews
        self.link = link

        if self.price != 0 or self.rating != -1 or self.reviews != 0:
            self.valid = 1
        else:
            self.valid = 0

    def add_to_db(self):

        try:
            with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
                with con:
                    cur = con.cursor()
                    cur.execute(
                        "INSERT INTO laptop ( Product_Name, Price, Rating, Reviews, Link, Created_At, Last_Update, Valid) VALUES (?, ?, ?, ?, ?, ?,?,?)",
                        [self.name, self.price, self.rating, self.reviews, self.link, datetime.now(), None, self.valid])
                con.commit()
            logger.info('Table laptop: added -> ' + self.name)
        except:
            e = sys.exc_info()[0]
            logger.error(f'An error {e} occurs when adding the laptop ' + self.name)

    def update_db(self, *args):
        q = ''
        val = {}
        parameter = {'Price': self.price, 'Rating': self.rating, 'Reviews': self.reviews, 'Link': self.link}
        for arg in args:
            val[arg] = parameter[arg]
            q += f'{arg} = :{arg},'

        q += 'Last_Update = :date'
        val['date'] = datetime.now()
        val['name'] = self.name

        try:
            with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
                with con:
                    cur = con.cursor()
                    query = "UPDATE laptop SET " + q + " WHERE Product_Name = :name"
                    cur.execute(query, val)
                    con.commit()
            logger.info('Table laptop: updated -> ' + self.name)
        except:
            e = sys.exc_info()[0]
            logger.error(f'An error {e} occurs when updating the laptop ' + self.name)

    def get_arg_db(self, *args):
        query = ''
        for arg in args:
            query += f'{arg} ,'

        try:
            with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
                with con:
                    cur = con.cursor()

                    get_query = "SELECT " + query[0:-1] + " FROM laptop WHERE Product_Name=:name"
                    cur.execute(get_query, {"name": self.name})
                    db_output = [item for item in cur.fetchall()]
                    return db_output
        except:
            e = sys.exc_info()[0]
            logger.error(f'An error {e} occurs when selecting the laptop' + self.name)
            print('Write you arguments by using the laptop table columns name -\n\
             Laptop_id, Product_Name, Price, Rating, Reviews, Link, Created_At, Last_Update, Valid')

    def get_arg(self, *args):
        output = []
        for option in args:
            if option == 'Price':
                output.append(self.price)
            elif option == 'Name':
                output.append(self.name)
            elif option == 'Reviews':
                output.append(self.reviews)
            elif option == 'Rating':
                output.append(self.rating)
            elif option == 'Link':
                output.append(self.link)
            elif option == 'Valid':
                output.append(self.valid)
            else:
                print('Write you arguments by using the following 5 options:\n\
                 Name, Price, Reviews, Link, Valid')
        return output

    def if_exist(self):
        try:
            with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:
                with con:
                    cur = con.cursor()
                    query = "SELECT COUNT(*) FROM laptop WHERE Product_Name= :name "
                    cur.execute(query, {'name': self.name})
                    if cur.fetchone()[0] != 0:
                        return True
                    else:
                        return False
        except:
            e = sys.exc_info()[0]
            logger.error(f'An error {e} occurs when opening the table laptop')
