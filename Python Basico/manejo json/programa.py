import json


# Función 1: Abrir y leer el archivo JSON
def load_pokemon():
    with open("pokemon.json", "r", encoding="utf-8") as file:
        pokemon_list = json.load(file)

    return pokemon_list


# Función 2: Mostrar los Pokémon existentes
def show_pokemon(pokemon_list):
    for pokemon in pokemon_list:
        print(pokemon["name"])


# Función 3: Solicitar los datos del nuevo Pokémon
def get_pokemon_data():
    name = input("Ingrese el nombre del nuevo Pokémon: ")
    pokemon_type = input("Ingrese el tipo del nuevo Pokémon: ")
    level = int(input("Ingrese el nivel del nuevo Pokémon: "))
    weight_kg = float(input("Ingrese el peso del nuevo Pokémon: "))

    # Solicitar las estadísticas
    hp = int(input("Ingrese HP: "))
    attack = int(input("Ingrese Attack: "))
    defense = int(input("Ingrese Defense: "))
    sp_attack = int(input("Ingrese Special Attack: "))
    sp_defense = int(input("Ingrese Special Defense: "))
    speed = int(input("Ingrese Speed: "))

    # Solicitar las habilidades
    skills = []
    quantity = int(input("¿Cuántas habilidades desea ingresar?: "))

    for i in range(quantity):
        skill = input(f"Ingrese la habilidad {i + 1}: ")
        skills.append(skill)

    # Preguntar si es shiny
    is_shiny = input("¿Es shiny? (si/no): ").strip().lower() == "si"

    # Preguntar por el objeto equipado
    held_item = input("Objeto equipado (Enter si no tiene): ").strip()

    if held_item == "":
        held_item = None

    return {
        "name": name,
        "pokemon_type": pokemon_type,
        "level": level,
        "weight_kg": weight_kg,
        "hp": hp,
        "attack": attack,
        "defense": defense,
        "sp_attack": sp_attack,
        "sp_defense": sp_defense,
        "speed": speed,
        "skills": skills,
        "is_shiny": is_shiny,
        "held_item": held_item
    }


# Función 4: Crear el diccionario del Pokémon
def create_pokemon(data):
    new_pokemon = {
        "name": data["name"],
        "type": data["pokemon_type"],
        "level": data["level"],
        "weight_kg": data["weight_kg"],
        "is_shiny": data["is_shiny"],
        "held_item": data["held_item"],
        "skills": data["skills"],
        "stats": {
            "hp": data["hp"],
            "attack": data["attack"],
            "defense": data["defense"],
            "sp_attack": data["sp_attack"],
            "sp_defense": data["sp_defense"],
            "speed": data["speed"]
        }
    }

    return new_pokemon


# Función 5: Guardar el archivo JSON
def save_pokemon(pokemon_list):
    with open("pokemon.json", "w", encoding="utf-8") as file:
        json.dump(pokemon_list, file, ensure_ascii=False, indent=4)


# Función principal
def main():
    pokemon_list = load_pokemon()

    show_pokemon(pokemon_list)

    data = get_pokemon_data()

    new_pokemon = create_pokemon(data)

    pokemon_list.append(new_pokemon)

    save_pokemon(pokemon_list)

    print("Nuevo Pokémon agregado correctamente.")


# Ejecutar el programa
if __name__ == "__main__":
    main()
