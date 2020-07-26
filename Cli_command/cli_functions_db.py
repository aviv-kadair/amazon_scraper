import scraper_class
from laptop_class import *

DB_FILENAME = config.DB_FILENAME

def search_results(url):
    """Get all the laptops from the search page, updating the Laptop in the table laptop
    if it already exists, or adding it if not.

    :param no_pages is the number of pages from the search page we want to scrape.

    :returns
    new_laptop: (list)
    a list of the new laptops (that do not appear before in our table laptop) with their attributes Product_name, Laptop_id, Link, in order to retrieve their features and adding them to the laptop_features table

    total_laptop: (list)
    a list with all the laptops we scrape with attributes Laptop_id, and Link for scraping the reviews
     """
    new_laptop = []
    total_laptop = []

    #my_url = f'https://www.amazon.com/s?k=laptop&s=date-desc-rank&page={count}&qid=1594213292&ref=sr_pg_2'
    scraper = scraper_class.SearchPage(url)
    laptop_list = scraper.get_data()
    for lap in laptop_list:
        if lap.if_exist():
            lap.update_db('Price', 'Rating', 'Reviews')
        else:
            lap.add_to_db()
            new_laptop.append(lap.get_arg_db('Product_name', 'Laptop_id', 'Link'))
    for lap in laptop_list:
        total_laptop.append(lap.get_arg_db('Laptop_id', 'Link'))

    return new_laptop, total_laptop


def features_laptop(new_laptop):
    """Get the features of the new laptop and add them to the table laptop_features of the db

    :param new_laptop (list)
    contains a list with the new laptop that didn't appear before in the laptop table
    """
    val = 0
    for count, new in enumerate(new_laptop):
        if new is not None:
            feat = scraper_class.Parameters(config.AMAZON + new[0][2])
            laptop = feat.get_param()
            if laptop is not None:
                laptop.add_to_db(new[0][0], new[0][1], new[0][2])

        if round(count * 100 / len(new_laptop)) % 5 == 0 and round(count * 100 / len(new_laptop)) != val:
            val = round(count * 100 / len(new_laptop))
            print(str(val) + '% of the laptop features has been downloaded')


def valid_features():
    """Check the validity of the features that were added to the table laptop_features,
    and re-scrape and update the corresponding records in case it was not valid."""
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
    """For all the laptops of the search page, check if the review already exists in the table reviews of the db
    and in case it is a new review add it to the table

    :param total_laptop (list)
    List of all the laptops from the search page
    """
    val = 0
    for count, new in enumerate(total_laptop):
        if new is not None:
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
    """Select all the profiles of the users from the reviews table"""
    with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
        with con:
            cur = con.cursor()
            cur.execute("SELECT DISTINCT Profile_link FROM reviews")
            db_output = [item for item in cur.fetchall()]
    return db_output


def retrieve_profile(db_output):
    """Update or add the user profile to the table profile of the db

    :param db_output (list)
    contains all the distinct profile links for the users who send a review to one of our laptops
    """
    pro = scraper_class.ProfileScrapper(db_output[0])
    p = pro.user_profile()
    if p.if_exist():
        p.update_db()

    else:
        p.add_to_db()


