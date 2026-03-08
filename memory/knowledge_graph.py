import networkx as nx

class KnowledgeGraph:

    def __init__(self):

        self.graph = nx.Graph()

    def add_relationship(self, entity1, relation, entity2):

        self.graph.add_node(entity1)
        self.graph.add_node(entity2)

        self.graph.add_edge(entity1, entity2, relation=relation)

    def get_relations(self, entity):

        return list(self.graph.edges(entity, data=True))