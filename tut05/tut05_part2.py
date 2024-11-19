def check_parentheses_balance():
    stack = []
    string = input("Enter a parentheses: ")
    n = len(string)

    if n & 1:
        print("Not Balanced.")
        return  # Exit the function early

    for i in range(n):
        char = string[i]
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                print("Not Balanced.")
                return
            top = stack.pop()
            if not ((char == ')' and top == '(') or
                    (char == ']' and top == '[') or
                    (char == '}' and top == '{')):
                print("Not Balanced.")
                return

    if stack:
        print("Not Balanced.")
    else:
        print("Balanced.")

check_parentheses_balance()