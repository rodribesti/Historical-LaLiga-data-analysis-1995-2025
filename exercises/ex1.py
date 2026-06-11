"""Ejercicio 1: carga y limpieza del dataset, y distribución de goles."""

import pandas as pd
import matplotlib.pyplot as plt
import config


def load_and_eda(file):
    """
    Carga el dataset y elimina columnas preestablecidas.

    Args:
        file (str): ruta relativa al dataset.

    Returns:
        pd.DataFrame: dataset cargado y personalizado.
    """
    data: pd.DataFrame = pd.read_csv(file)
    data = data.drop(columns=['HTHG', 'HTAG', 'HTR'])

    return data


def plot_home_away_goals(data):
    """
    Figura con dos plots que muestra la distribución de goles marcados
    por los equipos en casa y fuera.

    Args:
        data (pd.DataFrame): dataset limpio proveniente de load_and_eda.
    """
    _, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].boxplot(
        data['FTHG'],
        patch_artist=True,
        boxprops={"facecolor": "lightblue", "color": "blue"},
        medianprops={"color": "darkblue"}
    )
    axes[0].set_title('Goles equipo local')
    axes[0].set_ylabel('Goles')

    axes[1].boxplot(
        data['FTAG'],
        patch_artist=True,
        boxprops={"facecolor": "lightgreen", "color": "green"},
        medianprops={"color": "darkgreen"}
    )
    axes[1].set_title('Goles equipo visitante')
    axes[1].set_ylabel('Goles')

    plt.savefig(f"img/grafica_boxplot_ex1_{config.nom_alumne}_{config.date_time}.png")
    plt.show()
