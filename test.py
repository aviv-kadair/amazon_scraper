import queries_url
import scraper_class
import class_cli
URL = "https://www.amazon.com/s?k=laptop&i=computers&rh=n%3A541966%2Cn%3A565108%2Cp_72%3A1248882011&dc&qid=1594229352&rnid=1248877011&ref=sr_nr_p_72_4"
url_2 = "https://www.amazon.com/Acer-i5-9300H-MaxxAudio-Keyboard-AN515-54-5812/dp/B086KJBKDW/ref=sr_1_2?dchild=1&keywords=acer&qid=1592923186&refinements=p_72%3A1248881011&rnid=1248877011&s=computers-intl-ship&sr=1-2"
filt_results = scraper_class.Search_Page(URL)
results = filt_results.get_data()
print(results)
par = scraper_class.Parameters(url_2)
pams = par.get_param()
print(pams)
"""
def search_results(no_pages):

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
    search_page.to_csv('search_page.csv', index=False, encoding='utf-8')"""