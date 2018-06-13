# Implement parentheses balance
def balanceParentheses(parenString):
    if not parenString.isspace():
        chars = [x for x in parenString]
        isBalanced = True
        stack = []
        index = 0
        while index < len(chars) and isBalanced:
            symbol = chars[index]
            if symbol == "(":
                stack.append(symbol)
            else:
                stack.pop()

            index+=1

        if isBalanced and len(stack) == 0:
            return isBalanced
        else:
            return False
    return False

print(balanceParentheses('(())'))
print(balanceParentheses('(()())'))
print(balanceParentheses('((('))
print(balanceParentheses(' '))
