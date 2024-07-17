import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Function to scrape articles from The Hindu
def scrape_the_hindu():
    url = 'https://www.thehindu.com/archive/web/2023/06/24/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('h2')
    data = []
    for article in articles:
        title = article.text.strip()
        link = article.find('a')['href']
        data.append([title, '2023-06-24', link])
    return data

# Function to scrape articles from Hindustan Times
def scrape_hindustan_times():
    url = 'https://www.hindustantimes.com/archive/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', class_='news')
    data = []
    for article in articles:
        title = article.find('a').text.strip()
        link = article.find('a')['href']
        data.append([title, '2023-06-24', link])
    return data

# Extend the functions for other newspapers...

# Scrape data
all_articles = []
all_articles.extend(scrape_the_hindu())
all_articles.extend(scrape_hindustan_times())

# Convert to DataFrame
df = pd.DataFrame(all_articles, columns=['Title', 'Date', 'Link'])

# Save to CSV
df.to_csv('news_articles.csv', index=False)

print("Data scraping completed and saved to news_articles.csv")
