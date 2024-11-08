from .base_agent import BaseAgent
from crewai import Agent
from langchain.tools import Tool

class RouterAgent(BaseAgent):
    def __init__(self, groq_client):
        super().__init__(groq_client)
        self.agent = Agent(
            role="Router",
            goal="Analyze and route queries to appropriate search strategy",
            backstory="I am specialized in understanding queries and determining the best search approach",
            allow_delegation=True,
            tools=[
                Tool(
                    name="analyze_query",
                    func=self._analyze_query,
                    description="Analyzes query intent and structure"
                )
            ]
        )
    
    def _analyze_query(self, query):
        prompt = f"Analyze the following query and determine the best search strategy: {query}"
        return self.groq_client.get_completion(prompt)