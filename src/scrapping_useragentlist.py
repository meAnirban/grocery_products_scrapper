import requests
from bs4 import BeautifulSoup
import random

page_id = 2
user_agent_list = set()
url = 'https://developers.whatismybrowser.com/useragents/explore/software_name/googlebot/'

#get the list of bots
def makeSoup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


while True:
    url_page_id = url + str(page_id)
    soup = makeSoup(url_page_id)
    page_id += 1
    soup_bots = soup.findAll(class_ = 'code')
    if len(soup_bots) == 0:
        break
    else:
        for bots in soup_bots:
            user_agent_list.add(bots.text)


with open('data/user_agent_list/user_agent_list.txt', 'w') as f:
    for line in user_agent_list:
        f.write(f"{line}\n")