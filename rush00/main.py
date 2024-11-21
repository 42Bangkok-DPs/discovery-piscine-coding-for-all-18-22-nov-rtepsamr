#!/usr/bin/env python3
def find_king(board):
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 'K':
                return (r, c)
    raise ValueError("King not found on the board!")
def is_in_bounds(r, c, rows, cols):
    
    return 0 <= r < rows and 0 <= c < cols

def is_king_under_threat(board, king_pos): 
    rows, cols = len(board), len(board[0])
    moves = {
        'P': [(-1, -1), (-1, 1)],  
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],  
        'R': [(-1, 0), (1, 0), (0, -1), (0, 1)], 
        'Q': [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)], 
    }
    king_r, king_c = king_pos

    for r in range(rows):
        for c in range(cols):
            piece = board[r][c]
            if piece == '.' or piece == 'K':
                continue  
            if piece == 'P':
                for dr, dc in moves['P']:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) == (king_r, king_c):
                        return True            
            if piece in ['B', 'R', 'Q']:
                for dr, dc in moves[piece]:
                    nr, nc = r, c
                    while True:
                        nr += dr
                        nc += dc
                        if not is_in_bounds(nr, nc, rows, cols):  
                            break
                        if (nr, nc) == (king_r, king_c):  
                            return True
                        if board[nr][nc] != '.':  
                            break
    return False
def main():
    board = [
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', 'P', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', 'Q', 'K', '.'],]
    king_pos = find_king(board)
    if is_king_under_threat(board, king_pos):
        print("Success")
    else:
        print("Fail")


if __name__ == "__main__":
    main()