from fastapi import APIRouter
from typing import List
from ..model.quote import Quote
from ..service.quote_service import QuoteService

router = APIRouter()
quote_service = QuoteService()


@router.get("/api/quotes", response_model=List[Quote])
async def get_quotes():
    return quote_service.get_random_quotes(4)