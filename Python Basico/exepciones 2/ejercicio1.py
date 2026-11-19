def get_name():
    name = input("Enter your name: ")

    if name.isdigit():
        raise ValueError("The name cannot be a number")

    return name


def get_age():
    try:
        age = int(input("Enter your age: "))
        return age

    except ValueError:
        print("Invalid number")
        return None


def show_message(name, age):
    print(f"Hello {name}, you are {age} years old.")


def main():
    try:
        name = get_name()

    except ValueError as error:
        print(error)
        return

    age = get_age()

    if age is not None:
        show_message(name, age)


if __name__ == "__main__":
    main()