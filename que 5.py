s = input("Enter a string: ")

print("\nChoose an operation:")
print("a. Find the frequency of a character in a string.")
print("b. Replace a character by another character in a string.")
print("c. Remove the first occurrence of a character from a string.")
print("d. Remove all occurrences of a character from a string.")

choice = input("\nEnter your choice (a/b/c/d): ")

if choice == 'a':
    ch = input("Enter the character to find frequency: ")
    freq = s.count(ch)
    print(f"Frequency of '{ch}' in \"{s}\" is:", freq)

elif choice == 'b':
    old = input("Enter the character to replace: ")
    new = input("Enter the new character: ")
    result = s.replace(old, new, 1)  # replace first occurrence
    print("String after replacement:", result)

elif choice == 'c':
    ch = input("Enter the character to remove (first occurrence): ")
    result = s.replace(ch, "", 1)  # only first occurrence removed
    print("String after removing first occurrence:", result)

elif choice == 'd':
    ch = input("Enter the character to remove (all occurrences): ")
    result = s.replace(ch, "")
    print("String after removing all occurrences:", result)

else:
    print("Invalid choice!")