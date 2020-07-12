"""
Loop over all the pages, and the associated links to retrieve all the info of the laptop using the function we have defined
Authors: Aviv & Serah
"""
import contextlib
import pandas as pd
from get_data import get_data
from laptop_description import get_description
from get_profile import user_profile
from time import sleep
from pathlib import Path
from scraper_class import Search_Page, Parameters
import sqlite3
DB_FILENAME = 'projet.db'

def search_results(no_pages):

    URL = 'https://www.amazon.com/s?k=laptops&page='
    for i in range(1, no_pages + 1):
        scraper = Search_Page(URL + str(i))
        dic = scraper.get_data()
        new_laptop = []
        for key, value in dic.items():
            link = "https://www.amazon.com" + str(value[4])
            with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con: # auto-closes
                with con: # auto-commits
                    cur = con.cursor()
                    new_laptop.append(link)

                    cur.execute("INSERT INTO laptop ( Product_Name, Price, Ratings, Reviews, Link) VALUES ( ?, ?, ?, ?, ?)",
                                        [key, value[1], value[2], value[3],link ])

                    print(str(round(100 * i /no_pages)) + '% has been downloaded')


def features_laptop(new_laptop):

    for i, u in enumerate(new_laptop):
        scraper = Parameters(u)
        dic = scraper.get_param()
        with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con: # auto-closes
            with con: # auto-commits
                cur = con.cursor()

                cur.execute("INSERT INTO laptop_features (Screen_Size, Max_Screen_Resolution, Chipset_Brand, Card_Description, Brand_Name, Item_Weight, Operating_System,Computer_Memory_Type, Batteries)\ VALUES ( ?, ?, ?, ?, ?, ?,?,?,?)",
                 [dic['Screen Size'], dic['Max Screen Resolution'], dic['Chipset Brand'], dic['Card Description'],dic['Brand Name'], dic['Item Weight'], dic['Operating System'], dic['Computer Memory Type'], dic['Batteries']])

                print(str(round(100 * i /len(new_laptop))) + '% has been downloaded')

with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con: # auto-closes
    cur = con.cursor()
    cur.execute('''
        SELECT *
        FROM laptop
        ''')
    result = cur.fetchall()
print(result)


search_results(2, 0)
