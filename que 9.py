import math

# ---- Read file ----
fname = input("Enter file name: ")
f = open(fname, "r")
lines = f.readlines()
f.close()

# a) Count characters, words, lines
text = "".join(lines)
print("Total characters:", len(text))
print("Total words     :", len(text.split()))
print("Total lines     :", len(lines))

# b) Character frequency (dictionary)
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print("\nCharacter Frequencies:", freq)

# c) Print words in reverse order
words = text.split()
print("\nWords in reverse order:")
print(words[::-1])

# d) Copy odd and even lines to files
f1 = open("File1.txt", "w")   # even lines
f2 = open("File2.txt", "w")   # odd lines

for i, line in enumerate(lines, start=1):
    if i % 2 == 0:
        f1.write(line)
    else:
        f2.write(line)

f1.close()
f2.close()
print("\nEven lines copied to File1.txt")
print("Odd  lines copied to File2.txt")
