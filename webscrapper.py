# Web scraper for college essays and prompts
# Importing libraries
from bs4 import BeautifulSoup
import requests

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

# Extract all elements matching prompts or essays
content = soup.find_all(['p', 'blockquote'])

# Initialize variables for tracking
essays = []
current_prompt = None

# Iterate through the content in document order
for element in content:
    if element.name == 'p' and element.text.startswith("Prompt:"):
        # Extract and clean the prompt
        prompt_text = element.text.replace("Prompt: ", "").strip()
        if '(' in prompt_text and prompt_text.endswith(')'):
            prompt_text = prompt_text[:prompt_text.rfind('(')].strip()
        current_prompt = prompt_text
    elif element.name == 'blockquote':
        # Only add the essay if a prompt exists
        if current_prompt:
            essay_text = element.get_text("\n", strip=True)
            essays.append((current_prompt, essay_text))
            current_prompt = None  # Reset after pairing
        else:
            # Skip essays without prompts
            continue

# Print results
for index, (prompt, essay) in enumerate(essays, start=1):
    print(f"Essay {index}:")
    print(f"Prompt: {prompt}\n")
    print(essay)
    print("\n" + "-" * 50 + "\n")
