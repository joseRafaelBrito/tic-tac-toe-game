"""
Web Scraper Documentation
------------------------

This script provides a framework for web scraping using Python's requests and BeautifulSoup libraries.

How to Use:
1. Install required packages:
   pip install -r requirements.txt

2. To scrape a new website:
   - Modify the scrape_quotes() method or create a new method
   - Update the selectors (class names, tags) based on the target website's HTML structure
   - Add appropriate error handling and rate limiting if needed

3. For API-based scraping:
   - Replace the get_page() method with API calls
   - Add API key handling
   - Update the data processing logic

Important Notes:
- Always check the website's robots.txt and terms of service
- Add appropriate delays between requests
- Respect rate limits
- Handle errors gracefully
- Store API keys securely (not in the code)

Example API Integration:
------------------------
To add API scraping, modify the get_page() method:

def get_page(self, url, api_key=None):
    headers = {
        'User-Agent': 'Your User Agent',
        'Authorization': f'Bearer {api_key}',  # For API authentication
        'Accept': 'application/json'  # For API responses
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()  # For API responses
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
"""

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os
import time  # For rate limiting

class WebScraper:
    def __init__(self):
        # Customize headers based on the target website
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        # Add API key here if needed
        # self.api_key = "YOUR_API_KEY"

    def get_page(self, url):
        """
        Fetch webpage content
        Modify this method for API-based scraping:
        1. Add API key parameter
        2. Update headers for API authentication
        3. Handle API-specific response formats
        """
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            time.sleep(1)  # Add delay between requests
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching the page: {e}")
            return None

    def scrape_quotes(self, url="https://quotes.toscrape.com"):
        """
        Example scraping method for quotes.toscrape.com
        To scrape a different website:
        1. Update the URL
        2. Modify the selectors (class names, tags)
        3. Update the data structure
        """
        html = self.get_page(url)
        if not html:
            return []

        soup = BeautifulSoup(html, 'html.parser')
        quotes = []

        # Update these selectors based on the target website's HTML structure
        for quote in soup.find_all('div', class_='quote'):
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            
            quotes.append({
                'text': text,
                'author': author,
                'tags': tags
            })

        return quotes

    def scrape_news(self, url="https://news.ycombinator.com/"):
        """
        Scrape news headlines from Hacker News
        """
        html = self.get_page(url)
        if not html:
            return []

        soup = BeautifulSoup(html, 'html.parser')
        news_items = []

        # Find all news items
        for item in soup.find_all('tr', class_='athing'):
            title_elem = item.find('span', class_='titleline')
            if title_elem:
                title = title_elem.find('a').text
                link = title_elem.find('a')['href']
                
                # Get points and comments
                next_row = item.find_next_sibling('tr')
                if next_row:
                    score = next_row.find('span', class_='score')
                    points = score.text if score else '0 points'
                    
                    comments = next_row.find('a', string=lambda text: text and 'comment' in text.lower())
                    num_comments = comments.text if comments else '0 comments'
                else:
                    points = '0 points'
                    num_comments = '0 comments'
                
                news_items.append({
                    'title': title,
                    'link': link,
                    'points': points,
                    'comments': num_comments
                })

        return news_items

    def save_to_csv(self, data, filename=None):
        """Save scraped data to a CSV file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f'scraped_data_{timestamp}.csv'

        if not os.path.exists('scraped_data'):
            os.makedirs('scraped_data')

        filepath = os.path.join('scraped_data', filename)

        with open(filepath, 'w', newline='', encoding='utf-8') as file:
            if data:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
                print(f"Data saved to {filepath}")
            else:
                print("No data to save")

def main():
    scraper = WebScraper()
    
    print("Web Scraper")
    print("-----------")
    print("1. Scrape quotes from quotes.toscrape.com")
    print("2. Scrape news from Hacker News")
    print("3. Enter custom URL to scrape")
    print("4. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            print("\nScraping quotes from quotes.toscrape.com...")
            quotes = scraper.scrape_quotes()
            scraper.save_to_csv(quotes, 'quotes.csv')
            
        elif choice == '2':
            print("\nScraping news from Hacker News...")
            news = scraper.scrape_news()
            scraper.save_to_csv(news, 'hacker_news.csv')
            
        elif choice == '3':
            url = input("\nEnter the URL to scrape: ")
            print(f"\nScraping {url}...")
            # Note: You would need to implement specific scraping logic for custom URLs
            print("Custom URL scraping not implemented yet. Please use options 1 or 2 for demo.")
            
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 