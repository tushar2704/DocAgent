from nomic.embed import Embedding
from llama_index import VectorStoreIndex, Document
from langchain.embeddings import HuggingFaceEmbeddings

class DocumentProcessor:
    def __init__(self):
        self.nomic_embedder = Embedding(
            model="nomic-embed-text-v1.5",
            task_type="search_document"
        )
        self.index = None
    
    def process_document(self, text):
        chunks = self._chunk_text(text)
        embeddings = self.nomic_embedder.embed(chunks)
        documents = [Document(text=chunk) for chunk in chunks]
        self.index = VectorStoreIndex.from_documents(documents)
        return self.index
    
    def _chunk_text(self, text, chunk_size=512):
        return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]