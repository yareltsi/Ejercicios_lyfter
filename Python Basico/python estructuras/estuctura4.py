number1 = int(input("Ingrese el primer numero"))
number2 = int(input("Ingrese el segundo numero"))
number3 = int(input("Ingrese el tercer numero"))

if number1 > number2 and number1 > number3:
    print("El mayor es:", number1)
elif number2 > number1 and number2 > number3:
    print("El mayor es:", number2)
else:
    print("El mayor es:", number3)