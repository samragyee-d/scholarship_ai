#Webscraper for college essays and prompts
from bs4 import BeautifulSoup
import requests

scrape_URL = "https://www.collegeessayguy.com/blog/scholarship-essay-examples#A"

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
'Accept-Language':'en-US,en;q=0.5'})

webpage = requests.get(scrape_URL, headers=HEADERS)

soup = BeautifulSoup(webpage.content, 'html.parser')