from bs4 import BeautifulSoup
import requests
import html
from dotenv import load_dotenv

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0","Accept-Language":"en-GB,en;q=0.9",}
zillow_URL = "https://appbrewery.github.io/Zillow-Clone"

class WebScraper():
    def __init__(self)-> None:
        # scrape data
        response = requests.get(zillow_URL, headers=headers)
        response.raise_for_status()
        website_html = response.text
        # create soup
        self.soup = BeautifulSoup(website_html, "html.parser")
        # get required data
        self.all_link_elements = self.soup.select(".StyledPropertyCardDataWrapper a")

    def get_links(self):
        all_links = [link["href"] for link in self.all_link_elements]
        return all_links
    
    def get_price(self):
        prices = self.soup.select(".PropertyCardWrapper span")
        prices = [price.get_text().replace("/mo","").split("+")[0] for price in prices]
        return prices
    
    def get_address(self):
        all_address_elements = self.soup.select(".StyledPropertyCardDataWrapper address")
        all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]
        return all_addresses


