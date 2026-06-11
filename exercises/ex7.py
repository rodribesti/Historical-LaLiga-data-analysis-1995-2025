"""Exercise 7"""

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

import config


def graf(data, selected_teams):
    """
    Dibuja un grafo de conexiones entre los equipos seleccionados, donde
    cada arista indica cuántas veces se han enfrentado (local + visitante).

    Args:
        data: dataset de partidos.
        selected_teams: lista de equipos a incluir.
    """
    # 1. Filtramos: local Y visitante deben estar en la lista
    mask = data['HomeTeam'].isin(selected_teams) & data['AwayTeam'].isin(selected_teams)
    subset = data[mask]

    # 2. Contamos enfrentamientos por pareja, sin importar quién jugó en casa
    conexiones: dict[frozenset, int] = {}
    for _, row in subset.iterrows():
        pareja = frozenset([row['HomeTeam'], row['AwayTeam']])
        if len(pareja) == 2:
            conexiones[pareja] = conexiones.get(pareja, 0) + 1

    # 3. Construimos el grafo
    G = nx.Graph()
    G.add_nodes_from(selected_teams)
    for pareja, n in conexiones.items():
        equipo_a, equipo_b = tuple(pareja)
        G.add_edge(equipo_a, equipo_b, weight=n)

    # 4. Dibujamos
    _, ax = plt.subplots(figsize=(10, 8))
    pos = nx.circular_layout(G)

    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=2500, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=9, ax=ax)
    nx.draw_networkx_edges(G, pos, ax=ax)

    edge_labels = {(a, b): d['weight'] for a, b, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

    ax.axis('off')
    plt.tight_layout()
    plt.savefig(f"img/grafica_grafo_ex7_{config.nom_alumne}_{config.date_time}.png")
    plt.show()
