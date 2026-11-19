def file_complete(path):
    with open(path, 'r', encoding='utf-8') as file:
        full_text = ""

        for line in file:
            line = line.strip()
            full_text += line + " "

        full_text = full_text.strip()

    with open("complete.txt", "w", encoding="utf-8") as output_file:
        output_file.write(full_text)


file_complete("archivo.txt")