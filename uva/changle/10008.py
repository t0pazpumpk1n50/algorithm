n = int(input())
s = ''
for i in range(n):
    s = s + input()

s = s.upper()

letter_counts = {}
for c in s:
    if c not in letter_counts:
        letter_counts[c] = 1
    else:
        letter_counts[c] = letter_counts[c] + 1

items = letter_counts.items()

items = sorted(items, key=lambda x: (-x[1], x[0]))

for k,v in items:
    if k.isalpha():
        print(k, v)
