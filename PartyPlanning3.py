## The bakery wants to be able to sell it's in-stock orders first. Take in a second dictionary and distinguish between the in-stock items before ordering new items. Return a dictionary of in-stock ("stock") vs made-to-order ("custom") items.
## Input:
# large_party_size = 200
# menu = {"cakes": 25, "pies": 8, "cupcakes": 1 }
# in_stock = {"cakes": 1, "pies": 4, "cupcakes": 100 }
## output format:
# order = {"stock_cake": 1, "stock_pies": 4, "stock_cupcakes": 100, "custom_cake": 1, "custom_pies": 2, "custom_cupcakes": 2 }
def getname(dessert, is_stock):
  if is_stock: return "stock_" + dessert
  return "custom_" + dessert

def order_with_stock(party_size, in_stock, menu):
  answer = {}
  rev_menu = {v:k for k,v in menu.items()}
  dessert = sorted(rev_menu.keys(), reverse = True)
  i = 0
  while party_size > 0 and in_stock:
    if party_size >= dessert[i] and rev_menu[dessert[i]] in in_stock:
      party_size -= dessert[i]
      if getname(rev_menu[dessert[i]], True) in answer.keys():
        answer[getname(rev_menu[dessert[i]], True)] += 1
      else:
        answer[getname(rev_menu[dessert[i]], True)] = 1
      in_stock[rev_menu[dessert[i]]] -= 1
      if in_stock[rev_menu[dessert[i]]] == 0:
        in_stock.pop(rev_menu[dessert[i]])
    else:
      i += 1
  i = 0
  while party_size > 0:
    if party_size >= dessert[i]:
      party_size -= dessert[i]
      if getname(rev_menu[dessert[i]], False) in answer.keys():
        answer[getname(rev_menu[dessert[i]], False)] += 1
      else:
        answer[getname(rev_menu[dessert[i]], False)] = 1
    else:
      i += 1
  print(answer)

order_with_stock(200, in_stock, menu)
