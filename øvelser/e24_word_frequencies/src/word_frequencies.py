import re

def word_frequencies(filename):
    frequencies = {}
    punctuation = """!"#$%&'()*,-./:;?@[]_"""

    with open(filename, 'r', encoding='utf-8') as file:  # Ensure correct handling of encoding
        for line in file:
            words = line.split()
            for word in words:
                cleaned_word = word.strip(punctuation)
                if cleaned_word in frequencies:  # Check if the word is not empty
                    frequencies[cleaned_word] += 1
                else:
                    frequencies[cleaned_word] = 1

    return frequencies

def main():
    filename = r"C:\Users\lukr\Desktop\H3\Python\PythonData-1-main\øvelser\e24_word_frequencies\src\alice.txt"
    frequencies = word_frequencies(filename)
    for word, count in frequencies.items():
        print(f"{word}\t{count}")


if __name__ == "__main__":
    main()
