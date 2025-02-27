import time

import requests
from web_scrapper import WebScrapper
from data_entry_manager import DataEntryManager

url_to_scrape = 'https://appbrewery.github.io/Zillow-Clone/'
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfC9Bg_8bRilt9emIfvVzT8GYk_r53lQNJCnSh5JHAHOj1BQg/viewform?usp=sf_link'
parser = 'html.parser'

response = requests.get(url_to_scrape)
web_page = response.text
web_scrapper = WebScrapper(web_page, parser)
data_entry_manager = DataEntryManager()
data = web_scrapper.scrap_data()

for item in data:
    data_entry_manager.start_session(form_url)
    data_entry_manager.fill_form(item[0],item[1], item[2])
    data_entry_manager.close_session()


