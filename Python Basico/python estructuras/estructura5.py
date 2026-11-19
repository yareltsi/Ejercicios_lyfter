# cuantas notas se van a ingresar
number_grades = int(input("How many grades do you want to enter"))
# iniciar variable
total =  0
approved_count = 0 
approved_total = 0 

failed_count = 0
failed_total = 0

# pedir una nota
for i in range(number_grades):

    #Pedir una nota
    grade = int(input("Enter note"))

    #Sumar todas las notas para el promedio general 
    
    total = total + grade

    # clasificar todas las notas
    if grade > 70:
     approved_count = approved_count + 1
     approved_total = approved_total + grade
    else:
     
     failed_count = failed_count + 1
     failed_total = failed_total + grade

# Calcular los promedios

average_total = total / number_grades

# evitar divividr entre cero 
if approved_count > 0:
  average_approved = approved_total/ approved_count
else:
    average_approved = 0

if failed_count > 0:
    average_failed = failed_total / failed_count
else:
    average_failed = 0 

# mostrar resultado 
print("Approved_count", approved_count)
print("Failed_count" , failed_count)
print("Average_total", average_total)
print("Average_approved", average_approved)
print("Average_failed", average_failed)





 