from .base_agent import BaseAgent
from crewai import Agent
from langchain.tools import Tool

class GraderAgent(BaseAgent):
    def __init__(self, groq_client):
        super().__init__(groq_client)
        self.agent = Agent(
            role="Grader",
            goal="Validate and improve answer quality",
            backstory="I am specialized in ensuring answer accuracy and quality",
            allow_delegation=False,
            tools=[
                Tool(
                    name="validate_answer",
                    func=self._validate_answer,
                    description="Validates and improves answer quality"
                )
            ]
        )
    
    def _validate_answer(self, answer):
        prompt = f"Validate and improve the following answer: {answer}"
        return self.groq_client.get_completion(prompt)