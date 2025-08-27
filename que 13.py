


def accept_name():
    try:
        name = input("Enter your name: ")

        # Check if name contains only alphabets and spaces
        if not name.replace(" ", "").isalpha():
            raise InvalidNameError("Name must not contain digits or special characters!")

        print("Valid name entered:", name)

  
