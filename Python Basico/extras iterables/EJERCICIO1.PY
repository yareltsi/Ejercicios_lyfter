
number = []
for i in range(10):
    element = int(input("Ingresa diez numeros"))
    number.append(element)
target_number = int(input("Que numero desea buscar"))
counter = 0 
for element in number:
    if element == target_number:
        counter = counter + 1
print("El numero", target_number, "aparece", counter, "veces")






   

                           