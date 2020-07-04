"""Run all of the project scripts to build the databases
Authors: Aviv & Serah
"""

from scrapper_functions import search_results
from scrapper_functions import laptop_page
from scrapper_functions import profile
import pandas as pd

NO_PAGES = 20

if __name__ == "__main__":
    """Run all the function from the scrapper_functions"""

    #get the data from the laptop search result for all the pages
    #search_results(NO_PAGES)

    #get all the features and reviewes of the laptops obtained previously.
    data = pd.read_csv("search_page.csv")
    links = data["Link"]
    users_links = laptop_page(links)

    #Get the profile links of laptop reviewers
    #The scraping is done gradually in order to avoid TimeOut error from the server.
'''
    data2 = pd.read_csv("reviews_info.csv")
    profile_links = data2['link']
    profile(profile_links[1:3])
'''

