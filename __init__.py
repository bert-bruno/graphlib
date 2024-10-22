"""
    A graph theory package implementing various graph representatons and algorithms.
"""

__version__ = "0.1.0"
__author__ = "Bruno Bertholdi"

from .base import Graph
from .adjacency_list import AdjacencyListGraph
from .adjacency_matrix import AdjacencyMatrixGraph
from . import algorithms
from . import utils

def create_graph(graph_type="list", directed=False):
    """
    Factory function to create a graph object.
    """

    if graph_type == "list":
        return AdjacencyListGraph(directed=directed)
    elif graph_type == "matrix":
        return AdjacencyMatrixGraph(directed=directed)
    else:
        raise ValueError("Invalid graph type. Graphs must be either 'list' or 'matrix'.")
    
__all__ = ['Graph',
           'AdjacencyListGraph',
           'AdjacencyMatrixGraph',
           'create_graph',
           'algorithms',
           'utils'
           ]