# streamlit_app.py
import streamlit as st
from src.utils import PDFProcessor, TextProcessor, TextChunker, FileHandler

def main():
    st.title("DocAgent - Document Processing")
    
    # Initialize utilities
    pdf_processor = PDFProcessor()
    text_processor = TextProcessor()
    text_chunker = TextChunker(chunk_size=1000, overlap=200)
    file_handler = FileHandler()
    
    # File upload
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")
    if uploaded_file:
        # Process file
        try:
            # Get file hash for caching
            file_hash = file_handler.get_file_hash(uploaded_file)
            
            # Check cache
            cached_data = file_handler.load_from_cache(file_hash)
            if cached_data:
                st.success("Loading from cache...")
                processed_text = cached_data['data']['processed_text']
            else:
                # Process PDF
                raw_text = pdf_processor.read_pdf(uploaded_file)
                
                # Clean text
                cleaned_text = text_processor.clean_text(raw_text)
                
                # Chunk text
                text_chunks = text_chunker.chunk_text(cleaned_text)
                
                # Cache results
                file_handler.save_to_cache(file_hash, {
                    'processed_text': text_chunks
                })
                
                processed_text = text_chunks
            
            # Display results
            st.write("Processed Text Chunks:")
            for i, chunk in enumerate(processed_text):
                st.text_area(f"Chunk {i+1}", chunk, height=100)
                
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    main()