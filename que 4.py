char = input("Enter a character: ")

if len(char) != 1:
    print("Please enter exactly one character!")
else:
    # a. Check type of character
    if char.isalpha():  # if it's a letter
        print("It is a letter.")
        
        # b. Check case
        if char.isupper():
            print("The letter is uppercase.")
        else:
            print("The letter is lowercase.")
    
    elif char.isdigit():  # if it's a digit
        print("It is a numeric digit.")
        
        # c. Print its name
        digit_names = ["ZERO", "ONE", "TWO", "THREE", "FOUR", 
                       "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        print("Its name is:", digit_names[int(char)])
    
    else:
        print("It is a special character.")