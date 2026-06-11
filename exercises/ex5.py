"""Exercise 5"""

import pandas as pd


def add_points(data):
    """
    Añade al dataset los puntos conseguidos por el local (points_home) y
    el visitante (points_away) en cada partido: 3, 1 o 0.

    Args:
        data (pd.DataFrame): dataset limpio.

    Returns:
        pd.DataFrame: dataset con las dos columnas de puntos añadidas.
    """
    data['points_home'] = 0
    data['points_away'] = 0

    empate = data['FTHG'] == data['FTAG']
    data.loc[empate, 'points_home'] = 1
    data.loc[empate, 'points_away'] = 1

    gana_local = data['FTHG'] > data['FTAG']
    data.loc[gana_local, 'points_home'] = 3

    gana_visitante = data['FTHG'] < data['FTAG']
    data.loc[gana_visitante, 'points_away'] = 3

    return data


def fun_total_points(data):
    """
    Calcula el total de puntos acumulados por cada equipo desde 1995.

    Args:
        data (pd.DataFrame): dataset con points_home y points_away.

    Returns:
        tuple[pd.Series, pd.DataFrame]: misma información como Series y DataFrame.
    """
    puntos_local = data.groupby('HomeTeam')['points_home'].sum()
    puntos_visitante = data.groupby('AwayTeam')['points_away'].sum()

    total = puntos_local.add(puntos_visitante, fill_value=0)
    total = total.sort_values(ascending=False)
    total.name = 'TotalPoints'

    df_total_points = total.reset_index()
    df_total_points.columns = ['Team', 'TotalPoints']

    return total, df_total_points

def alltime_winner(df_total_points):
    """
    Devuelve el equipo con más puntos acumulados de toda la historia.

    Args:
        df_total_points (pd.DataFrame): puntos totales por equipo.

    Returns:
        pd.Series: fila del equipo ganador.
    """
    ganador = df_total_points.loc[df_total_points['TotalPoints'].idxmax()]
    return ganador

