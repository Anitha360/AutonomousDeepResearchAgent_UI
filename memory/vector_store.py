import chromadb
from sentence_transformers import SentenceTransformer
from config.logger import get_logger

logger = get_logger("VectorStore")

class VectorStore:

    def __init__(self):
        logger.info("Initializing VectorStore")

        try:

            self.client = chromadb.Client()

            self.collection = self.client.create_collection("research_memory")

            self.model = SentenceTransformer("all-MiniLM-L6-v2")
            logger.info("VectorStore initialized successfully")
            
        except Exception as e:
            logger.error("Failed to initialize VectorStore: %s", str(e))
            raise

    def add_document(self, text, source):
        logger.info("Adding document to vector store. Source: %s", source)
        
        try:
            logger.info("Generating embedding for document")
            embedding = self.model.encode(text).tolist()

            self.collection.add(
                documents=[text],
                embeddings=[embedding],
                metadatas=[{"source": source}],
                ids=[source]
            )
            logger.info("Document successfully stored in vector database")

        except Exception as e:

            logger.error("Failed to store document from %s: %s", source, str(e))

    def search(self, query):
        logger.info("Searching vector store for query: %s", query)

        try:
            logger.info("Generating embedding for query")

            embedding = self.model.encode(query).tolist()

            results = self.collection.query(
                query_embeddings=[embedding],
                n_results=5
            )
            
            logger.info("Vector search completed. Results found: %d", len(results["documents"]))

            return results["documents"]
        
        except Exception as e:

            logger.error("Vector search failed: %s", str(e))

            return []