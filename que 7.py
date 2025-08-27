def find_occurrences(text, pattern):
    indices = []
    start = 0
    
    while True:
        index = text.find(pattern, start)  # find pattern from 'start'
        if index == -1:
            break
        indices.append(index)
        start = index + 1  # move to next position
    
    return indices if indices else -1


# Example usage
s1 = input("Enter the main string: ")
s2 = input("Enter the substring to search: ")

result = find_occurrences(s1, s2)
print("Result:", result)
