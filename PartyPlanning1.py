# You're running a catering business that serves desserts. Customers call in and tell you a party size, and you provide enough dessert for everyone to have a piece.
# Cakes serve 25 guests.
# Pies serve 8 guests.
# Cupcakes serve 1 guest.
# The more people a dessert serves, the less it costs to make, so we want you to optimize for serving the biggest desserts first.

# Write a function that, given a party size, will output a dictionary with each dessert and the number to provide like this:
# input:
# party_size = 60
# # output:
# order = {
#   "cakes": 2,
#   "pies": 1,
#   "cupcakes": 2
# } 

def create_order(party_size):
  desserts = {
    "cakes": 25,
    "pies": 8,
    "cupcakes": 1
  }
  rev_des = {v:k for k,v in desserts.items()}
  answer = {}
  dessert_list = sorted(rev_des.keys(), reverse = True)
  i = 0
  while party_size > 0:
    if party_size >= dessert_list[i]:
      party_size -= dessert_list[i]
      if rev_des[dessert_list[i]] in answer.keys():
        answer[rev_des[dessert_list[i]]] += 1
      else:
        answer[rev_des[dessert_list[i]]] = 1
    else:
      i += 1
  return answer

print(create_order(108))
