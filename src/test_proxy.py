import requests
from bs4 import BeautifulSoup

proxy = '20.206.106.192:8123'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}

r = requests.get('https://www.bigbasket.com/pc/foodgrains-oil-masala/atta-flours-sooji/?nc=nb', headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=1)

print(r.status_code)