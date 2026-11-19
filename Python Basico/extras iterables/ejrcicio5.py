word_list = []
for i in range(5):
    word = input("Ingrese una palabra")
    word_list.append(word)
new_list = []
for word in word_list:
  if len(word) > 4:
   new_list.append(word)
print("Nueva lista" , new_list)
