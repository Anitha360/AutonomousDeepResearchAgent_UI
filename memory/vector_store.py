import chromadb
from sentence_transformers import SentenceTransformer
from config.logger import get_logger

logger = get_logger("VectorStore")
class VectorStore:

    def __init__(self):
        logger.info("Initialize vector store")
        self.client = chromadb.Client()

        self.collection = self.client.create_collection("research_memory")

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def add_document(self, text, source):
        logger.info("vector store: add_document")
        embedding = self.model.encode(text).tolist()

        self.collection.add(
            documents=[text],
            embeddings=[embedding],
            metadatas=[{"source": source}],
            ids=[source]
        )

    def search(self, query):
        logger.info("vector store: search")
        embedding = self.model.encode(query).tolist()

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=5
        )
        #logger.info("vector store", results["documents"])
        return results["documents"]