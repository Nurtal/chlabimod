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

    def apply_regulation(self):
        """Look for inhibition and induction in between the genes present and expressed in the cell"""

        for g in self._genes:
            for gi in self._genes:
                
                # check for inductor
                if gi.nom in g.inductor_list:
                    g.induced(gi.expression)
                    print(f"[LOG] gene {g.nom} is induced by gene {gi.nom}") # log purpose, to put in a better place

                # check for inhibitor
                if gi.nom in g.inhibitor_list:
                    g.inhibited(gi.expression)
                    print(f"[LOG] gene {g.nom} is inhibited by gene {gi.nom}") # log purpose, to put in a better place


    def __repr__(self):
        return f"Cellule({self._genes})"

