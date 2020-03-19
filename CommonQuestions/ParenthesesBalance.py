def isBalanced(s):
	left_chars, LOOKUP = [], {"{":"}", "(":")", "[":"]"}
	for c in s:
		if c in LOOKUP:
			left_chars.append(c)
		elif not left_chars or LOOKUP[left_chars.pop()] != c:
			return False
	return not left_chars

string = "{[()]}"
print(isBalanced(list(string)))

# print(isBalanced('(())'))
# print(isBalanced('[()]]'))
print(isBalanced('{{[[}}['))
print(isBalanced(' '))
