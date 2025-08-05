import requests

class DataCollectorAgent:
    def __init__(self, api_key=None):
        # Put your GNews API key here
        self.api_key = api_key or "5aaa3d40c832b918efcefdb7e81580e3"
        self.endpoint = "https://gnews.io/api/v4/search"

    def fetch_data(self, query="artificial intelligence"):
        params = {
            'q': query,
            'lang': 'en',
            'max': 3,
            'token': self.api_key
        }
        try:
            response = requests.get(self.endpoint, params=params)
            response.raise_for_status()
            articles = response.json().get("articles", [])
            return self._preprocess_articles(articles)
        except Exception as e:
            print("❌ Error in DataCollectorAgent:", e)
            return []

    def _preprocess_articles(self, articles):
        processed = []
        for article in articles:
            content = article.get("content") or article.get("description", "")
            if content:
                processed.append(content[:500])
        return processed