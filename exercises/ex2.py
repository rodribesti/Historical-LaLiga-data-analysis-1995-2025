"""Ejercicio 2"""

import pandas as pd
import matplotlib.pyplot as plt

import config


def total_matches(data):
    """
    Devuelve los partidos jugados por cada equipo y los que siempre han
    estado en primera división (máximo de partidos).

    Args:
        data (pd.DataFrame): dataset de partidos.

    Returns:
        tuple[pd.DataFrame, pd.DataFrame]: (matches_team_total, always_first_division).
    """
    home = data['HomeTeam'].value_counts()
    away = data['AwayTeam'].value_counts()

    matches_team_total = home.add(away, fill_value=0)
    matches_team_total = matches_team_total.sort_values(ascending=False)
    matches_team_total = matches_team_total.reset_index()
    matches_team_total.columns = ['Team', 'Matches']

    maximo = matches_team_total['Matches'].max()
    always_first_division = matches_team_total[matches_team_total['Matches'] == maximo]

    return matches_team_total, always_first_division


def plot_matches_team_total(matches_team_total):
    """
    Gráfico de barras del número de partidos jugados por cada equipo.

    Args:
        matches_team_total (pd.DataFrame): dataset de total_matches.
    """
    _, ax2 = plt.subplots(figsize=(30, 10))

    ax2.bar(
        matches_team_total['Team'],
        matches_team_total['Matches'],
        color='skyblue'
    )
    ax2.set_xlabel('Team')
    ax2.tick_params(axis='x', labelrotation=45)
    ax2.set_ylabel('Quantity of Matches')
    ax2.set_title('Matches per team in first division', fontsize=20)

    plt.savefig(f"img/grafica_matches_team_total_ex2_{config.nom_alumne}_{config.date_time}.png")
    plt.show()

