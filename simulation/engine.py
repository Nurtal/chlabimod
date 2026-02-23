from typing import List
from models.cellule import Cellule

class Engine:
    def __init__(self, cellules: List[Cellule]):
        if not cellules:
            raise ValueError("La simulation nécessite au moins une cellule.")

        self._cellules = cellules
        self._temps = 0
        self._historique = []  # stockage des états

    @property
    def temps(self) -> int:
        return self._temps

    @property
    def historique(self) -> list:
        return self._historique.copy()

    def step(self) -> None:
        """Fait avancer la simulation d'un pas de temps."""
        for cellule in self._cellules:
            cellule.evoluer()

        self._temps += 1
        self._enregistrer_etat()

    def run(self, steps: int) -> None:
        for _ in range(steps):
            self.step()

    def _enregistrer_etat(self) -> None:
        """
        Sauvegarde l'expression moyenne de chaque cellule
        à l'instant courant.
        """
        snapshot = {
            "temps": self._temps,
            "cellules": [
                cellule.expression_moyenne()
                for cellule in self._cellules
            ],
        }
        self._historique.append(snapshot)

