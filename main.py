"""Run all the project to build all the databases
Authors: Aviv & Serah
"""

from scrapper_functions import search_results
from scrapper_functions import laptop_page
from scrapper_functions import profile
import pandas as pd

NO_PAGES = 20

if __name__ == "__main__":
    """Run all the function from the scrapper_functions"""

    #search_results(NO_PAGES)

    """data = pd.read_csv("search_page.csv")
    links = data["Link"]
    users_links = laptop_page(links)"""

    data2 = pd.read_csv("reviews_info.csv")
    profile_links = data2['link']
    profile(profile_links[10:12])





