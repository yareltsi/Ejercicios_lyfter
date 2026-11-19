element_list = []
for i in range(5):
    number_list = int(input("Agrega los numeros de la lista"))
    element_list.append(number_list)
smallest = element_list[0]
for element in element_list:
     if element < smallest:
       smallest = element
print("El menor valor es", smallest) 
