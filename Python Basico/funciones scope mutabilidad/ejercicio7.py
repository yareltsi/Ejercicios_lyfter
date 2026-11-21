def sort_words(my_string):
    words_list = my_string.split("-")
    words_list.sort()
    sorted_string = "-".join(words_list)


    return sorted_string

print(sort_words("python-variable-funcion-computadora-monitor"))
