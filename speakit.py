import string

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
            if part:
                part = part.strip().lower()
                words.append(part)

    print(words[0:150])
    
main()

