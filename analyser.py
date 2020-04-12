import collections
import string

def count_chars():
    with open('fullLogs.txt', 'r') as f:
        original_text = f.read()
        character_set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ~`!@#$%^&*()-_=+[{]}\|;:'\"/?.>,<"
        text = original_text
        alphabet_set = set(character_set)
        count = collections.Counter(c for c in text if c in alphabet_set)

    for letter in characterSet:
        print(letter, count[letter])

    print("Total:", sum(count.values()))

    return count

def main():
    count_letters()


main()