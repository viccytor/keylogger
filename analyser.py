import collections
import string

def count_chars():
    with open('fullLogs.txt', 'r') as f:
        original_text = f.read()
        character_set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ~`!@#$%^&*()-_=+[{]}\|;:'\"/?.>,<"
        text = original_text
        # text = original_text.lower()
        alphabet_set = set(character_set)
        counts = collections.Counter(c for c in text if c in alphabet_set)

    for letter in characterSet:
        print(letter, counts[letter])

    print("Total:", sum(counts.values()))

    return counts

def main():
    count_letters()


main()