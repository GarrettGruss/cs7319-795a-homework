import json
import random
from pathlib import Path
from typing import List
from ..model.quote import Quote


class QuoteService:
    def __init__(self):
        self.quotes = self._load_quotes()
    
    def _load_quotes(self) -> List[Quote]:
        project_root = Path(__file__).parent.parent.parent.parent
        quotes_file = project_root / "data" / "quotes.json"
        
        with open(quotes_file, 'r', encoding='utf-8') as f:
            quotes_data = json.load(f)
        
        return [Quote(**quote_data) for quote_data in quotes_data]
    
    def get_random_quotes(self, count: int = 4) -> List[Quote]:
        if count > len(self.quotes):
            count = len(self.quotes)
        
        return random.sample(self.quotes, count)