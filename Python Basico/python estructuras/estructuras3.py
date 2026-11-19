import random
secret_number = random.randint(1 , 10)
user_number = int(input("Adivina el numero del 1 al 10"))

while user_number != secret_number:
    print("Incorrecto")
    user_number = int(input("Intente otra vez"))

print("correcto")
