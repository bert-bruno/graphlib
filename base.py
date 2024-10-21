# --- Imports and Definitions --- #
from abc import ABC, abstractmethod
from typing import Any, Iterable, Optional
# --- #
class Graph(ABC):
    @abstractmethod
    def add_vertex(self, vertex: Any) -> None:
        """Add a vertex to the graph."""
        pass
# --- #
    @abstractmethod
    def remove_vertex(self, vertex: Any) -> None:
        """Remove a vertex from the graph."""
        pass
# --- #
    @abstractmethod
    def add_edge(self, source: Any, destination: Any) -> None:
        """Add an edge to the graph."""
        pass
# --- #
    @abstractmethod
    def remove_edge(self, stary: Any, end: Any) -> None:
        """Remove an edge from the graph."""
        pass
# --- #
    @abstractmethod
    def has_edge(self, start: Any, end: Any) -> bool:
        """Check if an edge exists between two vertices."""
        pass
# --- #
    @abstractmethod
    def get_edge_weight(self, start: Any, end: Any) -> Optional[float]:
        """Get the weight of an edge."""
        pass
# --- #
    @abstractmethod
    def get_vertices(self) -> Iterable[Any]:
        """Get all vertices in the graph."""
        pass
# --- #
    @abstractmethod
    def is_directed(self) -> bool:
        """Check if the graph is directed."""
        pass