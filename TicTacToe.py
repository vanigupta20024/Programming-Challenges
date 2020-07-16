# GHC Codepath SE101 
# Sandbox - 3 BASIC

# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY board as parameter.
# The function will analyze the board and determine 
# the winner. Return 1 if player 1 wins, return 2 if
# player 2 wins, or return -1 if there was no winner.

def ticTacToe(a):
    # rows
    for i in range(len(a)):
        if a[i][0] == a[i][1] == a[i][2]:
            return a[i][0]
    # columns
    for i in range(len(a)):
        if a[0][i] == a[1][i] == a[2][i]:
            return a[0][i]

    # main diagnomal
    if a[0][0] == a[1][1] == a[2][2]:
        return a[0][0]

    # other diagonal
    if a[2][0] == a[1][1] == a[0][2]:
        return a[2][0]
    return -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    board_rows = int(input().strip())
    board_columns = int(input().strip())

    board = []

    for _ in range(board_rows):
        board.append(list(map(int, input().rstrip().split())))

    result = ticTacToe(board)

    fptr.write(str(result) + '\n')

    fptr.close()
