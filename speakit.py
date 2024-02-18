import sys
import string
import re

def main():

    f = open("data.txt", 'r')

    lines = []
    freq = {}
    try:
        for line in f:
            line.translate(str.maketrans('', '', string.punctuation))
            line.split("\n")
            lines.append(line)
        f.close()
    except FileNotFoundError() as e:
        raise("file not found xxx", e)
    finally:
        f.close()


    for line in lines:
        parts = line.split()
        for part in parts:
            part_cleaned= re.sub(r'\W+', '', part)
            if len(part) > 2:
                    part = part_cleaned.strip().lower()
                    if part in freq:
                        freq[part] += 1
                    elif part.isalpha():
                        freq[part] = 1


    sorted_dict = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

    num_words_to_spit = 15
    while True:
        user_input = input("type a substring or press q: ")
        if user_input == 'q':
            sys.exit("game over")
        sub = user_input
        count = 0
        for key in sorted_dict:
            if sub in key:
                if count < num_words_to_spit:
                    print(key)
                    count += 1

    #TODO: 
    #add tests to check above
    #split into functions
    #Need text that does not contain german or other random non-italian words

main()

