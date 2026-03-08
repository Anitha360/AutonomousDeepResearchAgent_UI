import chromadb
from sentence_transformers import SentenceTransformer

class VectorStore:

    def __init__(self):

        self.client = chromadb.Client()

        self.collection = self.client.create_collection("research_memory")

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def add_document(self, text, source):

        embedding = self.model.encode(text).tolist()

        self.collection.add(
            documents=[text],
            embeddings=[embedding],
            metadatas=[{"source": source}],
            ids=[source]
        )

    def search(self, query):

        embedding = self.model.encode(query).tolist()

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=5
        )

        return results["documents"]