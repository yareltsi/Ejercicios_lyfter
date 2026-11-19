def sum_of_value(my_list):
    total = 0


    for item in my_list:
        try:
            converted_value = float(item)
            total = total + converted_value
            print(f"{converted_value} added successfully.")


        except ValueError:
            print(f"Invalid item: {item}.")


    print(f"Total sum: {total}.")

my_list = ["10", "apple", "5.5", "3", "n/a"]

sum_of_value(my_list)