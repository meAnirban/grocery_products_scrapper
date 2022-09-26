import sys
import requests
from bs4 import BeautifulSoup
import random
import os
import yaml
import csv
import pandas as pd

from src.makesoup import MakeSoup
from src.bigbasket_scrapper import BigbasketScrapper

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)


class BigbasketCrawler:
    
    def __init__(self):
        #'data/url_files/bigbasket.csv' 
        self.bigbasket_main_urls = pd.read_csv(config['path_params']['url_files_path'] + config['files_names']['bigbasket_main_url_file'], sep ='|')
        self.bigbasket_scrapped_urls = list()
    
    def get_unscrapped_urls(self):
        if os.path.exists(config['path_params']['url_files_path'] + config['files_names']['bigbasket_scrapped_urls']):
            df3 = self.bigbasket_main_urls.merge(pd.read_csv('../' + config['path_params']['url_files_path'] + config['files_names']['bigbasket_scrapped_urls'], sep = '|'), on='link')
            self.bigbasket_main_urls = self.bigbasket_main_urls[~self.bigbasket_main_urls['link'].isin(df3['link'])]
        
        return self.bigbasket_main_urls
    
    def get_soup(self):
        url_list = self.get_unscrapped_urls()
        url_list = url_list[~url_list['category'].isin(['Fresh Vegetables', 'Fresh Fruits', 'Organic Fruits & Vegetables'])].values
        
        for sub_category in url_list:
            print(sub_category)
            soup = MakeSoup(sub_category[2])
            scrapper = BigbasketScrapper(soup.makeSoup_url())
            scrapper.get_images()
            self.bigbasket_scrapped_urls.append(sub_category)
        pd.DataFrame(self.bigbasket_scrapped_urls, columns=['category', 'sub_category', 'link']).to_csv(config['path_params']['url_files_path'] + config['files_names']['bigbasket_scrapped_urls'], sep = '|', index= False)
        