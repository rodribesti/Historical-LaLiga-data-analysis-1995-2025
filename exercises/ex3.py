"""Ejercicio 3"""

import pandas as pd
import matplotlib.pyplot as plt

import config


def goals_distribution(data):
    """
    Devuelve dos dataframes con el número de goles marcados como índice y
    el número de partidos en que se marcaron como columna (casa y fuera).

    Args:
        data (pd.DataFrame): dataset limpio.

    Returns:
        tuple[pd.DataFrame, pd.DataFrame]: (distr_goals_home, distr_goals_away).
    """
    distr_goals_home = data['FTHG'].value_counts().sort_index().to_frame(name='Quantity of matches')
    distr_goals_away = data['FTAG'].value_counts().sort_index().to_frame(name='Quantity of matches')

    return distr_goals_home, distr_goals_away


def plot_goals_distribution(distr_goals_home, distr_goals_away):
    """
    Representación gráfica de la distribución de goles (casa y visitante).

    Args:
        distr_goals_home (pd.DataFrame): distribución de goles en casa.
        distr_goals_away (pd.DataFrame): distribución de goles fuera.
    """
    _, axes3 = plt.subplots(1, 2, figsize=(10, 9))

    axes3[0].bar(distr_goals_home.index, distr_goals_home['Quantity of matches'])
    axes3[0].set_title('Home Goals Distribution')
    axes3[0].set_xlabel('Goals')
    axes3[0].set_ylabel('Matches')

    axes3[1].bar(distr_goals_away.index, distr_goals_away['Quantity of matches'])
    axes3[1].set_title('Away Goals Distribution')
    axes3[1].set_xlabel('Goals')
    axes3[1].set_ylabel('Matches')

    plt.tight_layout()
    plt.savefig(f"img/grafica_goals_distribution_ex3_{config.nom_alumne}_{config.date_time}.png")
    plt.show()

    