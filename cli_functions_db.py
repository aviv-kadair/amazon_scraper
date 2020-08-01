import config
import scraper_class
import sys
from Logging import logger
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
    print(f'{len(laptop_list)} laptops were found')
    try:
        for lap in laptop_list:
            if lap.if_exist():
                lap.update_db()
            else:
                lap.add_to_db()
                if lap.get_arg_db() is not None:
                    new_laptop.append(lap.get_arg_db())
        for lap in laptop_list:
            total_laptop.append(lap.get_arg_db())


    except ConnectionError:
        logger.warning("Server has reached maximum requests, please try again later")

    return new_laptop, total_laptop


#search_results("""https://www.amazon.com/s?k=laptop&i=computers&rh=n%3A541966%2Cn%3A565108%2Cp_72%3A1248882011&dc&qid=1594229352&rnid=1248877011&ref=sr_nr_p_72_4""")