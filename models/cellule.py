from typing import List
from .gene import Gene

class Cellule:
    NOMBRE_GENES = 3

    def __init__(self, genes: list[Gene]):
        if len(genes) != self.NOMBRE_GENES:
            raise ValueError("Une cellule doit avoir exactement 3 gènes.")

        self._genes = genes

    @property
    def genes(self) -> list[Gene]:
        return self._genes.copy()

    def expression_moyenne(self) -> float:
        return sum(g.expression for g in self._genes) / self.NOMBRE_GENES

    def evoluer(self) -> None:
        for gene in self._genes:
            gene.varier()

    def __repr__(self):
        return f"Cellule({self._genes})"

