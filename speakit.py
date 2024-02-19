import sys
import string
import re

def main():

    f = open("data.txt", 'r')

    lines = []
    freq = {}
    try:
        for line in f:
            lines.append(line)
        f.close()
    except FileNotFoundError() as e:
        raise("file not found xxx", e)
    finally:
        f.close()


    for line in lines:
        parts = line.split()
        for part in parts:
            part = part.lower().strip()
            #take out conjugates "l'ufficio"
            if "-" not in part and "'" not in part:  
                part_cleaned = re.sub(r'\W+', '', part)
                if len(part) > 2:
                        if part in freq:
                            freq[part] += 1
                        elif part.isalpha():
                            freq[part] = 1

    sorted_dict = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

    num_words_to_spit = 15
    while True:
        word_not_found = True
        user_input = input("\n"+"Type a substring or press q to quit: " + "\n")
        if user_input == 'q':
            sys.exit("Game over")
        sub = user_input
        count = 0
        for key in sorted_dict:
            if sub in key:
                word_not_found = False
                if count < num_words_to_spit:
                    print(key)
                    count += 1
        if word_not_found:
            print("Sub not in any word")

    #TODO: 
    #add tests to check above
    #split into functions
    #Need text that does not contain so many non-italian words

main()

