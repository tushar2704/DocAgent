import PyPDF2
import fitz  # PyMuPDF
from typing import List, Optional
import io

class PDFProcessor:
    """Handles PDF document processing and text extraction"""
    
    def __init__(self):
        self.current_pdf = None
    
    def read_pdf(self, file_obj) -> str:
        """
        Reads a PDF file and extracts text content
        
        Args:
            file_obj: File object (can be Streamlit uploaded file or file path)
        Returns:
            str: Extracted text from PDF
        """
        try:
            # Handle both file paths and uploaded file objects
            if isinstance(file_obj, str):
                pdf_document = fitz.open(file_obj)
            else:
                pdf_document = fitz.open(stream=file_obj.read(), filetype="pdf")
            
            text = ""
            for page_num in range(pdf_document.page_count):
                page = pdf_document[page_num]
                text += page.get_text()
            
            return text
        
        except Exception as e:
            raise Exception(f"Error processing PDF: {str(e)}")
    
    def extract_pages(self, file_obj, start_page: int = 0, end_page: Optional[int] = None) -> List[str]:
        """
        Extracts text from specific pages of the PDF
        
        Args:
            file_obj: PDF file object
            start_page: Starting page number (0-based)
            end_page: Ending page number (optional)
        Returns:
            List[str]: List of extracted text by page
        """
        try:
            if isinstance(file_obj, str):
                pdf_document = fitz.open(file_obj)
            else:
                pdf_document = fitz.open(stream=file_obj.read(), filetype="pdf")
            
            end_page = end_page or pdf_document.page_count
            pages = []
            
            for page_num in range(start_page, min(end_page, pdf_document.page_count)):
                page = pdf_document[page_num]
                pages.append(page.get_text())
            
            return pages
        
        except Exception as e:
            raise Exception(f"Error extracting pages: {str(e)}")
    
    def get_metadata(self, file_obj) -> dict:
        """
        Extracts PDF metadata
        
        Args:
            file_obj: PDF file object
        Returns:
            dict: PDF metadata
        """
        try:
            if isinstance(file_obj, str):
                pdf_document = fitz.open(file_obj)
            else:
                pdf_document = fitz.open(stream=file_obj.read(), filetype="pdf")
            
            metadata = pdf_document.metadata
            return {
                "title": metadata.get("title", ""),
                "author": metadata.get("author", ""),
                "subject": metadata.get("subject", ""),
                "keywords": metadata.get("keywords", ""),
                "page_count": pdf_document.page_count
            }
        
        except Exception as e:
            raise Exception(f"Error extracting metadata: {str(e)}")