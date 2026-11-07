board = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]

rows = len(board)
cols = len(board[0])

for row in range(rows):
    for col in range(cols):
        print(board[row][col])

#move between adjacent cells
# Up
board[row - 1][col]

# Down
board[row + 1][col]

# Left
board[row][col - 1]

# Right
board[row][col + 1]
# but need to chck if it doesntfall outisde the range

ORRRR

directions = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]

row, col = 1, 1  # Start at centre ("e")

for dr, dc in directions:
    new_row = row + dr
    new_col = col + dc

    if 0 <= new_row < rows and 0 <= new_col < cols:
        print(board[new_row][new_col])