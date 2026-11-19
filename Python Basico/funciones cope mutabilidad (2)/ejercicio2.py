def filter_words(list , n ):
    result = []

    for word in list: 
        if len(word) > n:
            result.appernd(word)


    return result


word = ["sky", "sun", "wonderful", "day"]

number = int(input("Enter the minimum number of letters.: "))

print(filter_words(word, number))