from dotenv import load_dotenv
from pathlib import Path
import os
from src.news_fetcher import NewsFetcher
from src.generator import NewsGenerator
from src.validator import NewsValidator

def main():
   
     # Load .env file
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    api_key = os.getenv("NEWSAPI_KEY")
    if not api_key:
        print("NEWSAPI_KEY not found. Please set it in the .env file.")
        return

    # Initialize components
    news_fetcher = NewsFetcher(api_key)
    generator = NewsGenerator()
    validator = NewsValidator()

    # CLI input
    topic = input("Enter a news topic: ")

    # Fetch related news
    related_news = news_fetcher.fetch_related_news(topic)

    if not related_news:
        print("No news articles found for this topic. Please try again.")
        return

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
