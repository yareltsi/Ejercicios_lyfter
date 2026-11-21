number_list = []
for i in range(10):
   element = int(input("Ingrese numeros positivos o negativos"))
   number_list.append(element)
for element in number_list:
   if element >= 0 :
    print("Hay al menos un numero negativo o cero")
    break 
else:
    print("Todos los numeros son positivo") 