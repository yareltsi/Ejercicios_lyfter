def declare_variable():
  variable_inside_function_scope = 8
  print(f'Inside function: {variable_inside_function_scope}')

declare_variable()
print(f'Out of function: {variable_inside_function_scope}')