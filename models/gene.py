from dataclasses import dataclass


@dataclass
class Gene:
    nom: str
    expression: float  # entre 0.0 et 1.0

    def __post_init__(self):
        if not (0.0 <= self.expression <= 1.0):
            raise ValueError("L'expression doit être entre 0.0 et 1.0")

    def reguler(self, nouvelle_expression: float) -> None:
        if not (0.0 <= nouvelle_expression <= 1.0):
            raise ValueError("L'expression doit être entre 0.0 et 1.0")
        self.expression = nouvelle_expression
