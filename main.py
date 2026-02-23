from models import Chlabichou, Cellule, Gene


def test_run():
    """ """

    # Création de gènes
    g1 = Gene("A", 0.8)
    g2 = Gene("B", 0.5)
    g3 = Gene("C", 0.3)

    # Création cellule
    cellule = Cellule("neurone", [g1, g2, g3])

    # Création animal
    animal = Chlabichou("Chat", [cellule])

    print(cellule)
    print("Expression globale :", animal.expression_globale())



if __name__ == "__main__":

    test_run()
