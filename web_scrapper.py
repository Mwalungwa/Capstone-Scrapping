from bs4 import BeautifulSoup
import re

class WebScrapper:

    def __init__(self, content, parser):
        self.soup = BeautifulSoup(content, parser)

    def scrap_data(self):
        rentals = []
        cards = self.soup.find_all(name='div', class_='StyledCard-c11n-8-84')
        for card in cards:
            unformatted_price = card.find(name='span', class_ = 'PropertyCardWrapper__StyledPriceLine').getText()
            if '+' in unformatted_price:
                formatted_price = re.sub(r'\+.*', '', unformatted_price)
            else:
                formatted_price = re.sub(r'/.*', '', unformatted_price)
            location = card.find(name='a', class_ = 'StyledPropertyCardDataArea-anchor').getText().strip().replace('|', '')
            url = card.find(name='a', class_ = 'StyledPropertyCardDataArea-anchor').get('href')
            rental = [location, formatted_price, url]
            rentals.append(rental)
        return rentals



