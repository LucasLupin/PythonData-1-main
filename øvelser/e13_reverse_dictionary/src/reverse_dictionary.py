#!/usr/bin/env python3

def reverse_dictionary(d):
    reverse_d = {}
    for eng_word, fin_words in d.items():
        for fin_word in fin_words:
            if fin_word in reverse_d:
                reverse_d[fin_word].append(eng_word)
            else:
                reverse_d[fin_word] = [eng_word]
    return reverse_d

def main():
    pass
if __name__ == "__main__":
    main()
    d = {'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))
