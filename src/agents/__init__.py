from .router_agent import RouterAgent
from .retriever_agent import RetrieverAgent
from .grader_agent import GraderAgent
from crewai import Crew, Task

class RAGCrewBuilder:
    def __init__(self, groq_client, document_processor):
        self.router = RouterAgent(groq_client)
        self.retriever = RetrieverAgent(groq_client, document_processor)
        self.grader = GraderAgent(groq_client)
    
    def create_crew(self, query):
        tasks = [
            Task(
                description=f"Analyze query: {query}",
                agent=self.router.agent
            ),
            Task(
                description="Retrieve relevant information",
                agent=self.retriever.agent
            ),
            Task(
                description="Validate and improve answer",
                agent=self.grader.agent
            )
        ]
        
        return Crew(
            agents=[self.router.agent, self.retriever.agent, self.grader.agent],
            tasks=tasks,
            process="sequential"
        )