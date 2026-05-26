import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

class DataService:
    @staticmethod
    def get_historical_data(symbol: str, period: str = "5d", interval: str = "5m"):
        """Fetch historical data from Yahoo Finance."""
        try:
            ticker = yf.Ticker(symbol)
            df = ticker.history(period=period, interval=interval)
            return df
        except Exception as e:
            print(f"Error fetching historical data: {e}")
            return pd.DataFrame()

    @staticmethod
    def get_nse_live_quote(symbol: str):
        """
        Scrape live quote from NSE India.
        Note: This is fragile and should be used with caution.
        Better to use a broker API if available for free.
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'accept-language': 'en-US,en;q=0.9',
            'accept-encoding': 'gzip, deflate, br'
        }
        # In a real scenario, we might need to hit the home page first to get cookies
        session = requests.Session()
        session.get("https://www.nseindia.com", headers=headers)

        url = f"https://www.nseindia.com/api/quote-equity?symbol={symbol}"
        try:
            response = session.get(url, headers=headers)
            return response.json()
        except Exception as e:
            print(f"Error scraping NSE: {e}")
            return None

    @staticmethod
    def get_news_sentiment(keywords: list):
        """Placeholder for news sentiment logic using VADER."""
        # This will be implemented with RSS feeds later
        return {"sentiment": "neutral", "score": 0.0}
