from selenium import webdriver
from bs4 import BeautifulSoup
import time


# Set up the WebDriver (update the path to your downloaded driver)
driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

# Open the webpage
url = "https://www.collegeessayguy.com/blog/scholarship-essay-examples#A"
driver.get(url)

# Let the page load completely
time.sleep(5) # Let the user actually see something!

# Get the page source
html = driver.page_source

# Parse the HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Print the parsed HTML (optional)
print(soup.prettify())

# Close the browser
driver.quit()
