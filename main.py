# main.py
import os
from src.news_fetcher import NewsFetcher
from src.generator import NewsGenerator
from src.validator import NewsValidator

def main():

    # Initialize components
    news_fetcher = NewsFetcher(newsapi_key=None)
    generator = NewsGenerator()
    validator = NewsValidator()
    
    # Get user input
    topic = input("Enter a news topic: ")
    
    # Fetch related news
    related_news = news_fetcher.fetch_related_news(topic)
    
    # Generate article
    article = generator.generate_article(topic, related_news)
    
    # Validate article
    validation_result = validator.validate_article(article)
    
    # Output results
    if validation_result["is_valid"]:
        print("\nGenerated Article:")
        print("=" * 50)
        print(article)
        print("\nWord count:", validation_result["word_count"])
    else:
        print("\nValidation Issues:")
        for issue in validation_result["issues"]:
            print(f"- {issue}")
        print("\nRaw Article:")
        print(article)

if __name__ == "__main__":
    main()