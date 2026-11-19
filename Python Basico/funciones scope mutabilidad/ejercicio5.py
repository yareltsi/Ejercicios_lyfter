def reverse_my_string(my_string):
 reverse_string =""


 for index in range(len(my_string)-1, -1,-1):
   reverse_string = reverse_string + my_string[index]


 return reverse_string


print(reverse_my_string("HOLA MUNDO"))

