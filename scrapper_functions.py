"""
Loop over all the pages, and the associated links to retrieve all the info of the laptop using the function we have defined
Authors: Aviv & Serah
"""

import pandas as pd
from get_data import get_data
from laptop_description import get_description
from get_profile import user_profile
from time import sleep
from pathlib import Path


def search_results(no_pages):
    """Save the info of all of the laptop search page in a csv

    :param
    no_pages (int): the number of pages that we want to retrieve data from

    :returns
    - csv file with all the info of the laptop search
    - all the links for the laptop page description for each laptop
    """

    products = []
    prices = []
    ratings = []
    reviews = []
    links = []
    for i in range(1, no_pages + 1):
        dic = get_data(i)
        print(str(100 * i / no_pages) + '% of the search page has been retrieved')
        for key, value in dic.items():
            products.append(key)
            prices.append(value[1])
            ratings.append(value[2])
            reviews.append(value[3])
            links.append("https://www.amazon.com" + str(value[4]))

    search_page = pd.DataFrame({'Product Name': products, 'Price': prices, 'Ratings': ratings, 'Reviews': reviews, 'Link': links})
    search_page.to_csv('search_page.csv', index=False, encoding='utf-8')
    return links


def laptop_page(links):
    """Retrieve all the info for all the laptop pages description

    :param
    links (list): all the links for all the laptop page description

    :returns
    users_links (list): all the users profile links
    (two csv file one with all the parameters for each laptop and second one with the reviews details
    """
    par_list = []
    names = []
    locations = []
    ranks = []
    users_links = []
    laptop_link = []
    stage = 0
    for i, li in enumerate(links):
        if round(100*i/len(links)) % 5 == 0 and round(100*i/len(links)) != stage:
            stage = round(100*i/len(links))
            print(str(stage) + '% of the laptop links has been retrieved')
        par, review = get_description(li)
        par_list.append(par)
        names.extend(review.keys())
        locations.extend([item[0] for item in list(review.values())])
        ranks.extend([item[1] for item in list(review.values())])
        users_links.extend([item[2] for item in list(review.values())])

        for i in range(len(list(review.values()))):
            laptop_link.append(li)

    reviews_info = pd.DataFrame()
    reviews_info['name'] = names
    reviews_info['loc'] = locations
    reviews_info['rank'] = ranks
    reviews_info['link'] = users_links
    reviews_info['laptop'] = laptop_link
    reviews_info.to_csv('reviews_info.csv', index=False, encoding='utf-8')
    laptop_features = pd.DataFrame(par_list)
    laptop_features.to_csv('laptop_features.csv', index=False, encoding='utf-8')

    return users_links


def profile(users_links):
    """Get the data from the user profiles

    :param
    users_links (list): all the profile links of users that reviewed laptops

    :return
    csv file with all the details on each profile that gave a review on a laptop
    """
    my_file = Path('users_data.csv')
    if my_file.is_file():
        users_data = pd.read_csv('users_data.csv')
    else:
        users_data = pd.DataFrame()
    rank = []
    rev = []
    help_votes = []
    profile_link = []
    for i, link in enumerate(users_links):
        print(f'{i+1} profile(s) on {len(users_links)} have been retrieved')
        reviewer_ranking, reviews, votes = user_profile(link)
        rank.append(reviewer_ranking)
        rev.append(reviews)
        help_votes.append(votes)
        profile_link.append(link)
        sleep(2)
    users_data = users_data.append(pd.DataFrame({'Reviewer_Ranking': rank, 'Reviews': rev, 'Helpful_votes': help_votes, 'Profile_link': profile_link}), ignore_index= True)
    #users_data['Reviewer_Ranking'] = rank
    #users_data['Reviews'] = rev
    #users_data['Helpful_votes'] = help_votes
    users_data.to_csv('users_data.csv', index=False, encoding='utf-8')

    return rank, rev, help_votes
