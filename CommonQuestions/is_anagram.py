def makeAnagram(a, b):
  if len(b) > len(a):
    return makeAnagram(b,a)
  
  changes = 0
    
  a_dict = {}
  b_dict = {}
  
  for char in a:
    if char not in a_dict:
      a_dict[char]=1
    else:
      a_dict[char]+=1
  
  for char in b:
    if char not in b_dict:
      b_dict[char]=1
    else:
      b_dict[char]+=1
  
  # Find all uncommon  and common elements and their counts
  uncommon_chars = set(a_dict)^set(b_dict)
  common_chars = set(a_dict)&set(b_dict)
  
  if uncommon_chars:
    for char in uncommon_chars:
      if char in a_dict:
        # Get count of the char
        changes += a_dict[char]
      else:
        changes += b_dict[char]
        
  if common_chars:
    for char in common_chars:
      if a_dict[char] != b_dict[char]:
        changes += abs(a_dict[char]-b_dict[char])
        
  return changes