import json
from pathlib import Path


# Función 1: Leer el archivo JSON
def load_pokemon():
    file_path = Path(__file__).resolve().parent.parent / "pokemon.json"

    with open(file_path, "r", encoding="utf-8") as file:
        pokemon_list = json.load(file)

    return pokemon_list


# Función 2: Solicitar el tipo de Pokémon
def get_pokemon_type():
    pokemon_type = input("Ingrese el tipo de Pokémon: ").strip().lower()
    return pokemon_type


# Función 3: Buscar Pokémon por tipo
def filter_pokemon(pokemon_list, pokemon_type):
    matches = []

    for pokemon in pokemon_list:
        if pokemon_type in pokemon["type"].lower():
            matches.append(pokemon)

    return matches


# Función 4: Mostrar los resultados
def show_results(matches):
    if len(matches) == 0:
        print("No se encontraron Pokémon de ese tipo.")
    else:
        for pokemon in matches:
            print("Nombre:", pokemon["name"])


# Función principal
def main():
    pokemon_list = load_pokemon()
    pokemon_type = get_pokemon_type()
    matches = filter_pokemon(pokemon_list, pokemon_type)
    show_results(matches)


if __name__ == "__main__":
    main()
