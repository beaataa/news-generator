# app.py
import streamlit as st
import os
from dotenv import load_dotenv
from src.news_fetcher import NewsFetcher
from src.generator import NewsGenerator
from src.validator import NewsValidator

def initialize_components():
    """Initialize all required components with error handling."""
    try:
        api_key = os.getenv("NEWSAPI_KEY")
        if not api_key:
            st.error("⚠️ NEWSAPI_KEY not found in environment variables")
            st.stop()
            
        news_fetcher = NewsFetcher(api_key)
        generator = NewsGenerator()
        validator = NewsValidator()
        return news_fetcher, generator, validator
    
    except Exception as e:
        st.error(f"⚠️ Error initializing components: {str(e)}")
        st.stop()

def main():
    # Page config
    st.set_page_config(
        page_title="AI News Generator",
        page_icon="📰",
        layout="wide"
    )
    
    # Load environment variables
    load_dotenv()
    
    # Header
    st.title("📰 AI News Article Generator")
    st.markdown("""
    This app generates news articles based on your chosen topic using AI and real-time news data.
    Enter a topic below to get started!
    """)
    
    # Initialize components
    news_fetcher, generator, validator = initialize_components()
    
    # Input section using columns
    col1, col2 = st.columns([3, 1])
    
    with col1:
        topic = st.text_input("Enter your news topic:", placeholder="e.g., technology, climate change, sports")
    
    with col2:
        generate_button = st.button("Generate Article", type="primary", use_container_width=True)

    # Article generation section (full width)
    if generate_button:
        if not topic:
            st.warning("Please enter a topic first!")
            return
        
        # Progress section
        progress_col1, progress_col2 = st.columns(2)
        
        # 1. Fetch news
        with progress_col1:
            with st.spinner("🔍 Fetching related news..."):
                related_news = news_fetcher.fetch_related_news(topic)
                
                if not related_news:
                    st.error("No news found for this topic. Please try a different topic.")
                    return
                
                st.success(f"Found {len(related_news)} related articles!")
        
        # 2. Generate article
        with progress_col2:
            with st.spinner("✍️ Generating article..."):
                article = generator.generate_article(topic, related_news)
                validation_result = validator.validate_article(article)
        
        # Create tabs for the full width content
        tab1, tab2 = st.tabs(["Article", "Validation Details"])
        
        with tab1:
            # Article container
            with st.container():
                st.markdown("### Generated Article")
                st.markdown(article)
                
                # Download button aligned to the right
                col1, col2, col3 = st.columns([3, 3, 1])
                with col3:
                    st.download_button(
                        label="📥 Download",
                        data=article,
                        file_name=f"{topic.replace(' ', '_')}_article.md",
                        mime="text/markdown"
                    )
        
        with tab2:
            # Validation details in a clean layout
            col1, col2 = st.columns(2)
            
            with col1:
                # Validation status
                if validation_result["is_valid"]:
                    st.success("✅ Article passed all validation checks!")
                else:
                    st.warning("⚠️ Some issues were found:")
                    for issue in validation_result["issues"]:
                        st.write(f"- {issue}")
                
                # Word count
                st.info(f"Word count: {validation_result['word_count']} words")
            
            with col2:
                # Source articles
                st.markdown("### Source Articles")
                for idx, article in enumerate(related_news, 1):
                    with st.expander(f"Source {idx}: {article.get('title', 'Untitled')}"):
                        st.write(article.get('description', 'No description available'))
                        if article.get('url'):
                            st.write(f"[Read more]({article['url']})")

if __name__ == "__main__":
    main()