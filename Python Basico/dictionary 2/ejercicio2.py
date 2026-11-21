employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

employees_by_department = {}

for employee in employees:
    department = employee["department"]
    if department in employees_by_department:
      employees_by_department[department].append(employee)
    else:
       employees_by_department[department] = [employee]
for department in employees_by_department:
   print("Department:", department)     
   for employee in employees_by_department[department]:
    print(employee["name"]) 
    
