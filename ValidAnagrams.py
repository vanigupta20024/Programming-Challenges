

# Given two strings s and t, write a function to # determine if s is an anagram of t. 
# len(s) = N = len(t)
def simple_valid_anagrams(s, t):
  if len(s) != len(t): # 2 * O(1)
    return False # O(1)
  return sorted(s) == sorted(t) # 2 * O(N*Log(N))
# Runtime: O(N*Log(N))
# Storage: O(2*N)

#print(simple_valid_anagrams('listen', 'silent'))
#print(simple_valid_anagrams('bob', 'bot'))

# Check length of both strings 
# Loop through s, create hashmap of characters 
# Loop through t, create hashmap of characters 
# Compare keys and values of hashmaps 

# N: len(s)
def valid_anagrams(s, t):
  if len(s) != len(t): # 2 * O(1)
    return False # O(1)
  s_dict = {} 
  for c in s: # O(N)
    if c in s_dict: 
      s_dict[c] += 1 
    else:
      s_dict[c] = 1 
  t_dict = {}
  for c in t: # O(N)
    if c in t_dict: 
      t_dict[c] += 1 
    else:
      t_dict[c] = 1 
  for k, v in s_dict.items(): # O(N)
    if k not in t_dict: # O(1)
      return False 
    if v != t_dict[k]: # O(1)
      return False 
  return True 
# Runtime: O(2*N) + O(N) -> O(N)
# Storage: O(2*N) -> O(N)

print(valid_anagrams('listen', 'silent'))
print(valid_anagrams('bob', 'bot'))
print(valid_anagrams('listet', 'silent'))
