def text_lower(path):
    with open(path, 'r', encoding='utf-8') as file:
        with open("uppercase.txt", "w", encoding="utf-8") as output_file:
            for line in file:
                line = line.upper()
                output_file.write(line)

text_lower("minuscula.txt")

