import networkx as nx
from config.logger import get_logger

logger = get_logger("KnowledgeGraph")

class KnowledgeGraph:

    def __init__(self):
        logger.info("Initializing Knowledge Graph")

        try:

            self.graph = nx.Graph()
            logger.info("Knowledge Graph initialized successfully")

        except Exception as e:
            logger.error("Failed to initialize Knowledge Graph: %s", str(e))
            raise

    def add_relationship(self, entity1, relation, entity2):
        logger.info(
            "Adding relationship: %s --(%s)--> %s",
            entity1, relation, entity2
        )

        try:

            self.graph.add_node(entity1)
            self.graph.add_node(entity2)

            self.graph.add_edge(entity1, entity2, relation=relation)
            logger.info("Relationship added successfully")

        except Exception as e:

            logger.error(
                "Failed to add relationship between %s and %s: %s",
                entity1, entity2, str(e)
            )

    def get_relations(self, entity):
        
        logger.info("Fetching relationships for entity: %s", entity)

        try:
            relations = list(self.graph.edges(entity, data=True))

            logger.info(
                "Total relations found for %s: %d",
                entity, len(relations)
            )

            return relations

        except Exception as e:

            logger.error(
                "Failed to retrieve relations for %s: %s",
                entity, str(e)
            )

            return []