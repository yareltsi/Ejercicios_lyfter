import json
from pathlib import Path


# Función para leer el archivo JSON
def load_pokemon():
    file_path = Path(__file__).resolve().parent.parent / "pokemon.json"

    with open(file_path, "r", encoding="utf-8") as file:
        pokemon_list = json.load(file)

    return pokemon_list


# Función para mostrar los Pokémon
def show_pokemon(pokemon_list):
    for pokemon in pokemon_list:
        print("Nombre:", pokemon["name"])
        print("Tipo:", pokemon["type"])
        print("Nivel:", pokemon["level"])
        print("-------------------------")


# Función principal
def main():
    pokemon_list = load_pokemon()
    show_pokemon(pokemon_list)


if __name__ == "__main__":
    main()
