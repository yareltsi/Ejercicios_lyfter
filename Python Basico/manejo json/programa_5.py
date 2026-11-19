
import json
from pathlib import Path


# Función 1: Leer el archivo JSON
def load_pokemon():
    file_path = Path(__file__).resolve().parent.parent / "pokemon.json"

    with open(file_path, "r", encoding="utf-8") as file:
        pokemon_list = json.load(file)

    return pokemon_list


# Función 2: Agrupar los Pokémon por tipo
def group_pokemon(pokemon_list):
    groups = {}

    for pokemon in pokemon_list:
        pokemon_type = pokemon["type"].strip().lower()
        level = int(pokemon["level"])

        if pokemon_type not in groups:
            groups[pokemon_type] = []

        groups[pokemon_type].append(level)

    return groups


# Función 3: Calcular los promedios
def calculate_averages(groups):
    averages = {}

    for pokemon_type, levels in groups.items():
        average = sum(levels) / len(levels)
        averages[pokemon_type] = average

    return averages


# Función 4: Mostrar los resultados
def show_averages(averages):
    for pokemon_type, average in averages.items():
        print("Tipo:", pokemon_type)
        print("Promedio de nivel:", round(average, 2))
        print("-------------------------")


# Función principal
def main():
    pokemon_list = load_pokemon()
    groups = group_pokemon(pokemon_list)
    averages = calculate_averages(groups)
    show_averages(averages)


if __name__ == "__main__":
    main()
