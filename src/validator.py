# validator.py
from typing import Dict
import re

class NewsValidator:
    def __init__(self):
        self.blacklist_words = [
            "possibly", "maybe", "might", "could be", "uncertain",
            "unconfirmed", "allegedly", "rumored"
        ]

    def validate_article(self, article: str) -> Dict:
        """Validate the generated article for potential issues."""
        issues = []
        
        # Check for speculative language
        for word in self.blacklist_words:
            if re.search(r'\b' + word + r'\b', article.lower()):
                issues.append(f"Contains speculative term: {word}")

        # Check article length
        word_count = len(article.split())
        if word_count < 200:
            issues.append("Article too short")
        elif word_count > 400:
            issues.append("Article too long")

        return {
            "is_valid": len(issues) == 0,
            "issues": issues,
            "word_count": word_count
        }