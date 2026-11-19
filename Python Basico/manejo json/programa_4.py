import json
from pathlib import Path


# Función 1: Leer el archivo JSON
def load_pokemon():
    file_path = Path(__file__).resolve().parent.parent / "pokemon.json"

    with open(file_path, "r", encoding="utf-8") as file:
        pokemon_list = json.load(file)

    return pokemon_list


# Función 2: Mostrar las estadísticas
def show_stats(pokemon_list):
    for pokemon in pokemon_list:
        stats = pokemon["stats"]

        print("Nombre:", pokemon["name"])
        print("Ataque:", stats["attack"])
        print("Defensa:", stats["defense"])
        print("Velocidad:", stats["speed"])
        print("-------------------------")


# Función principal
def main():
    pokemon_list = load_pokemon()
    show_stats(pokemon_list)


if __name__ == "__main__":
    main()
