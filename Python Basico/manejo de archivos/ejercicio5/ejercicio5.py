def add_text(path):
    text = input("Enter a line of text: ")

    with open(path, "a", encoding="utf-8") as file:
        file.write(text + "\n")

    print("The text was added to the end of the file.")

add_text("records.txt")