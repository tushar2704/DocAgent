from typing import List, Optional
import re
from nltk.tokenize import sent_tokenize
import nltk

# Download required NLTK data
try:
    nltk.download('punkt', quiet=True)
except:
    pass

class TextProcessor:
    """Handles text processing and cleaning operations"""
    
    @staticmethod
    def clean_text(text: str) -> str:
        """
        Cleans and normalizes text
        
        Args:
            text: Input text
        Returns:
            str: Cleaned text
        """
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters
        text = re.sub(r'[^\w\s.,!?-]', '', text)
        return text.strip()
    
    @staticmethod
    def extract_sentences(text: str) -> List[str]:
        """
        Extracts sentences from text
        
        Args:
            text: Input text
        Returns:
            List[str]: List of sentences
        """
        return sent_tokenize(text)

class TextChunker:
    """Handles text chunking for processing large documents"""
    
    def __init__(self, chunk_size: int = 1000, overlap: int = 200):
        self.chunk_size = chunk_size
        self.overlap = overlap
    
    def chunk_text(self, text: str) -> List[str]:
        """
        Splits text into overlapping chunks
        
        Args:
            text: Input text
        Returns:
            List[str]: List of text chunks
        """
        chunks = []
        start = 0
        text_len = len(text)
        
        while start < text_len:
            end = start + self.chunk_size
            
            # Adjust chunk end to not split words
            if end < text_len:
                # Find the last space before chunk_size
                while end > start and text[end] != ' ':
                    end -= 1
            
            # Add chunk
            chunks.append(text[start:end])
            
            # Move start position considering overlap
            start = end - self.overlap
        
        return chunks