import contextlib
import sqlite3
from datetime import datetime
from configuration import config
import sys
from Logging.Logging import logger

DB_FILENAME = config.DB_FILENAME


class Profile:
    def __init__(self, username, ranking='', review='', votes=''):
        self.username = username
        self.ranking = ranking
        self.review = review
        self.votes = votes
        if self.review == 0 and self.ranking == 0 and self.ranking == 0:
            self.valid = 0
        else:
            self.valid = 1

    def add_to_db(self):

        try:
            with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
                with con:
                    cur = con.cursor()
                    cur.execute(
                        "INSERT INTO profile ( Username, Reviewer_Ranking, Reviews, Helpful_votes, Created_at,Last_Update, Valid) VALUES ( ?, ?, ?, ?, ?,?,?)",
                        [self.username, self.ranking, self.review, self.votes, datetime.now(), None, self.valid])
                    con.commit()
            logger.info('Table profile: added -> ' + self.username)

        except:
            e = sys.exc_info()[0]
            logger.error(f'An error {e} occurs when adding the profile' + self.username)

    def get_arg_db(self, *args):
        query = ''
        for arg in args:
            query += f'{arg} ,'

        try:
            with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:
                with con:
                    cur = con.cursor()

                    get_query = "SELECT " + query[0:-1] + " FROM profile WHERE Username=:username"
                    cur.execute(get_query, {"username": self.username})
                    db_output = [item for item in cur.fetchall()[0]]
                    return db_output
        except:
            e = sys.exc_info()[0]
            logger.error(f'An error {e} occurs when selecting the profile' + self.username)
            print('Write you arguments by using the profile table columns name -\n\
             Username, Reviewer_Ranking, Reviews, Helpful_votes, Created_at,Last_Update, Valid')

    def get_arg(self, *args):
        output = []
        for option in args:
            if option == 'Username':
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
                 Username, Reviewer_Ranking, Reviews, Helpful_votes, Valid')
        return output

    def if_exist(self):
        try:
            with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:
                with con:
                    cur = con.cursor()
                    query = "SELECT COUNT(*) FROM profile WHERE Username= :username"
                    cur.execute(query, {'username': self.username})
                    if cur.fetchone()[0] != 0:
                        return True
                    else:
                        return False
        except:
            e = sys.exc_info()[0]
            logger.error(f'An error {e} occurs when opening the table profile')

    def update_db(self, *args):
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
            with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:
                with con:
                    cur = con.cursor()
                    query = "UPDATE profile SET " + q + " WHERE Username = :username"
                    cur.execute(query, val)
                    con.commit()
            logger.info('Table profile: updated -> ' + self.username)
        except:
            e = sys.exc_info()[0]
            logger.error(f'An error {e} occurs when updating the profile' + self.username)
