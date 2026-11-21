def convert_to_int(list):

    for item in list:
       try:
        converted_number = int(item)
        print(f"Converted '{item}' to {converted_number}.")
    
       except ValueError:
           print(f"Cannot convert '{item}' to an integer.")


my_list = ["10", "20", "abc", "30.5", "40"]
convert_to_int(my_list)