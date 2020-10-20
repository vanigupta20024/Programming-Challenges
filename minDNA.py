## Write a new function that finds the shortest sequence that contains all proteins in no particular order and returns it (CATG or GATC, any combination is valid)

def shortest_diverse_sequence(dna):
  prot = "ATCG"
  start = 0
  end = 4
  while end < len(dna):
    if set(dna[start:end]) == set(prot):
      return dna[start:end]
    else:
      start += 1
      end += 1

print(shortest_diverse_sequence("GAGTCCGTTTTTTTA"))
