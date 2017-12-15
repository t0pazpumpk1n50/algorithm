import sys

mirror_map = {
    'A': 'A',
    'E': '3',
    'H': 'H',
    'I': 'I',
    'J': 'L',
    'M': 'M',
    'O': 'O',
    'S': '2',
    'T': 'T',
    'U': 'U',
    'V': 'V',
    'W': 'W',
    'X': 'X',
    'Y': 'Y',
    'Z': '5',
    '1': '1',
    '8': '8'
}

for k, v in list(mirror_map.items()):
    mirror_map[v] = k


def mirror(s):
    return ''.join(mirror_map.get(c, '') for c in s)


for line in sys.stdin.read().splitlines():
    if line != line[::-1]:
        if line[::-1] == mirror(line):
            print(line + ' -- is a mirrored string.')
        else:
            print(line + ' -- is not a palindrome.')
    else:
        if line[::-1] == mirror(line):
            print(line + ' -- is a mirrored palindrome.')
        else:
            print(line + ' -- is a regular palindrome.')
    print()


