# ACTIVIDAD 2 
name = input("Ingrese su Nombre")
last_name = input("Ingrese su Apellido")
age = int(input("Ingrese su Edad"))

print(name)
print(last_name)
print(age)
print (type(age))
if age <=2:
    print("Bebe")
elif age <= 10:
    print("nino")
elif age <=12:
    print("Preadolescente")
elif age <= 17:
    print("Adolescente")
elif age <= 25:
    print("Adulto Joven")
elif age <= 64:
    print("Adulto")
else:
    print("Adulto Mayor")



