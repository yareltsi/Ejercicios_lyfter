name_student = "Jose"


def list_ecoworld_student():
  global name_student
  name_student = "Maria"
  print(f'Inside function: {name_student}')


list_ecoworld_student()
print(f'Outside function: {name_student}')