tictac = {
    "TL" : " ", "TM" : " ", "TR" : " ",
    "ML" : " ", "MM" : " ", "MR" : " ",
    "BL" : " ", "BM" : " ", "BR" : " "
}
def print_board(tictac):
    print(tictac["TL"] + "  | " + tictac["TM"] + " | " + tictac["TR"] + "\n--- --- ---")
    print(tictac["ML"] + "  | " + tictac["MM"] + " | " + tictac["MR"] + "\n--- --- ---")
    print(tictac["BL"] + "  | " + tictac["BM"] + " | " + tictac["BR"])
    
print("The board looks like:\n")
print(" \
TL | TM | TR \n \
--- ---- ---\n \
ML | MM | MR\n \
--- ---- ---\n \
BL | BM | BR")

def check(tictac):
    winner = ""
    
    if (tictac["TL"] == tictac["TM"]) and (tictac["TL"] == tictac["TR"]) and tictac["TL"] != " ":
        return tictac["TL"]
    if (tictac["ML"] == tictac["MM"]) and (tictac["MR"] == tictac["MM"]) and tictac["MM"] != " ":
        return tictac["ML"]
    if (tictac["BL"] == tictac["BM"]) and (tictac["BR"] == tictac["BL"]) and tictac["BL"] != " ":
        return tictac["BL"]
    if (tictac["TL"] == tictac["ML"]) and (tictac["BL"] == tictac["ML"]) and tictac["ML"] != " ":
        return tictac["TL"]
    if (tictac["TM"] == tictac["MM"]) and (tictac["BM"] == tictac["TM"]) and tictac["TM"] != " ":
        return tictac["TM"]
    if (tictac["TR"] == tictac["MR"]) and (tictac["BR"] == tictac["TR"]) and tictac["TR"] != " ":
        return tictac["TR"]
    if (tictac["TL"] == tictac["MM"]) and (tictac["BR"] == tictac["MM"]) and tictac["TL"] != " ":
        return tictac["TL"]
    if (tictac["TR"] == tictac["MM"]) and (tictac["BL"] == tictac["TR"]) and tictac["TR"] != " ":
        return tictac["TR"]
    return None

turn = 'X'
count = 0
while count < len(tictac):
    print("Enter position to place {}.".format(turn))
    pos = input()
    
    if pos not in tictac.keys():
        print("Enter a valid place!")
        continue
    if tictac[pos] != " ":
        print("Place already filled! Choose another position.")
        continue
    
    tictac[pos] = turn
    count += 1
    
    if turn == "X": turn = "O"
    else: turn = "X"
    
    win = check(tictac)
    if win:
        print_board(tictac)
        print(win, "won the match!!")
        break
    print_board(tictac)
    
if count == len(tictac):
    if check(tictac) is None:
        print("Oops! It's a tie!")
