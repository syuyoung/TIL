while True:
    word = input()
    if word == '.':
        break
    stack = []

    for i in word:
        if i == '(' or i == ')' or i == '[' or i == ']':
            if len(stack) == 0:
                stack.append(i)
            elif stack[-1] == '(' and i ==')':
                stack.pop()
            elif stack[-1] == '[' and i ==']':
                stack.pop()
            else:
                stack.append(i)

    if len(stack) == 0:
        print('yes')
    else:
        print('no')