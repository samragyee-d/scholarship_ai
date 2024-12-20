#Getting HTML data from the college essay guy website
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
import requests
  
driver = webdriver.Chrome(executable_path='"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"')

url = "https://www.collegeessayguy.com/blog/scholarship-essay-examples#A"
driver.get(url)

driver.implicitly_wait(10)  

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())




# function to extract html document from given url 
def getHTMLdocument(url): 
      
    # request for HTML document of given url 
    response = requests.get(url) 
      
    # response will be provided in JSON format 
    return response.text 
  
scrape_url = "https://www.collegeessayguy.com/blog/scholarship-essay-examples"
html_document = getHTMLdocument(scrape_url) 

#Works

#Trying to get essays 
soup = BeautifulSoup(urlopen(scrape_url))


































