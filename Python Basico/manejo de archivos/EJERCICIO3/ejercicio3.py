def text_lines(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        words = content.split()
        amount = len(words)
        print(f"Cantidad de palabras: {amount}")

text_lines("content.txt")
