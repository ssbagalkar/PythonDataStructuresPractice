# Implement your function below.
## My solution(not very effective)
# def is_one_away(s1, s2):
	# same = 0

	# if len(s1) != len(s2):
		# if len(s1) < len(s2):
			# return (is_one_away(s2, s1))

		# ii = 0
		# jj = 0
		# no_change = 0
		# if len(s1)-len(s2) == 1:
			# while ii < len(s1) and jj < len(s2):
				# if s1[ii] == s2[jj]:
						# same+=1
						# ii+=1
						# jj+=1
				# else:
						# no_change=1
						# ii+=1
	
			# if no_change:
					# if same >= len(s1)-1:
							# return True
			# else:
					# return True


	# else:
			# for ii in range(len(s1)):
					# if s1[ii] == s2[ii]:
							# same += 1
			# if same >= len(s1) - 1:
					# return True
			# else:
					# return False

					
## Solution from lesson

def is_one_away_same_length(s1,s2):
	count_diff = 0
	
	for ii in range(len(s1)):
		if s1[ii] != s2[ii]:
			count_diff+=1
			
		if count_diff > 1:
			return False
	return True
	
def is_one_away_diff_length(s1,s2):
	count_diff = 0
	ii=0
	
	while ii<len(s2):
		if s1[ii+count_diff] == s2[ii]:
			ii+=1
		else:
			count_diff+=1
			
			if count_diff>1:
				return False
				
	return True
	
def is_one_away(s1,s2):
	if len(s1)-len(s2)>= 2 or len(s2) - len(s1) >= 2:
		return False
		
	elif (len(s1) == len(s2)):
		return is_one_away_same_length(s1,s2)
	
	elif(len(s1)>len(s2)):
		return is_one_away_diff_length(s1,s2)
		
	else:
		return is_one_away_diff_length(s2,s1)
 





# NOTE: The following input values will be used for testing your solution.
print(is_one_away("abcde", "abcd"))  # should return True
print(is_one_away("abde", "abcde"))  # should return True
print(is_one_away("a", "a"))  # should return True
print(is_one_away("abcdef", "abqdef"))  # should return True
print(is_one_away("abcdef", "abccef"))  # should return True
print(is_one_away("abcdef", "abcde"))  # should return True
print(is_one_away("aaa", "abc"))  # should return False
print(is_one_away("abcde", "abc"))  # should return False
print(is_one_away("abc", "abcde"))  # should return False
print(is_one_away("abc", "bcc"))  # should return False