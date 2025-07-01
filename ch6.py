game = [[0,0,0],
        [0,0,0],
        [0,0,0]]


def game_board():
    print("   0  1  2")
    for count,row in enumerate(game):
        print(count,row)
    return 100

print(game_board)
print(game_board())
print(None)
print(type(game_board))
print(type(game_board()))
print(type(100))
print(int)
# x=game_board
# y=x
# game_board()

# game[0][1] = 2
# x()
# game[2][2] = 1
# y()
# # game[0][1] = 1
# # game_board()
