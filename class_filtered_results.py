URL = "https://www.amazon.com/s?k=laptop&i=computers&rh=n%3A541966%2Cn%3A565108%2Cp_72%3A1248882011&dc&qid=1594229352&rnid=1248877011&ref=sr_nr_p_72_4"
def search_results(url):

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

search_results(URL)