from pydantic import BaseModel
from typing import List


class Quote(BaseModel):
    quote: str
    author: str


class QuoteResponse(BaseModel):
    quotes: List[Quote]