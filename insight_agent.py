import spacy
from collections import Counter

class InsightAgent:
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            print("❌ Error: spaCy English model not found. Please run:")
            print("python -m spacy download en_core_web_sm")
            self.nlp = None

    def extract_keywords(self, texts):
        if not self.nlp:
            return [("spacy model missing", 1.0)]
            
        all_phrases = []
        for text in texts:
            doc = self.nlp(text)
            phrases = [chunk.text.lower() for chunk in doc.noun_chunks]
            all_phrases.extend(phrases)

        top_phrases = Counter(all_phrases).most_common(5)
        return top_phrases