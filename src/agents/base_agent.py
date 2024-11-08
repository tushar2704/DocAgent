from crewai import Agent
from langchain.tools import Tool

class BaseAgent:
    def __init__(self, groq_client):
        self.groq_client = groq_client