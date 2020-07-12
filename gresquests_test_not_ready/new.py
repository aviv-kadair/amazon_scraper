"""
This is a copy of functions.py with a little change in the first function with the implementation of grequests.
It is still in progress.
Authors:
Aviv and Serah
"""
import grequests
import scraper_class
from laptop_class import *
import config
import random
from bs4 import BeautifulSoup
import time

pages = config.NOPAGES

DB_FILENAME = config.DB_FILENAME
proxies_list = config.PROXIES_LIST


def search_results(no_pages):
    new_laptop = []
    total_laptop = []
    my_urls = []
    for count in range(1, 20):
        my_urls.append(f'https://www.amazon.com/s?k=laptops&page={count}&qid=1594392240&ref=sr_pg_{count}')
    proxy = {'http': random.choice(proxies_list)}
    rs = (grequests.get(u, headers={"user-agent": config.HEADERS}, proxies=proxy) for u in my_urls)
    for r in grequests.imap(rs, size=10):
        content = r.content
        soup = BeautifulSoup(content, features="lxml")
        scraper = scraper_class.SearchPage(soup)
        laptop_list = scraper.get_data()
        for lap in laptop_list:
            if lap.if_exist():
                lap.update_db('Price', 'Rating', 'Reviews')
            else:
                lap.add_to_db()
                new_laptop.append(lap.get_arg_db('Product_name', 'Laptop_id', 'Link'))
        for lap in laptop_list:
            total_laptop.append(lap.get_arg_db('Laptop_id', 'Link'))

        print(str(round(100 * 1 / no_pages)) + '% of the search page has been downloaded')
    return new_laptop, total_laptop


def features_laptop(new_laptop):
    val = 0
    for count, new in enumerate(new_laptop):
        feat = scraper_class.Parameters(config.AMAZON + new[0][2])
        laptop = feat.get_param()
        if laptop is not None:
            laptop.add_to_db(new[0][0], new[0][1], new[0][2])

        if round(count * 100 / len(new_laptop)) % 5 == 0 and round(count * 100 / len(new_laptop)) != val:
            val = round(count * 100 / len(new_laptop))
            print(str(val) + '% of the laptop features has been downloaded')


def valid_features():
    with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
        with con:
            cur = con.cursor()
            cur.execute("SELECT Link, Laptop_id FROM laptop_features WHERE Valid=0")
            db_output = [item for item in cur.fetchall()]
            for my_url in db_output:
                feat = scraper_class.Parameters(config.AMAZON + my_url[0])
                laptop = feat.get_param()
                laptop.update_db(my_url[1])


def reviews(total_laptop):
    val = 0
    for count, new in enumerate(total_laptop):
        rev = scraper_class.Reviews(config.AMAZON + new[0][1])
        laptop = rev.get_reviews()
        for lap in laptop:
            if lap is not None:
                if not lap.if_exist():
                    lap.add_to_db(new[0][0])

        if round(count * 100 / len(total_laptop)) % 5 == 0 and round(count * 100 / len(total_laptop)) != val:
            val = round(count * 100 / len(total_laptop))
            print(str(val) + '% of the reviews has been downloaded')


def profile():
    with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
        with con:
            cur = con.cursor()
            cur.execute("SELECT Profile_link FROM reviews")
            db_output = [item for item in cur.fetchall()]
    return db_output


def retrieve_profile(db_output):
    pro = scraper_class.ProfileScrapper(db_output[0])
    p = pro.user_profile()
    if p.if_exist():
        p.update_db()

    else:
        p.add_to_db()


before = time.time()
laptops = search_results(pages)
after = time.time()
print(after - before)
