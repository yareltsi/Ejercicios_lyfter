
def song_lines(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines.sort()

    for line in lines:
        print(line.strip())

    with open("canciones_ordenadas.txt", "w", encoding="utf-8") as output_file:
        for line in lines:
            output_file.write(line)

song_lines("cancion.txt") 
