char = input("enter the character: ")

if char.isalpha():
    print("it is a letter")
    if char.isupper():
        print("the letter is uppercase")
    else:
        print("the letter is lowercase")

elif char.isdigit():
    print("it is a numeric digit")

    # Dictionary to convert digit to word
    digit_name = {
        "0": "ZERO",
        "1": "ONE",
        "2": "TWO",
        "3": "THREE",
        "4": "FOUR",
        "5": "FIVE",
        "6": "SIX",
        "7": "SEVEN",
        "8": "EIGHT",
        "9": "NINE"
    }

    print("Digit name is:", digit_name[char])

else:
    print("it is a special character")
