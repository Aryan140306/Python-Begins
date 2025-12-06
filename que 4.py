char=input("enter the character")
if char.isalpha():
    print("it is a letter")
    if char.isupper():
        print('the letter is uppercase')
    else:
        print('the letter is lowercase')
elif char.isdigit():
    print('it is a numeric digit')
else:
    print('it is a special character')
    
