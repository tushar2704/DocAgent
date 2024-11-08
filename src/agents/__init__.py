from typing import List
from crewai import Crew, Task, Agent
from .router_agent import RouterAgent
from .retriever_agent import RetrieverAgent
from .grader_agent import GraderAgent

class RAGCrewBuilder:
    """
    Builds and manages the RAG Crew with all necessary agents.
    """
    def __init__(self, groq_client, document_processor):
        self.groq_client = groq_client
        self.document_processor = document_processor
        
        # Initialize agents
        self.router = RouterAgent(groq_client)
        self.retriever = RetrieverAgent(groq_client, document_processor)
        self.grader = GraderAgent(groq_client)
        
        # Store all agents
        self.agents: List[Agent] = [
            self.router.agent,
            self.retriever.agent,
            self.grader.agent
        ]
    
    def _create_tasks(self, query: str) -> List[Task]:
        """
        Creates a list of tasks for the crew based on the query.
        """
        return [
            Task(
                description=f"Analyze the following query and determine search strategy: {query}",
                agent=self.router.agent,
                context="Determine the best approach to answer this query",
                expected_output="Search strategy and query analysis"
            ),
            Task(
                description=f"Search and retrieve relevant information for: {query}",
                agent=self.retriever.agent,
                context="Use the search strategy to find relevant information",
                expected_output="Retrieved relevant information"
            ),
            Task(
                description="Validate and improve the retrieved information",
                agent=self.grader.agent,
                context="Ensure accuracy and quality of the final answer",
                expected_output="Final validated and improved answer"
            )
        ]
    
    def create_crew(self, query: str) -> Crew:
        """
        Creates a crew with all necessary agents and tasks.
        """
        tasks = self._create_tasks(query)
        
        return Crew(
            agents=self.agents,
            tasks=tasks,
            process="sequential",
            verbose=True
        )
    
    async def process_query(self, query: str) -> str:
        """
        Process a query through the RAG pipeline.
        """
        crew = self.create_crew(query)
        result = await crew.kickoff()
        return result

__all__ = ["RAGCrewBuilder", "RouterAgent", "RetrieverAgent", "GraderAgent"]