'''
On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', 
black pawns 'p', and empty squares '.'.

When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then 
moves in that direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is 
blocked by a white bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's 
turn. The number of available captures for the white rook is the number of pawns that the rook is attacking.

Return the number of available captures for the white rook.
'''

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rookx, rooky = -1, -1
        for i in range(len(board)):
            if "R" in board[i]:
                rookx, rooky = i, board[i].index("R")
                break
        count = 0
        if rookx > 0:
            for i in range(rookx - 1, -1, -1):
                if board[i][rooky] == "B": break
                elif board[i][rooky] == "p":
                    count += 1
                    break
        if rookx < len(board) - 1:
            for i in range(rookx + 1, len(board)):
                if board[i][rooky] == "B": break
                elif board[i][rooky] == "p":
                    count += 1
                    break
        if rooky > 0:
            for i in range(rooky - 1, -1, -1):
                if board[rookx][i] == "B": break
                elif board[rookx][i] == "p":
                    count += 1
                    break
        if rooky < len(board) - 1:
            for i in range(rooky + 1, len(board)):
                if board[rookx][i] == "B": break
                elif board[rookx][i] == "p":
                    count += 1
                    break
        return count
