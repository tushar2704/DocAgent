from .base_agent import BaseAgent
from crewai import Agent
from langchain.tools import Tool

class RetrieverAgent(BaseAgent):
    def __init__(self, groq_client, document_processor):
        super().__init__(groq_client)
        self.doc_processor = document_processor
        self.agent = Agent(
            role="Retriever",
            goal="Find and retrieve relevant information from documents",
            backstory="I am specialized in searching and retrieving relevant information",
            allow_delegation=False,
            tools=[
                Tool(
                    name="search_documents",
                    func=self._search_documents,
                    description="Searches indexed documents for relevant information"
                )
            ]
        )
    
    def _search_documents(self, query):
        if self.doc_processor.index:
            query_engine = self.doc_processor.index.as_query_engine()
            return query_engine.query(query)
        return "No documents indexed yet"