def count_upper_lower(my_text):
    upper_count = 0 
    lower_count = 0 

    for letter in my_text:
        if letter.isupper():
            upper_count = upper_count + 1
        elif letter.islower():
            lower_count = lower_count + 1


    print(f"Upper count:{upper_count}")
    print(f"Lower count:{lower_count}")


count_upper_lower("I Love Nacion Sushi")

      