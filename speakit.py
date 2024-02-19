import sys
import re
from collections import Counter

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {filename}") from e

def clean_word(word):
    word = word.lower().strip()
    return re.sub(r'\W+', '', word) if "-" not in word and "'" not in word else None

def count_frequency(lines):
    words = (clean_word(word) for line in lines for word in line.split())
    return Counter(word for word in words if word and len(word) > 2 and word.isalpha())

def get_matching_words(freq, substring):
    return [word for word in freq if substring in word]

def main():
    filename = "data.txt"
    lines = read_file(filename)
    freq = count_frequency(lines)

    num_words_to_print = 15
    while True:
        user_input = input("\nType a substring or press q to quit: \n").strip()
        if user_input == 'q':
            sys.exit("Game over")
        matching_words = get_matching_words(freq, user_input)
        if matching_words:
            print("\n".join(matching_words[:num_words_to_print]))
        else:
            print(f"Substring {user_input} not found in any word")

if __name__ == "__main__":
    main()

