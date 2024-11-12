class SymptomAnalyzerAgent(Agent):
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0.2, 
            model="llama3-8b-8192"
        )
    
    def analyze_symptoms(self, symptom, intensity):
        prompt = f"""
        For a {symptom} with {intensity} intensity:
        1. Potential underlying conditions
        2. Recommended diagnostic tests
        3. Red flag symptoms requiring immediate medical attention
        """
        
        response = self.llm.invoke(prompt)
        return response.content