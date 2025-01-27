# generator.py
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from typing import Dict, List

class NewsGenerator:
    def __init__(self):
        self.llm = ChatOllama(model="llama2")
        self.template = """
        You are a professional news writer. Write a news article based on the following information:

        Topic: {topic}
        Related Facts: {facts}
        Tone: Objective and professional
        Length: Approximately 300 words

        Rules:
        - Stick to the facts provided
        - Use journalistic style
        - Include a headline
        - Format in markdown
        - Add attribution where appropriate

        Article:
        """

    def generate_article(self, topic: str, facts: List[Dict]) -> str:
        """Generate a news article based on topic and facts."""
        prompt = ChatPromptTemplate.from_template(self.template)
        
        # Extract relevant information from facts
        facts_text = "\n".join([
            f"- {fact.get('title', '')}: {fact.get('description', '')}"
            for fact in facts if fact.get('title')
        ])
        
        # Generate the article
        chain = prompt | self.llm
        result = chain.invoke({"topic": topic, "facts": facts_text})
        return result.content