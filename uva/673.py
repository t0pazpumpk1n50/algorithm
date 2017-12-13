def is_correct(s):
    stack = []
    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        else:  # ) or ]
            if not stack:
                return False
            if c == ')' and stack[-1] == '[' or c == ']' and stack[-1] == '(':
                return False
            stack.pop()
    return not stack


n = int(input())
for _ in range(n):
    print('Yes' if is_correct(input()) else 'No')
