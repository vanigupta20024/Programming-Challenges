'''
On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', 
black pawns 'p', and empty squares '.'.

When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then 
moves in that direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is 
blocked by a white bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's 
turn. The number of available captures for the white rook is the number of pawns that the rook is attacking.

Return the number of available captures for the white rook.
'''

# Recursive solution
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        def find(rx, ry, direction, count):
            if rx == 8 or ry == 8 or rx == -1 or ry == -1: return count
            if board[rx][ry] == "B": return 0
            if board[rx][ry] == "p": return count + 1
            if direction == "L": return find(rx, ry - 1, "L", count)
            elif direction == "R": return find(rx, ry + 1, "R", count)
            elif direction == "U": return find(rx - 1, ry, "U", count)
            else: return find(rx + 1, ry, "D", count)
            
        rookx = rooky = -1
        for i in range(len(board)):
            if "R" in board[i]:
                rookx, rooky = i, board[i].index("R")
                break
                
        return find(rookx, rooky, "L", 0) + find(rookx, rooky, "R", 0) + find(rookx, rooky, "U", 0) + find(rookx, rooky, "D", 0)
    
# Iterative Solution

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
