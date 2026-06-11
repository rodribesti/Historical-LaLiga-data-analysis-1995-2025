"""Archivo de test del ejercicio 6"""

import pandas as pd
from exercises.ex6 import fun_total_goals


def test_caso_normal():
    data = pd.DataFrame({'FTHG': [2, 0, 3], 'FTAG': [1, 1, 0]})
    assert fun_total_goals(data) == (5, 2, 7)


def test_dataframe_vacio():
    data = pd.DataFrame({'FTHG': [], 'FTAG': []})
    assert fun_total_goals(data) == (0, 0, 0)


def test_un_solo_partido():
    data = pd.DataFrame({'FTHG': [4], 'FTAG': [2]})
    assert fun_total_goals(data) == (4, 2, 6)


def test_sin_goles():
    data = pd.DataFrame({'FTHG': [0, 0], 'FTAG': [0, 0]})
    assert fun_total_goals(data) == (0, 0, 0)


def test_autor():
    print("\nAutor: Rodrigo Parafita Bestilleiro")
    assert True
