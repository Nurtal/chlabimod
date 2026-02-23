from models import Chlabichou, Cellule, Gene
from simulation import Engine


def test_run():
    """ """

    # Création de gènes
    g1 = Gene("A", 0.8)
    g2 = Gene("B", 0.5)
    g3 = Gene("C", 0.3)


    print(g3.expression)
    g3.induced(5)
    print(g3.expression)

    g3.inductor_list.append('A')

    print(g3.inductor_list)

    # Création cellule
    cellule = Cellule([g1, g2, g3])
    cellule.apply_regulation()

    # Création animal
    animal = Chlabichou("Chat", [cellule])
    engine = Engine([cellule])
    engine.run(10)

    for etat in engine.historique:
        print(etat)


def craft_chlabichou():
    """ """

    print("Tardis")


if __name__ == "__main__":

    craft_chlabichou()
    test_run()

