#Webscraper for college essays and prompts

#Importing libraries
from bs4 import BeautifulSoup
import requests
import bs4
import re

#Obtained URL and defined the headers
scrape_URL = "https://www.collegeessayguy.com/blog/scholarship-essay-examples#A"

#Dictionary for User Agent and expected language. This is used to simulate a user actually going to the website. 
HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
'Accept-Language':'en-US,en;q=0.5'}

#The values in the HEADERS dictionary are sent with the HTTP GET request to the servers. The response (the website) is stored in the webpage variable 
webpage = requests.get(scrape_URL, headers=HEADERS)

#This extracts the html code from the information stored in the webpage variable.

soup = bs4.BeautifulSoup(webpage.content, 'html.parser')

text = 'Prompt: '
 
# Search by text with the help of lambda function
gfg = soup.find_all(lambda tag: tag.name == "p" and text in tag.text)

prompts = []
for i in gfg:
    if i.text.startswith('Prompt:'):
        prompts.append(i.text)

ind_prompts = []

for prompt in prompts:
    # Remove "Prompt: "
    clean_prompt = prompt.replace("Prompt: ", "").strip()
    
    # Remove word count info (anything in parentheses at the end)
    if '(' in clean_prompt and clean_prompt.endswith(')'):
        clean_prompt = clean_prompt[:clean_prompt.rfind('(')].strip()
    
    ind_prompts.append(clean_prompt)

#print(ind_prompts)

no_dupes = list(set(ind_prompts))
#print(no_dupes)

# Maintaining order
no_dupes_ordered = []
for item in ind_prompts:
    if item not in no_dupes_ordered:
        no_dupes_ordered.append(item)
print("This is the no duplicates this: " + str(no_dupes_ordered))



