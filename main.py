import requests
import news_sources
import news_story
from bs4 import BeautifulSoup

website_url= 'https://www.foxnews.com/politics'
response = requests.get(website_url)
response_text =response.text
soup = BeautifulSoup(response_text,"html.parser")
main_headlines= soup.find_all('h2')
for headline in main_headlines:
    print (headline.get_text())
