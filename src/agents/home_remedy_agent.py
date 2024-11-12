from crewai import Agent
from langchain_groq import ChatGroq

class HomeRemedyAgent(Agent):
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0.2, 
            model="llama3-8b-8192"
        )
        
    def find_home_remedies(self, symptom, intensity):
        prompt = f"""
        For a {intensity} intensity {symptom}, provide:
        1. 3-4 immediate home remedies
        2. Symptoms to watch out for
        3. When to seek medical attention
        """
        
        response = self.llm.invoke(prompt)
        return response.content