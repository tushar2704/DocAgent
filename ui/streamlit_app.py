
import streamlit as st
from dotenv import load_dotenv
import os
from src.core.groq_client import *
from src.core.embeddings import DocumentProcessor
from src.agents import RAGCrewBuilder
import PyPDF2

def load_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def main():
    load_dotenv()
    
    st.title("DocAgent - Intelligent Document Assistant")
    
    groq_client = GroqClient()
    doc_processor = DocumentProcessor()
    rag_crew_builder = RAGCrewBuilder(groq_client, doc_processor)
    
    query = st.text_input("Ask your question")
    if query and doc_processor.index:
        with st.spinner("Generating response..."):
            crew = rag_crew_builder.create_crew(query)
            result = crew.kickoff()
            st.write(result)

if __name__ == "__main__":
    main()