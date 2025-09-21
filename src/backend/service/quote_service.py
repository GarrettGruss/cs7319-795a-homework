import random
from typing import List
from ..model.quote import Quote


class QuoteService:
    QUOTES_DATA = [
        [
  {"quote": "The only way to do great work is to love what you do."},
  {"quote": "Innovation distinguishes between a leader and a follower."},
  {"quote": "Stay hungry, stay foolish."},
  {"quote": "The future belongs to those who believe in the beauty of their dreams."},
  {"quote": "Success is not final, failure is not fatal: it is the courage to continue that counts."},
  {"quote": "Believe you can and you're halfway there."},
  {"quote": "The only impossible journey is the one you never begin."},
  {"quote": "Life is what happens when you're busy making other plans."},
  {"quote": "The best time to plant a tree was 20 years ago. The second best time is now."},
  {"quote": "Your time is limited, don't waste it living someone else's life."}
]
    ]

    def __init__(self):
        self.quotes = self._load_quotes()
    
    def _load_quotes(self) -> List[Quote]:
        return [Quote(**quote_data) for quote_data in self.QUOTES_DATA]
    
    def get_random_quotes(self, count: int = 4) -> List[Quote]:
        if count > len(self.quotes):
            count = len(self.quotes)
        
        return random.sample(self.quotes, count)