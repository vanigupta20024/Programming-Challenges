## You are a DNA analyst. You're looking for long unbroken sequences of proteins for some esoteric reason that you don't have time to explain right now.
# You have a file of DNA sequences that looks like this:
## the longest continuous sequence of proteins is "TTTTTTT" which is 7 elements long.

def longest_sequence(dna):
  slow = 0
  fast = 0
  mx = 0
  while fast < len(dna):
    if dna[slow] == dna[fast]:
      fast += 1
      diff = fast - slow
      if mx < diff: mx = diff 
    else:
      slow = fast
      fast += 1
  return mx

print(longest_sequence("GATAGCCGATTTTTTTA"))
