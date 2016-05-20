import matplotlib.pyplot as plt
import networkx as nx

class Infection_Visual(object):
    """Class for visualization of graph and spread of infection"""
    def __init__(self):
        super(Infection_Visual, self).__init__()
        self.graph = nx.Graph()

    def draw(self):
        nx.draw_random(self.graph)
        plt.show(block=False)
