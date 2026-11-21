number = []
for i in range(10):
    number1 = int(input("Enter a number"))
    number.append(number1)
print(number)
larger_number = number[0]

for i in number:
    if i > larger_number:
        larger_number = i 
print(larger_number)