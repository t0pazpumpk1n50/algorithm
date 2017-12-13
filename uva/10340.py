import sys

for line in sys.stdin:
    s, t = line.split()
    i = 0
    for c in t:
        if i < len(s) and c == s[i]:
            i += 1
    print('Yes' if i == len(s) else 'No')
