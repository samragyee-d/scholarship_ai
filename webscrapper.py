# Web scraper for college essays and prompts
# Importing libraries
from bs4 import BeautifulSoup
import requests
import re

# Obtained URL and defined the headers
scrape_URL = "https://www.collegeessayguy.com/blog/scholarship-essay-examples#A"

# Dictionary for User Agent and expected language. This is used to simulate a user actually going to the website.
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5'
}

# The values in the HEADERS dictionary are sent with the HTTP GET request to the servers. The response (the website) is stored in the webpage variable
webpage = requests.get(scrape_URL, headers=HEADERS)

# This extracts the HTML code from the information stored in the webpage variable.
soup = BeautifulSoup(webpage.content, 'html.parser')

# Find all blockquote elements (essays) and pair them with their preceding "Prompt:" text
essay_sections = soup.find_all('blockquote')

for index, essay in enumerate(essay_sections, start=1):
    # Find the closest preceding paragraph containing the prompt
    prompt_paragraph = essay.find_previous('p', text=re.compile(r'^Prompt:'))
    
    if prompt_paragraph:
        # Extract and clean the prompt
        prompt_text = prompt_paragraph.text.replace("Prompt: ", "").strip()
        if '(' in prompt_text and prompt_text.endswith(')'):
            prompt_text = prompt_text[:prompt_text.rfind('(')].strip()
    else:
        # Handle cases where no prompt is found
        prompt_text = "No prompt found"

    # Extract and clean the essay text
    essay_text = essay.get_text("\n", strip=True)

    # Print the results
    print(f"Essay {index}:")
    print(f"Prompt: {prompt_text}\n")
    print(essay_text)
    print("\n" + "-" * 50 + "\n")
