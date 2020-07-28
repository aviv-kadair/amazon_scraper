import requests
import config



proxies_list = config.PROXIES_LIST
headers = config.HEADERS

url = 'https://www.amazon.com/s?k=laptop&qid=1591707465&ref=sr_pg_2'
web_page = requests.get(url, headers=headers)
content = web_page.content
print(content)
