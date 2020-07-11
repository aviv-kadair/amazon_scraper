from scraping import scraper_class
from OOP.laptop_class import *
from configuration import config

pages = config.NOPAGES

DB_FILENAME = config.DB_FILENAME


def search_results(no_pages):
    new_laptop = []
    total_laptop = []
    for count in range(1, no_pages + 1):
        my_url = f'https://www.amazon.com/s?k=laptop&s=date-desc-rank&page={count}&qid=1594213292&ref=sr_pg_2'
        scraper = scraper_class.SearchPage(my_url)
        laptop_list = scraper.get_data()
        for lap in laptop_list:
            if lap.if_exist():
                lap.update_db('Price', 'Rating', 'Reviews')
            else:
                lap.add_to_db()
                new_laptop.append(lap.get_arg_db('Product_name', 'Laptop_id', 'Link'))
        for lap in laptop_list:
            total_laptop.append(lap.get_arg_db('Laptop_id', 'Link'))

        print(str(round(100 * count / no_pages)) + '% of the search page has been downloaded')
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

