def read_text(text , character):
  counter =  0 

  for letter in text:
    if letter == character:
      counter = counter + 1 


  return counter 

my_text = input("Ender the text")
user_character = input("Enter the character to search for")


print(f"The character was found {read_text(my_text, user_character)} times.")