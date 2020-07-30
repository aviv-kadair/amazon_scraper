import config
from Scraping import scraper_class
import sys
sys.path.append('../')

DB_FILENAME = config.DB_FILENAME


def search_results(url):
    """Get all the laptops from the search page, updating the Laptop in the table laptop
    if it already exists, or adding it if not.

    :param url is the link of the search page we want to scrape.

    :returns
    new_laptop: (list)
    a list of the new laptops (that do not appear before in our table laptop) with their attributes Product_name, Laptop_id, Link, in order to retrieve their features and adding them to the laptop_features table

    total_laptop: (list)
    a list with all the laptops we scrape with attributes Laptop_id, and Link for scraping the reviews
     """
    new_laptop = []
    total_laptop = []

    scraper = scraper_class.SearchPage(url)
    laptop_list = scraper.get_data()
    print(laptop_list)
    for lap in laptop_list:
        if lap.if_exist():
            lap.update_db('Price', 'Rating', 'Reviews')
        else:
            lap.add_to_db()
            new_laptop.append(lap.get_arg_db('Product_name', 'Laptop_id', 'Link'))
    for lap in laptop_list:
        total_laptop.append(lap.get_arg_db('Laptop_id', 'Link'))

    return new_laptop, total_laptop
