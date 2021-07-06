"""
Problme link -->
Solution link -->

Passed leetcode tests -->  Yes!!

Complexity --> O( n + s)
"""


def min_window(s, t):
	m = len(s)
	n = len(t)

	if not n: return ""

	current_window, desired_window = dict(), dict()

	for c in t:
		desired_window[c] = 1 + desired_window.get(c, 0)

	result, result_length = [-1, -1], float("Infinity")

	formed, desired = 0, len(desired_window)
	l = 0

	for r in range(m):
		c = s[r]

		current_window[c] = 1 + current_window.get(c, 0)

		if c in desired_window and current_window[c] == desired_window[c]:
			formed += 1

		while formed == desired:

			if (r - l + 1) < result_length:
				result_length = r - l + 1
				result = [l, r]
			# pop from left
			current_window[s[l]] -= 1
			if s[l] in desired_window and current_window[s[l]] < desired_window[s[l]]:
				formed -= 1
			l += 1
	l, r = result
	if result_length != float("Infinity"):
		return s[l: r + 1]
	return ""

print(min_window("ADOBECODEBANC", "ABC"))



