# Taking the string from the user
s = input("Enter a string: ")

# a. Frequency of a character
ch = input("Enter a character to find its frequency: ")
print("Frequency of", ch, "=", s.count(ch))


# b. Replace a character with another
old = input("Enter the character to replace: ")
new = input("Enter the new character: ")
new_string = s.replace(old, new)
print("String after replacement:", new_string)


# c. Remove first occurrence of a character
char_remove_first = input("Enter a character to remove first occurrence: ")
result = s.replace(char_remove_first, "", 1)  # only first occurrence removed
print("String after removing first occurrence:", result)


# d. Remove all occurrences of a character
char_remove_all = input("Enter a character to remove all occurrences: ")
s_all_removed = s.replace(char_remove_all, "")
print("After removing all occurrences:", s_all_removed)
