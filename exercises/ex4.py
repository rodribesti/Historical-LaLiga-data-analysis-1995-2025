"""Ejercicio 4"""

import pandas as pd
import matplotlib.pyplot as plt

import config


def FTR(data):
    """
    Cuenta los partidos ganados por locales, visitantes y empatados, y
    calcula el porcentaje de victorias locales.

    Args:
        data (pd.DataFrame): dataset de partidos.

    Returns:
        tuple[pd.DataFrame, float]: (dataframe de resultados, % victorias locales).
    """
    contador_locales = 0
    contador_visitantes = 0
    contador_draw = 0

    for _, row in data.iterrows(): #Tenía escrito index pero no hace falta, corregido 
        if row['FTHG'] == row['FTAG']:
            contador_draw += 1
        elif row['FTHG'] > row['FTAG']:
            contador_locales += 1
        else:
            contador_visitantes += 1

    ftr_dict = {
        'Resultado': ['Victoria local', 'Victoria visitante', 'Empate'],
        'Número de partidos': [contador_locales, contador_visitantes, contador_draw]
    }

    ftr_df = pd.DataFrame(ftr_dict)

    partidos_totales = ftr_df['Número de partidos'].sum()
    porcentaje_win_local = (contador_locales / partidos_totales) * 100

    return ftr_df, porcentaje_win_local


def plot_FTR(ftr):
    """
    Representación de la información de la función FTR.

    Args:
        ftr: dataframe proporcionado por la función FTR.
    """
    _, axes4 = plt.subplots(figsize=(10, 6))

    axes4.barh(ftr['Resultado'], ftr['Número de partidos'], color='skyblue')
    axes4.set_xlabel('Número de partidos')
    axes4.set_ylabel('Resultado')
    axes4.set_title('Distribución de resultados finales')

    plt.tight_layout()
    plt.savefig(f"img/grafica_resultados_partidos_ex4_{config.nom_alumne}_{config.date_time}.png")
    plt.show()

