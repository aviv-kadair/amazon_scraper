from scrapper_functions import search_results
from scrapper_functions import laptop_page
from scrapper_functions import profile

NO_PAGES=20

if __name__ == "__main__":

    links = search_results(NO_PAGES)
    users_links = laptop_page(links)
    #profile(users_links)
