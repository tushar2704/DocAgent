
import os
import streamlit as st
# from dotenv import load_dotenv
from groq import Groq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_groq import ChatGroq 
from crewai import Agent, Task, Crew, Process

# Load environment variables
# load_dotenv()
api_key = st.secrets["GROQ_API_KEY"]
# Import local components
from src.components.navigation import page_config, custom_style, footer


# Set up Groq LLM client
groq_llm = ChatGroq(
    api_key=st.secrets["GROQ_API_KEY"], #or os.getenv("GROQ_API_KEY")
    model="llama-3.1-8b-instant",  # Specify the model you want to use
    temperature=0.1,
    max_tokens=None,
    timeout=3,
    max_retries=2,
)

            
        
        
        
        
        
        
# Define Agents using Groq LLM
symptom_analyzer = Agent(
    role="Symptom Analyzer",
    goal="Analyze user-reported symptoms and provide structured output.",
    backstory="You are an expert in analyzing medical symptoms.",
    llm=groq_llm, 
    verbose=True
)

health_advisor = Agent(
    role="Health Advisor",
    goal="Provide professional health advice based on symptom analysis.",
    backstory="You are a medical assistant providing health advice.",
    llm=groq_llm, 
    verbose=True
)

researcher = Agent(
    role="Researcher",
    goal="Conduct research on symptoms using external tools like DuckDuckGo.",
    backstory="You are an expert researcher in healthcare.",
    llm=groq_llm, 
    verbose=True
)

doclib_agent = Agent(
    role="DocLib Manager",
    goal="Retrieve relevant medical documents from DocLib.",
    backstory="You manage and retrieve medical documents from DocLib.",
    llm=groq_llm, 
    verbose=True
)


specialist_finder = Agent(
    role="Local Specialist Finder",
    goal="Find local area medical specialists based on the user's location and symptoms.",
    backstory="You are an expert at finding local healthcare providers and specialists.",
    llm=groq_llm, 
    verbose=True 
)


# Define Tasks for each agent
task_symptom_analysis = Task(
    description="Analyze the user's symptoms and provide structured data.",
    expected_output='A bullet list of symptoms and their severity',
    agent=symptom_analyzer,
)

task_health_advice = Task(
    description="Generate health advice based on analyzed symptoms.",
    expected_output='A bullet list of health advice based on analyzed symptoms and intensity',
    agent=health_advisor,
)

task_research = Task(
    description="Perform external research to validate health advice.",
    expected_output='A summary of external research to validate health advice',
    agent=researcher,
    
)

task_doclib = Task(
    description="Retrieve relevant medical documents.",
    expected_output='A bullet list of relevant medical documents.',
    agent=doclib_agent,
)


task_find_specialist = Task(
    description="Find local area medical specialists based on the user's city and symptoms.",
    expected_output="A bullet list of relevant medical medical specialists based on the users city and symptoms.",
    agent=specialist_finder,
)



crew = Crew(
   agents=[symptom_analyzer, health_advisor, researcher, doclib_agent, specialist_finder],
   tasks=[task_symptom_analysis, task_health_advice, task_research, task_doclib, task_find_specialist],
   process=Process.sequential,
)


def main():
    # Streamlit Page Setup
    page_config("DocLib", "🤖", "wide")
    custom_style()

    st.title("🤖 DocLib 🤖")
    st.markdown("### DocLib helps you find specialists nearby while suggesting home remedies for your health issues.")


    # Input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        
        
        
        symptoms = st.text_input("Enter your symptoms:")



    with col2:
        intensity = st.selectbox("Select symptom intensity:", ["Mild", "Moderate", "Severe"])

    with col3:
        city = st.text_input("Enter your city (for finding local specialists):")

    # Advice generation
    if st.button("Get Health Advice and Find Specialists"):
        inputs = {"symptoms": symptoms, "intensity": intensity, "city": city}
    
    try:
        result = crew.kickoff(inputs=inputs)
        st.success(f"Health Advice: {result}")
        
        # Display document retrieval results from DocLib
        doc_result = task_doclib.output.raw  
        st.info(f"Relevant Documents: {doc_result}")
        
        # Display specialist search results
        specialist_result = task_find_specialist.output.raw  
        st.info(f"Local Specialists in {city}: {specialist_result}")
        
    except Exception as e:
        st.error(f"Error during execution: {e}")

if __name__ == "__main__":
    main()



