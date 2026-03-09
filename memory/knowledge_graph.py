import networkx as nx
from config.logger import get_logger

logger = get_logger("KnowledgeGraph")

class KnowledgeGraph:

    def __init__(self):

        self.graph = nx.Graph()

    def add_relationship(self, entity1, relation, entity2):
        logger.info("add_relationship")

        self.graph.add_node(entity1)
        self.graph.add_node(entity2)

        self.graph.add_edge(entity1, entity2, relation=relation)

    def get_relations(self, entity):
        #logger.info("Get Relations", list(self.graph.edges(entity, data=True)))
        return list(self.graph.edges(entity, data=True))