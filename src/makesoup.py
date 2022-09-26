import sys
import requests
from bs4 import BeautifulSoup
import random
import os
import yaml
import csv
import pandas as pd
import urllib
import urllib.request
import time

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)


class MakeSoup:
    
    def __init__(self, url):
        self.url = url
        
    def GET_UA(self):
        #'data/user_agent_list/user_agent_list.txt' 
        with open(config['path_params']['user_agent_path'] + config['files_names']['user_agent_file']) as f:
            user_agents_list = f.readlines()
            
        return random.choice(user_agents_list)
        
    def makeSoup_url(self):
        headers = {'User-Agent': self.GET_UA()[:-1]}
        r = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        return soup