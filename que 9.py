def process_file(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found!")
        return

    # (a) Total number of characters, words and lines
    num_lines = len(lines)
    num_chars = sum(len(line) for line in lines)
    num_words = sum(len(line.split()) for line in lines)

    print("Total characters:", num_chars)
    print("Total words:", num_words)
    print("Total lines:", num_lines)

    # (b) Frequency of each character
    freq = {}
    for line in lines:
        for ch in line:
            freq[ch] = freq.get(ch, 0) + 1

    print("\nCharacter frequencies:")
    for ch, count in freq.items():
        print(repr(ch), ":", count)

    # (c) Print words in reverse order
    words = []
    for line in lines:
        words.extend(line.split())
    print("\nWords in reverse order:")
    print(" ".join(words[::-1]))

    # (d) Copy even and odd lines into different files
    with open("File1.txt", "w") as f1, o
