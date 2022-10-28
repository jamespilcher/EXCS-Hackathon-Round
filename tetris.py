# DO NOT MODIFY THIS FILE

import random
from tetris_ai import move_piece

class Board:

    def __init__(self):
        self.w = 10
        self.h = 20
        self.board = [[" "]*self.w for i in range(self.h)]
        self.piece = Piece()
        self.score = 0

    def __str__(self):
        s = f"Score : {self.score}\n"
        s += "="*23 + "\n"
        for i in range(self.h):
            l = "| "
            for j in range(self.w):
                if [j,i] in self.piece.shape:
                    l += self.piece.c
                else:
                    l += self.board[i][j]
                l += " "
            s += l + "|\n" 
        s += "="*23 + "\n"
        return s

    def tick(self):
        alive = True
        while alive:
            print(self)
            display_b = DisplayBoard(self.board)
            display_p = DisplayPiece(self.piece.type, self.piece.orientation, self.piece.shape)
            instruction = move_piece(display_b, display_p)
            dx = 0
            down = False
            if instruction.lower() == "r":
                dx = 1
            elif instruction.lower() == "l":
                dx = -1
            elif instruction.lower() == "d":
                down = True
            invalid = False
            undo_move = False
            while not invalid:
                if instruction.lower() == "x":
                    rotate = True
                    new_orientation = (self.piece.orientation+1) % 4
                    for i in range(4):
                        r = self.piece.rotations[new_orientation][i]
                        new_x = self.piece.shape[i][0] + r[0]
                        new_y = self.piece.shape[i][1] + r[1]
                        if new_x < 0 or new_x > 9 or new_y < 0 or new_y > 19:
                            rotate = False
                        elif self.board[new_y][new_x] != " ":
                            rotate = False
                    
                    if rotate:
                        self.piece.orientation = new_orientation
                        for i in range(4):
                            r = self.piece.rotations[new_orientation][i]
                            self.piece.shape[i][0] += r[0]
                            self.piece.shape[i][1] += r[1]

                for i in range(4):
                    x,y = self.piece.shape[i]


                    if y == 19 or self.board[y+1][x] != " ":
                        invalid = True
                        undo_move = True
                    elif x+dx == 10 or x+dx == -1 or self.board[y+1][x+dx] != " ":
                        undo_move = True
                    self.piece.shape[i][1] += 1
                    self.piece.shape[i][0] += dx
                if not down:
                    break

            if undo_move:
                for i in range(4):
                    self.piece.shape[i][0] -= dx

            if invalid:
                for i in range(4):
                    x,y = self.piece.shape[i]
                    self.board[y-1][x] = self.piece.c
                self.piece = Piece()
                self.score += 20

                in_a_row = 0
                y = 0
                while y < 20:
                    if self.board[y].count(" ") == 0:
                        in_a_row += 1
                        self.board[y] = [" "]*10
                        if in_a_row <= 4:
                            self.score += [0,40,100,300,1200][in_a_row]
                        else:
                            self.score += 1200
                        for y2 in range(y, 0, -1):
                            self.board[y2] = self.board[y2-1][:]
                        y -= 1
                    else:
                        in_a_row = 0
                    y += 1

                for i in range(4):
                    x,y = self.piece.shape[i]
                    if self.board[y][x] != " ":
                        print("-"*23)
                        print(f"Score: {self.score}")
                        alive = False
                        break


class Piece:

    def __init__(self):
        self.type = random.choice(["I","O","T","J","L","S","Z"])
        self.c = random.choice(["%","X","&","$","@"])
        self.shape = {
            "L" : [[4,0], [4,1], [4,2], [5,2]],
            "Z" : [[4,0], [5,0], [5,1], [6,1]],
            "J" : [[5,0], [5,1], [5,2], [4,2]],
            "S" : [[4,1], [5,0], [5,1], [6,0]],
            "T" : [[4,0], [5,0], [5,1], [6,0]],
            "O" : [[4,0], [4,1], [5,0], [5,1]],
            "I" : [[4,0], [4,1], [4,2], [4,3]]
        }[self.type][:]
        self.orientation = 0

        self.rotations = {
            "L" : [[[1,-1], [0,0], [-1,1], [0,2]], [[1,1], [0,0], [-1,-1], [-2,0]], [[-1,1], [0,0], [1,-1], [0,-2]], [[-1,-1], [0,0], [1,1], [2,0]]],
            "Z" : [[[0,-2], [1,-1], [0,0], [1,1]], [[2,0], [1,1], [0,0], [-1,1]], [[0,2], [-1,1], [0,0], [-1,-1]], [[-2,0], [-1,-1], [0,0], [1,-1]]],
            "J" : [[[1,-1], [0,0], [-1,1], [-2,0]], [[1,1], [0,0], [-1,-1], [0,-2]], [[-1,1], [0,0], [1,-1], [2,0]], [[-1,-1], [0,0], [1,1], [0,2]]],
            "S" : [[[-1,-1], [1,-1], [0,0], [2,0]], [[1,-1], [1,1], [0,0], [0,2]], [[1,1], [-1,1], [0,0], [-2,0]], [[-1,1], [-1,-1], [0,0], [0,-2]]],
            "T" : [[[-1,-1], [0,0], [-1,1], [1,1]], [[1,-1], [0,0], [-1,-1], [-1,1]], [[1,1], [0,0], [1,-1], [-1,-1]], [[-1,1], [0,0], [1,1], [1,-1]]],
            "O" : [[[0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0]]],
            "I" : [[[2,-1], [1,0], [0,1], [-1,2]], [[1,2], [0,1], [-1,0], [-2,-1]], [[-2,1], [-1,0], [0,-1], [1,-2]], [[-1,-2], [0,-1], [1,0], [2,1]]]
        }[self.type][:]

class DisplayBoard():
    def __init__(self, tiles):
        self.tiles = []
        for x in tiles:
            self.tiles.append(x[:])
        self.width = 10
        self.height = 20

class DisplayPiece():
    def __init__(self, name, rotation, tiles):
        self.name = name
        self.rotation = rotation
        self.tiles = []
        for x in tiles:
            self.tiles.append(x[:])

if __name__ == "__main__":
    b = Board()
    b.tick()