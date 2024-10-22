# --- Imports --- #
from typing import Any, Dict, Set, Optional, Iterable
from collections import defaultdict
from .base import Graph

# --- Classes and methods --- #
class AdjacencyListGraph(Graph):
    """
    Graph implementation using an adjancency list representation.

    This implementation uses a dictionary of dictionaries to represente the graph,
    where the outer dictionary maps vertices to their neighbors, and the inner
    dictionary maps neighbors to edge weights.

    Attributes:
        _graph (Dict): the internal representation of the graph;
        _directed (bool): whether the graph is directed or not.
    """

    def __init__(self, directed: bool = False):
        """
        Initialize an empty graph.

        Args:
            directed (bool): if True, creates a directed graph. Default is False.
        """
        self._graph: Dict[Any, Dict[Any, Optional[float]]] = defaultdict(dict)
        self._directed = directed

    def add_vertex(self, vertex: Any) -> None:
        """
        Add a vertex to the graph if it does not exist.

        Args:
            vertex: the vertex to add.
        """
        if vertex not in self._graph:
            self._graph[vertex] = {}

    def remove_vertex(self, vertex: Any) -> None:
        """
        Remove a vertex from the graph if it exists.

        Args:
            vertex: the vertex to remove.
        """
        pass