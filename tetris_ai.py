# Board class
# ====================
# board.tiles = An array containing rows of the board, which are arrays of characters. (board.tiles[5][2] = 6th row, 3rd column)
# board.width = 10
# board.height = 20


# Piece class
# =====================
# piece.name = One of 'I','O','T','J','L','S', or 'Z', indicating the tetromino name.
# piece.rotation = A value from 0 - 3, indicating the number of clockwise rotations.
# piece.tiles = An array of length 4 containing [x,y] pairs with the coordinates of each tile of the piece.

#    piece.name    |        I        |        O        |        T        |        J        |        L        |        S        |        Z        |
# -----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
#                  |       O         |       O O       |         O       |         O       |       O         |         O O     |       O O       |
#  Starting Shape  |       O         |       O O       |       O O O     |         O       |       O         |       O O       |         O O     |
#                  |       O         |                 |                 |       O O       |       O O       |                 |                 |
#                  |       O         |                 |                 |                 |                 |                 |                 |
# -----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|

import time

def move_piece(board, piece):
    """
    Controls the movement of a piece.

    Arguments:
     - board: An instance of the Board class (detailed above)
     - piece: An instance of the Piece class (detailed above)
    
    Returns
     - 'R' for right,
     - 'L' for left,
     - 'D' for down,
     - 'X' for rotate,
     - ' ' for neutral.
    """

    # EXAMPLE
    if piece.name == "L" and piece.rotation != 3:
        move = "X"
    elif piece.name == "J" and piece.rotation != 1:
        move = "X"
    elif board.tiles[19][0] != " ": #20th row, 1st column (bottom left corner)
        move = "R"
    else:
        move = "L"   
    # EXAMPLE

    # Game timer (tick), can be changed for testing. The piece moves every _ seconds.
    time.sleep(0.5)

    return move