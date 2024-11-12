class DoctorFinderAgent(Agent):
    def __init__(self, search_engine):
        self.search_engine = search_engine
        self.llm = ChatGroq(
            temperature=0.2, 
            model="llama3-8b-8192"
        )
    
    def find_specialists(self, location, symptom):
        search_results = self.search_engine.search(
            f"best {symptom} specialists in {location}"
        )
        
        prompt = f"""
        Analyze these search results and provide:
        1. Top 3 specialists for {symptom} in {location}
        2. Their contact details
        3. Estimated availability for appointments
        
        Search Results: {search_results}
        """
        
        response = self.llm.invoke(prompt)
        return response.content