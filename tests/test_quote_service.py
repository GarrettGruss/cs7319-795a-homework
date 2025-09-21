import unittest
import json
from unittest.mock import patch, mock_open
from pathlib import Path
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from backend.service.quote_service import QuoteService
from backend.model.quote import Quote


class TestQuoteService(unittest.TestCase):
    
    def setUp(self):
        self.test_quotes_data = [
            {"quote": "Test quote one for unit testing.", "author": "Test Author One"},
            {"quote": "Test quote two for unit testing.", "author": "Test Author Two"},
            {"quote": "Test quote three for unit testing.", "author": "Test Author Three"},
            {"quote": "Test quote four for unit testing.", "author": "Test Author Four"},
            {"quote": "Test quote five for unit testing.", "author": "Test Author Five"},
            {"quote": "Test quote six for unit testing.", "author": "Test Author Six"},
            {"quote": "Test quote seven for unit testing.", "author": "Test Author Seven"},
            {"quote": "Test quote eight for unit testing.", "author": "Test Author Eight"},
            {"quote": "Test quote nine for unit testing.", "author": "Test Author Nine"},
            {"quote": "Test quote ten for unit testing.", "author": "Test Author Ten"}
        ]
        
    @patch("builtins.open", new_callable=mock_open)
    @patch("pathlib.Path.exists")
    def test_load_quotes_success(self, mock_exists, mock_file):
        mock_exists.return_value = True
        mock_file.return_value.read.return_value = json.dumps(self.test_quotes_data)
        
        service = QuoteService()
        
        self.assertEqual(len(service.quotes), 10)
        self.assertIsInstance(service.quotes[0], Quote)
        self.assertEqual(service.quotes[0].quote, "Test quote one for unit testing.")
        self.assertEqual(service.quotes[0].author, "Test Author One")
    
    @patch("builtins.open", new_callable=mock_open)
    @patch("pathlib.Path.exists")
    def test_get_random_quotes_default_count(self, mock_exists, mock_file):
        mock_exists.return_value = True
        mock_file.return_value.read.return_value = json.dumps(self.test_quotes_data)
        
        service = QuoteService()
        quotes = service.get_random_quotes()
        
        self.assertEqual(len(quotes), 4)
        self.assertTrue(all(isinstance(quote, Quote) for quote in quotes))
        
        # Verify all quotes are unique
        quote_texts = [quote.quote for quote in quotes]
        self.assertEqual(len(quote_texts), len(set(quote_texts)))
    
    @patch("builtins.open", new_callable=mock_open)
    @patch("pathlib.Path.exists")
    def test_get_random_quotes_custom_count(self, mock_exists, mock_file):
        mock_exists.return_value = True
        mock_file.return_value.read.return_value = json.dumps(self.test_quotes_data)
        
        service = QuoteService()
        quotes = service.get_random_quotes(6)
        
        self.assertEqual(len(quotes), 6)
        self.assertTrue(all(isinstance(quote, Quote) for quote in quotes))
        
        # Verify all quotes are unique
        quote_texts = [quote.quote for quote in quotes]
        self.assertEqual(len(quote_texts), len(set(quote_texts)))
    
    @patch("builtins.open", new_callable=mock_open)
    @patch("pathlib.Path.exists")
    def test_get_random_quotes_count_exceeds_available(self, mock_exists, mock_file):
        mock_exists.return_value = True
        mock_file.return_value.read.return_value = json.dumps(self.test_quotes_data)
        
        service = QuoteService()
        quotes = service.get_random_quotes(15)  # More than available
        
        self.assertEqual(len(quotes), 10)  # Should return all available quotes
        self.assertTrue(all(isinstance(quote, Quote) for quote in quotes))
    
    @patch("builtins.open", new_callable=mock_open)
    @patch("pathlib.Path.exists")
    def test_get_random_quotes_zero_count(self, mock_exists, mock_file):
        mock_exists.return_value = True
        mock_file.return_value.read.return_value = json.dumps(self.test_quotes_data)
        
        service = QuoteService()
        quotes = service.get_random_quotes(0)
        
        self.assertEqual(len(quotes), 0)
    
    @patch("builtins.open", new_callable=mock_open)
    @patch("pathlib.Path.exists")
    def test_get_random_quotes_randomness(self, mock_exists, mock_file):
        mock_exists.return_value = True
        mock_file.return_value.read.return_value = json.dumps(self.test_quotes_data)
        
        service = QuoteService()
        
        # Get multiple sets of quotes and verify they're not always the same
        quote_sets = []
        for _ in range(10):
            quotes = service.get_random_quotes(4)
            quote_texts = tuple(quote.quote for quote in quotes)
            quote_sets.append(quote_texts)
        
        # Should have at least some variation (not all identical)
        unique_sets = set(quote_sets)
        self.assertGreater(len(unique_sets), 1, "Random selection should produce different results")
    
    @patch("builtins.open", new_callable=mock_open)
    @patch("pathlib.Path.exists")
    def test_quote_model_validation(self, mock_exists, mock_file):
        mock_exists.return_value = True
        mock_file.return_value.read.return_value = json.dumps(self.test_quotes_data)
        
        service = QuoteService()
        quote = service.quotes[0]
        
        # Test that Quote model has correct attributes
        self.assertTrue(hasattr(quote, 'quote'))
        self.assertTrue(hasattr(quote, 'author'))
        self.assertIsInstance(quote.quote, str)
        self.assertIsInstance(quote.author, str)


if __name__ == '__main__':
    unittest.main()