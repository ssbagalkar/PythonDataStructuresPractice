# *
# * *
# * * *
# * * * *
# * * * * *

def print_ladder_pattern(n):
	for ii in range(1, n + 1):
		print(ii * "*")


print_ladder_pattern(5)

#     *
#    **
#   ***
#  ****
# *****
def print_ladder_pattern_rotated_180(n):
	for ii in range(1, n+1):
		print((n - ii) * " " + ii * "*")

print_ladder_pattern_rotated_180(5)

# * * * * *
# * * * *
# * * *
# * *
# *

def print_ladder_upside_down(n):
	for ii in range(n, 0, -1):
		print("*" * ii)
		
print_ladder_upside_down(5)

# 1
# 22
# 333
# 4444
# 55555
def print_numbers_same(n):
	for ii in range(1,n+1):
		print(str(ii)*ii)
		
print_numbers_same(5)

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6
# 7 7 7 7 7 7 7
# 8 8 8 8 8 8 8 8
# 9 9 9 9 9 9 9 9 9

def print_numbers_same_with_spaces(n):
	for num in range(n):
		for ii in range(num):
			print(num, end=" ")
		print()
	
print_numbers_same_with_spaces(10)