from .cellule import Cellule
from typing import List



class Chlabichou:
    def __init__(self, nom: str, cellules: List[Cellule]):
        if not cellules:
            raise ValueError("Un animal doit avoir au moins une cellule.")

        self.nom = nom
        self._cellules = cellules

    @property
    def nombre_cellules(self) -> int:
        return len(self._cellules)

    def expression_globale(self) -> float:
        total = sum(c.expression_moyenne() for c in self._cellules)
        return total / self.nombre_cellules

    def __repr__(self) -> str:
        return f"Animal(nom={self.nom}, cellules={self.nombre_cellules})"
