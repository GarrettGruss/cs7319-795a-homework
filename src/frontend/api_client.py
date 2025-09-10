import requests
from typing import List, Dict
import streamlit as st


class QuotesAPIClient:
    def __init__(self, base_url: str = "http://localhost:8080"):
        self.base_url = base_url
    
    def get_quotes(self) -> List[Dict[str, str]]:
        try:
            response = requests.get(f"{self.base_url}/api/quotes", timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the quotes API. Make sure the backend is running.")
            return []
        except requests.exceptions.Timeout:
            st.error("Request timed out. Please try again.")
            return []
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching quotes: {str(e)}")
            return []
    
    def health_check(self) -> bool:
        try:
            response = requests.get(f"{self.base_url}/health", timeout=5)
            return response.status_code == 200
        except:
            return False