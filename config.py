DB_FILENAME = 'project.db'
PROXIES_LIST = ["128.199.109.241:8080", "113.53.230.195:3128", "125.141.200.53:80", "125.141.200.14:80",
                "128.199.200.112:138", "149.56.123.99:3128", "128.199.200.112:80", "125.141.200.39:80",
                "134.213.29.202:4444"]
HEADERS = {
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.amazon.com/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}
LAPTOP_FEATURES = ['Screen Size', 'Max Screen Resolution', 'Chipset Brand', 'Card Description',
                   'Brand Name', 'Item Weight', 'Operating System', 'Computer Memory Type', 'Batteries']

AMAZON = 'https://www.amazon.com'

BROWSER="chromedriver.exe"

NOPAGES = 20
