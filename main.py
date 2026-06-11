import argparse

import config
from exercises.ex1 import load_and_eda, plot_home_away_goals
from exercises.ex2 import total_matches, plot_matches_team_total
from exercises.ex3 import goals_distribution, plot_goals_distribution
from exercises.ex4 import FTR, plot_FTR
from exercises.ex5 import add_points, fun_total_points, alltime_winner
from exercises.ex6 import (
    fun_total_goals,
    fun_total_goals_by_team,
    fun_summary_1996_2025,
    podium,
)
from exercises.ex7 import graf


def main():
    parser = argparse.ArgumentParser(
        description="PEC4 - Análisis de LaLiga. Ejecuta los ejercicios de forma incremental."
    )
    parser.add_argument(
        "-ex",
        type=int,
        required=True,
        help="Ejecuta los N primeros ejercicios (ej: -ex 5 ejecuta del 1 al 5)."
    )
    args = parser.parse_args()

    file = "data/LaLiga_Matches.csv"
    data = None

    # Ejercicio 1 
    if args.ex >= 1:
        print("\nEJERCICIO 1")
        print("Las primeras y últimas filas del dataset son:\n")
        data = load_and_eda(file)
        print(data.head(5))
        print(data.tail(5))
        print("\nEl dataset contiene la siguiente información:\n")
        data.info()
        print("\nLa distribución de los goles es la siguiente:")
        plot_home_away_goals(data)

    #  Ejercicio 2 
    if args.ex >= 2:
        print("\n EJERCICIO 2")
        matches_team_total, always_first_division = total_matches(data)
        print("\nLos partidos totales de los 10 primeros equipos fueron:")
        print(matches_team_total.head(10))
        print("\nLos equipos que siempre jugaron en primera división son:")
        print(always_first_division)
        plot_matches_team_total(matches_team_total)

    # Ejercicio 3 
    if args.ex >= 3:
        print("\nEJERCICIO 3")
        distr_goals_home, distr_goals_away = goals_distribution(data)
        print("\nDistribución de goles en casa:")
        print(distr_goals_home)
        print("\nDistribución de goles fuera:")
        print(distr_goals_away)
        plot_goals_distribution(distr_goals_home, distr_goals_away)

    # Ejercicio 4
    if args.ex >= 4:
        print("\n EJERCICIO 4")
        ftr, porcentaje_win_local = FTR(data)
        print(ftr)
        print(f"El porcentaje de partidos que ganan los locales es de {porcentaje_win_local:.2f} %")
        plot_FTR(ftr)

    # Ejercicio 5 
    if args.ex >= 5:
        print("\nEJERCICIO 5")
        data = add_points(data)
        series_points, df_points = fun_total_points(data)
        print("\nTotal de puntos acumulados por equipo (10 primeros):")
        print(df_points.head(10))
        ganador_historico = alltime_winner(df_points)
        print("\nEl ganador histórico de la liga acumulada es:")
        print(ganador_historico)

    # Ejercicio 6 
    if args.ex >= 6:
        print("\nEJERCICIO 6")
        home_goals, away_goals, total_goals = fun_total_goals(data)
        print(f"\nGoles local: {home_goals}, visitante: {away_goals}, total: {total_goals}")
        home_goals_by_team, away_goals_by_team, total_goals_by_team = fun_total_goals_by_team(data)
        print("\nGoles totales por equipo (10 primeros):")
        print(total_goals_by_team.head(10))
        summary_1996_2025 = fun_summary_1996_2025(
            df_points, home_goals_by_team, away_goals_by_team, total_goals_by_team
        )
        print("\nResumen 1996-2025:")
        print(summary_1996_2025.head())
        podium(summary_1996_2025)

    # === Ejercicio 7 ===
    if args.ex >= 7:
        print("\n========== EJERCICIO 7 ==========")
        selected_teams = df_points['Team'].head(5).tolist()
        print("\nEquipos seleccionados para el grafo (5 con más puntos):")
        print(selected_teams)
        graf(data, selected_teams)


if __name__ == "__main__":
    main()