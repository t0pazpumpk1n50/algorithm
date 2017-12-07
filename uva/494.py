import sys


def count_words(s):
    n = 0
    letter = False
    for c in s:
        if c.isalpha():
            if not letter:
                n += 1
                letter = True
        else:
            letter = False
    return n


for line in sys.stdin:
    print(count_words(line))


