def count_vowels(text):
    counter = 0

    for letter in text:
        if letter in "aeiou":
            counter = counter + 1

    return counter


text = input("Enter a text: ")
print(count_vowels(text))  