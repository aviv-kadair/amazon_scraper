import pandas as pd
from get_data import get_data
from laptop_description import get_description
from get_profile import user_profile
from time import sleep
import csv



def search_results(no_pages):
    products = []
    prices = []
    ratings = []
    reviews = []
    links = []
    for i in range(1,no_pages):
        dic = get_data(i)
        for key, value in dic.items():
            products.append(key)
            prices.append(value[1])
            ratings.append(value[2])
            reviews.append(value[3])
            links.append("https://www.amazon.com" + str(value[4]))


    search_page = pd.DataFrame({'Product Name':products, 'Price':prices, 'Ratings':ratings, 'Reviews':reviews, 'Link': links})
    search_page.to_csv('search_page.csv', index=False, encoding='utf-8')
    return links



def laptop_page(links):
    par_list = []
    names = []
    locations = []
    ranks = []
    users_links = []
    laptop_link = []
    for li in links:
        par, review = get_description(li)
        par_list.append(par)
        names.extend(review.keys())
        locations.extend([item[0] for item in list(review.values())])
        ranks.extend([item[1] for item in list(review.values())])
        users_links.extend([item[2] for item in list(review.values())])

        for i in range(len(list(review.values()))):
            laptop_link.append(li)



    reviews_info = pd.DataFrame()
    reviews_info['name']=names
    reviews_info['loc']=locations
    reviews_info['rank']=ranks
    reviews_info['link']=users_links
    reviews_info['laptop']=laptop_link
    reviews_info.to_csv('reviews_info.csv', index=False, encoding='utf-8')
    laptop_features = pd.DataFrame(par_list)
    laptop_features.to_csv('laptop_features.csv', index=False, encoding='utf-8')

    return users_links




def profile(users_links):
    users_data = pd.DataFrame()
    rank=[]
    rev = []
    help_votes=[]
    for link in users_links:
        sleep(2)
        reviewer_ranking,reviews,votes = user_profile(link)
        rank.append(reviewer_ranking)
        rev.append(reviews)
        help_votes.append(votes)
    users_data['Reviewer_Ranking']= rank
    users_data['Reviews']=rev
    users_data['Helpful_votes']=help_votes
    print(users_data)
    users_data.to_csv('users_data.csv', index=False, encoding='utf-8')



