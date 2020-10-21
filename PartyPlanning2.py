# The bakery might have different desserts available on different days. Update your function so that 
# you can accept a dictionary of items available and the number of guests they serve. 
# Our original function would have taken in:
# menu = {
#   "cakes": 25,
#   "pies": 8,
#   "cupcakes": 1
# }
## an updated menu might take in:
menu = {
  "cakes": 25,
  "pies": 8,
  "fudge_block": 5,
  "cupcakes": 1
}

def create_order_update(party_size, menu):
  rev_menu = {v:k for k,v in menu.items()}
  menu_list = sorted(rev_menu.keys(), reverse = True)
  i = 0
  answers = {}
  while party_size > 0:
    if party_size >= menu_list[i]:
      party_size -= menu_list[i]
      if rev_menu[menu_list[i]] in answers.keys():
        answers[rev_menu[menu_list[i]]] += 1
      else:
        answers[rev_menu[menu_list[i]]] = 1
    else:
      i += 1
  return answers

print(create_order_update(55, menu))
