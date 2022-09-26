import requests
from bs4 import BeautifulSoup
import random
import os
import yaml
import csv
import pandas as pd

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)


def GET_UA():
    #'data/user_agent_list/user_agent_list.txt' 
    with open(config['path_params']['user_agent_path'] + config['files_names']['user_agent_file']) as f:
        user_agents_list = f.readlines()
    
    return random.choice(user_agents_list)


#get the list of free proxies
def makeSoup(url):
    headers = {'User-Agent': GET_UA()[:-1]}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


soup = makeSoup(config['platform_urls']['bigbasket']['all_categories_url'])

categories = soup.findAll(class_ = 'DropDownColum')

if len(categories) > 0 :
    link_list = list()
    
    for cate_ in categories:
        category = cate_.find('a').text
        sub_categories = cate_.find_all('li')
        for sub_cate_ in sub_categories:
            sub_category = sub_cate_.text
            sub_category_link = config['platform_urls']['bigbasket']['main_url'] + sub_cate_.find_all('a', href=True)[0]['href']
            link_list.append((category, sub_category, sub_category_link))
            
    #'data/url_files/bigbasket.csv' 
    pd.DataFrame(link_list, columns=['category', 'sub_category', 'link']).to_csv(config['path_params']['url_files_path'] + config['files_names']['bigbasket_main_url_file'], sep = '|', index= False)

#with open('data/url_files/bigbasket.csv','w', newline ='') as out:
#    csv_out=csv.writer(out)
#    csv_out.writerow(link_list)

