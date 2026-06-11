"""Exercise 6"""

import pandas as pd
import matplotlib.pyplot as plt
import config


def fun_total_goals(data):
    """
    Devuelve los goles totales marcados como local, como visitante y en total.

    Args:
        data (pd.DataFrame): dataset de partidos.

    Returns:
        (home_goals, away_goals, total_goals).
    """
    home_goals = int(data['FTHG'].sum())
    away_goals = int(data['FTAG'].sum())
    total_goals = home_goals + away_goals

    return home_goals, away_goals, total_goals


def fun_total_goals_by_team(data):
    """
    Goles marcados por cada equipo como local, como visitante y en total.

    Args:
        data: dataset de partidos.

    Returns:
        tupla de tres DataFrames: home, away y total de goles por equipo.
    """
    home = data.groupby('HomeTeam')['FTHG'].sum()
    away = data.groupby('AwayTeam')['FTAG'].sum()
    total = home.add(away, fill_value=0).astype(int)

    home_goals_by_team = home.sort_values(ascending=False).reset_index()
    home_goals_by_team.columns = ['Team', 'HomeGoals']

    away_goals_by_team = away.sort_values(ascending=False).reset_index()
    away_goals_by_team.columns = ['Team', 'AwayGoals']

    total_goals_by_team = total.sort_values(ascending=False).reset_index()
    total_goals_by_team.columns = ['Team', 'TotalGoals']

    return home_goals_by_team, away_goals_by_team, total_goals_by_team


def fun_summary_1996_2025(total_points_by_team,home_goals_by_team, away_goals_by_team,total_goals_by_team):
    """
    Concatena los cuatro DataFrames (puntos, goles local, goles visitante,
    goles totales) en un único resumen por equipo.

    Returns:
        pd.DataFrame: resumen combinado, ordenado por puntos.
    """
    summary = pd.concat(
        [
            total_points_by_team.set_index('Team'),
            home_goals_by_team.set_index('Team'),
            away_goals_by_team.set_index('Team'),
            total_goals_by_team.set_index('Team'),
        ],
        axis=1
    )

    summary = summary.sort_values('TotalPoints', ascending=False).reset_index()

    return summary


def podium(summary_1996_2025: pd.DataFrame) -> None:
    """
    Dibuja un podio con los tres primeros equipos del resumen.

    Args:
        summary_1996_2025 (pd.DataFrame): resumen ordenado por puntos.
    """
    top3 = summary_1996_2025.head(3)

    equipos = top3['Team'].tolist()
    puntos = top3['TotalPoints'].tolist()

    posiciones = [0, 1, 2]
    alturas = [puntos[1], puntos[0], puntos[2]]
    nombres = [equipos[1], equipos[0], equipos[2]]
    colores = ['silver', 'gold', "#eb7311"]

    _, ax = plt.subplots(figsize=(8, 6))
    barras = ax.bar(posiciones, alturas, color=colores)

    for barra, nombre in zip(barras, nombres):
        ax.text(
            barra.get_x() + barra.get_width() / 2,
            barra.get_height(),
            nombre,
            ha='center', va='bottom'
        )

    ax.set_xticks([])
    ax.set_yticks([])

    plt.tight_layout()
    plt.savefig(f"img/grafica_podium_ex6_{config.nom_alumne}_{config.date_time}.png")
    plt.show()

