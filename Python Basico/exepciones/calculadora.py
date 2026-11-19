def show_menu(current_number):
    print("\nCurrent number:", current_number)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear result")
    print("6. Exit")


def get_number():
    try:
        return float(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None


def add(current_number, new_number):
    return current_number + new_number


def subtract(current_number, new_number):
    return current_number - new_number


def multiply(current_number, new_number):
    return current_number * new_number


def divide(current_number, new_number):
    try:
        return current_number / new_number
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return current_number


def calculator():
    current_number = 10

    while True:
        show_menu(current_number)

        option = input("Select an option: ")

        if option == "1":
            new_number = get_number()

            if new_number is not None:
                current_number = add(current_number, new_number)
                print("Result:", current_number)

        elif option == "2":
            new_number = get_number()

            if new_number is not None:
                current_number = subtract(current_number, new_number)
                print("Result:", current_number)

        elif option == "3":
            new_number = get_number()

            if new_number is not None:
                current_number = multiply(current_number, new_number)
                print("Result:", current_number)

        elif option == "4":
            new_number = get_number()

            if new_number is not None:
                current_number = divide(current_number, new_number)
                print("Result:", current_number)

        elif option == "5":
            current_number = 0
            print("Result cleared.")

        elif option == "6":
            print("Calculator closed.")
            break

        else:
            print("Invalid option.")


def main():
    calculator()


if __name__ == "__main__":
    main()