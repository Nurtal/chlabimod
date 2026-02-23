from typing import List
from .gene import Gene



class Cellule:
    NOMBRE_GENES = 3

    def __init__(self, type_cellule: str, genes: List[Gene]):
        if len(genes) != self.NOMBRE_GENES:
            raise ValueError("Une cellule doit avoir exactement 3 gènes.")

        self.type_cellule = type_cellule
        self._genes = genes
        self.vivante = True

    @property
    def genes(self) -> List[Gene]:
        return self._genes.copy()  # évite modification externe directe

    def expression_moyenne(self) -> float:
        return sum(g.expression for g in self._genes) / self.NOMBRE_GENES

    def mourir(self) -> None:
        self.vivante = False

    def __repr__(self) -> str:
        return (
            f"Cellule(type={self.type_cellule}, "
            f"expression_moyenne={self.expression_moyenne():.2f})"
        )
