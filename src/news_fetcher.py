# news_fetcher.py
import requests
import feedparser
from datetime import datetime
from typing import List, Dict

class NewsFetcher:
    def __init__(self, newsapi_key: str):
        self.newsapi_key = "817e93fe932249aca8f44b009daf9e12"
        self.newsapi_url = "https://newsapi.org/v2/everything"

    def fetch_related_news(self, topic: str) -> List[Dict]:
        """Fetch news articles related to a specific topic."""
        params = {
            'q': topic,
            'apiKey': self.newsapi_key,
            'language': 'en',
            'sortBy': 'relevancy',
            'pageSize': 5
        }
        
        try:
            response = requests.get(self.newsapi_url, params=params)
            response.raise_for_status()
            return response.json()['articles']
        except Exception as e:
            print(f"Error fetching news: {e}")
            return []

    def get_rss_feeds(self, rss_url: str) -> List[Dict]:
        """Fetch news from RSS feeds."""
        try:
            feed = feedparser.parse(rss_url)
            return feed.entries
        except Exception as e:
            print(f"Error parsing RSS feed: {e}")
            return []