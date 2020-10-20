## Write another function that, given two strands of DNA as strings finds the most common pair of proteins- Protein pairs that share an index:

right_strand = "GATACATAC"
left_strand  = "TTCTGDACG"
## Most common pair: T and A - found on index 1, 3, 6
def most_common_pair(right_strand,left_strand):
  com = {}
  for i in range(len(right_strand)):
    s = tuple(set((right_strand[i],left_strand[i])))
    if s in com.keys() and len(s) == 2:
      com[s] += 1
    else:
      com[s] = 1
  strand = tuple()
  mx = 0
  for k, v in com.items():
    if v > mx:
      strand = k
      mx = v
  return strand

print(most_common_pair(right_strand,left_strand))
