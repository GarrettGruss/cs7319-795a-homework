import streamlit as st
from api_client import QuotesAPIClient
import time

# Page configuration
st.set_page_config(
    page_title="Inspirational Quotes",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
.quote-card {
    background-color: #f8f9fa;
    border-left: 4px solid #007bff;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 0.5rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.quote-text {
    font-style: italic;
    font-size: 1.1rem;
    color: #333;
    margin-bottom: 0.5rem;
}

.quote-author {
    font-weight: bold;
    color: #666;
    text-align: right;
}

.status-indicator {
    padding: 0.2rem 0.5rem;
    border-radius: 0.25rem;
    font-size: 0.8rem;
    font-weight: bold;
}

.status-healthy {
    background-color: #d4edda;
    color: #155724;
}

.status-unhealthy {
    background-color: #f8d7da;
    color: #721c24;
}
</style>
""", unsafe_allow_html=True)

def display_quote(quote_data):
    """Display a single quote in a styled card format"""
    st.markdown(f"""
    <div class="quote-card">
        <div class="quote-text">"{quote_data['quote']}"</div>
        <div class="quote-author">— {quote_data['author']}</div>
    </div>
    """, unsafe_allow_html=True)

def main():
    # Header
    st.title("💡 Inspirational Quotes")
    st.markdown("*Get inspired with randomly selected motivational quotes*")
    
    # Initialize API client
    api_client = QuotesAPIClient()
    
    # Sidebar for API status and controls
    with st.sidebar:
        st.header("API Status")
        
        # Health check
        if api_client.health_check():
            st.markdown('<div class="status-indicator status-healthy">🟢 API Online</div>', 
                       unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-indicator status-unhealthy">🔴 API Offline</div>', 
                       unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("**Backend:** FastAPI + Pydantic")
        st.markdown("**Frontend:** Streamlit")
        st.markdown("**Deployment:** Kubernetes (4 replicas)")
    
    # Main content area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Fetch quotes button
        if st.button("🎲 Get New Quotes", type="primary", use_container_width=True):
            with st.spinner("Fetching inspirational quotes..."):
                quotes = api_client.get_quotes()
                
                if quotes:
                    st.session_state.quotes = quotes
                    st.session_state.last_fetch = time.time()
    
    # Display quotes if available
    if hasattr(st.session_state, 'quotes') and st.session_state.quotes:
        st.markdown("### Your Inspirational Quotes")
        
        # Display fetch time
        if hasattr(st.session_state, 'last_fetch'):
            fetch_time = time.strftime("%H:%M:%S", time.localtime(st.session_state.last_fetch))
            st.caption(f"Last updated: {fetch_time}")
        
        # Display quotes in a grid
        for i, quote in enumerate(st.session_state.quotes):
            display_quote(quote)
        
        # Add refresh button at the bottom
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("🔄 Refresh Quotes", use_container_width=True):
                st.rerun()
    
    else:
        # Welcome message
        st.markdown("### Welcome!")
        st.info("Click the **'Get New Quotes'** button above to fetch 4 randomly selected inspirational quotes from our collection of 51+ quotes.")
        
        # Sample quote for demonstration
        st.markdown("#### Sample Quote:")
        sample_quote = {
            "quote": "Click the button above to get your personalized inspirational quotes!",
            "author": "Quotes API"
        }
        display_quote(sample_quote)

if __name__ == "__main__":
    main()