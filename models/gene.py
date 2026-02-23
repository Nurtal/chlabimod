import random

class Gene:
    def __init__(self, nom: str, expression: float):
        if not (0.0 <= expression <= 1.0):
            raise ValueError("Expression doit être entre 0 et 1")

        self.nom = nom
        self.expression = expression
        self.inductor_list = []
        self.inhibitor_list = []

    def varier(self, amplitude: float = 0.1) -> None:
        variation = random.uniform(-amplitude, amplitude)
        nouvelle_valeur = self.expression + variation

        # Clamp entre 0 et 1
        self.expression = max(0.0, min(1.0, nouvelle_valeur))

    def induced(self, factor:float):
        """
        Modify gene expression if gene is induced
        Args:
            - factor (float) : supposed to be between 0 and 1
        """

        # compute variation
        variation = self.expression * factor

        # new expression
        self.expression = self.expression + variation
        
    def inhibited(self, factor:float):
        """
        Modify gene expression if gene is inhibited
        Args:
            - factor (float) : supposed to be between 0 and 1
        """

        # compute variation
        variation = self.expression * factor

        # new expression
        self.expression = self.expression - variation

    def __repr__(self):
        return f"{self.nom}:{self.expression:.2f}"

