import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class NewsService:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.feeds = [
            "https://www.moneycontrol.com/rss/latestnews.xml",
            "https://economictimes.indiatimes.com/rssfeedstopstories.cms"
        ]

    def get_latest_sentiment(self):
        headlines = []
        for feed in self.feeds:
            try:
                response = requests.get(feed, timeout=5)
                soup = BeautifulSoup(response.content, 'xml')
                items = soup.find_all('item')
                for item in items[:5]:
                    headlines.append(item.title.text)
            except Exception as e:
                print(f"Error fetching news feed {feed}: {e}")

        if not headlines:
            return {"sentiment": "NEUTRAL", "score": 0}

        combined_text = ". ".join(headlines)
        vs = self.analyzer.polarity_scores(combined_text)

        sentiment = "NEUTRAL"
        if vs['compound'] >= 0.05:
            sentiment = "BULLISH"
        elif vs['compound'] <= -0.05:
            sentiment = "BEARISH"

        return {
            "sentiment": sentiment,
            "score": vs['compound'],
            "headlines": headlines[:5]
        }
