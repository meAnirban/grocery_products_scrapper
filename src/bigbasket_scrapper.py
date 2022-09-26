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



class BigbasketScrapper:
    
    def __init__(self, soup):
        self.soup = soup
        self.product_list = list()
        
    def get_images(self):
        html_list = self.soup.findAll('script')[4].text.replace('\\', '')[self.soup.findAll('script')[4].text.replace('\\', '').index('{'):-2].split(',')
        
        i=0

        while i < len(html_list):
            if 'mimage' in html_list[i]:
                image_link = html_list[i].split('"')[3].strip()
                i += 1
                while True:
                    if 'desc' in html_list[i]:
                        product_name = html_list[i].split('"')[3].strip()
                    elif 'w2' in html_list[i]:
                        qty = html_list[i].split('"')[3].strip()
                    elif 'brandName' in html_list[i]:
                        brandname = html_list[i].split('"')[3].strip()
                        break
                    i += 1
            
                self.product_list.append((brandname, product_name, qty, image_link))
                
                tempCheck = image_link.split('.')
                check = str(tempCheck[len(tempCheck) -1])
                ImageType = ".jpeg"
                
                if (check == "jpg" or check == "jpeg" or check == "png"):
                    
                    if check == "jpg" or check == "jpeg":
                        ImageType = ".jpeg"
                    else:
                        ImageType = ".png"
                        
                    if not os.path.exists(config['path_params']['output_images_path']  + '/' + brandname + '/' + product_name):
                        os.makedirs(config['path_params']['output_images_path'] + '/' + brandname + '/' + product_name)
                    
                    time.sleep(random.randrange(2, 10))
                    imagefile = open(config['path_params']['output_images_path']  + '/' + brandname + '/' + product_name + ImageType, 'wb')
                    imagefile.write(urllib.request.urlopen(image_link).read())
                    imagefile.close()
                i +=1
            else:
                i += 1