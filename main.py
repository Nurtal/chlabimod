from models import Chlabichou, Cellule, Gene
from simulation import Engine
import matplotlib.pyplot as plt


def test_run():
    """ """

    # Création de gènes
    g1 = Gene("A", 0.5)
    g2 = Gene("B", 0.5)
    g3 = Gene("C", 0.5)


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


def test_oscillation():
    """ """

    # init data
    data = {'A':[],'B':[], 'C':[]}

    # Création de gènes
    g1 = Gene("A", 0.5)
    g2 = Gene("B", 0.5)
    g3 = Gene("C", 0.5)

    # create links
    g1.inhibitor_list.append('B')
    g2.inhibitor_list.append('C')
    g3.inhibitor_list.append('A')

    g1.inductor_list.append('C')
    g2.inductor_list.append('A')
    g3.inductor_list.append('B')

    # create cell
    cellule = Cellule([g1, g2, g3])

    # custom sim
    steps = 500
    for x in range(steps):

        # apply regulation
        cellule.apply_regulation()

        # display values
        print(f"[EXPR][C{x}] A -> {g1.expression}")
        print(f"[EXPR][C{x}] B -> {g2.expression}")

        # update data
        data['A'].append(g1.expression)
        data['B'].append(g2.expression)
        data['C'].append(g3.expression)


    # plot figs
    plt.figure()
    plt.plot(data['A'], label="Gene A")
    plt.plot(data['B'], label="Gene B")
    plt.plot(data['C'], label="Gene C")
    plt.xlabel("Temps")
    plt.ylabel("Expression")
    plt.title("Evolution")
    plt.legend()
    plt.show()
    


def craft_chlabichou():
    """ """

    print("Tardis")


if __name__ == "__main__":

    # craft_chlabichou()
    # test_run()

    test_oscillation()

