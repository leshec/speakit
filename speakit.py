import string
import re

def main():

    f = open("data.txt", 'r')

    lines = []
    words = []
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
            if part and part.isnumeric()==False and len(part) > 2:
                part = part_cleaned.strip().lower()
                words.append(part)


    for word in words:
        if "ce" in word:
            print(word)

    #TODO:
    #trim off ":" or "-" and others
    #check done
    #add tests to check above
    #remove numbers, and do test
    #split into functions
    #create dictionary of words by frequency
    #decide data structure to capture "ce" words
    #can use: contains, list of key="ce", value="words" or key"word", value="ce" 
    #Or somekind of trie 
    #See Tim ripgrep example if unsure. 
    #Need text that does not contain german or other random non-italian words

main()

