quantity = int(input("Cuantas notas vas a ingresar"))
number_list = []
for i in range(quantity):
     enter_grades = int(input("Ingresa las notas"))
     number_list.append(enter_grades)
accumulator = 0 
for enter_grades in number_list:
    accumulator = accumulator + enter_grades
average = accumulator / len(number_list)
greater_list = []
for enter_grades in number_list:
    if enter_grades > average:
       greater_list.append(enter_grades)
print("Promedio:", average)
print("Nueva lista:", greater_list)



