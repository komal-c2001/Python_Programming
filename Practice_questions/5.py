s = "{[()]}"

stack = []
pairs = {')': '(', '}': '{', ']': '['}

for i in s:
    if i in "({[":
        stack.append(i)

    elif i in ")}]":
        if not stack or stack[-1] != pairs[i]:
            print("Not Balanced")
            break
        stack.pop()
else:
    if len(stack) == 0:
        print("Balanced")
    else:
        print("Not Balanced")