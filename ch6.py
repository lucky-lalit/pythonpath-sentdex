game = [[0,0,0],
        [0,0,0],
        [0,0,0]]


def game_board():
    print("   0  1  2")
    for count,row in enumerate(game):
        print(count,row)
    return 100

print('Hello World','Hello Universe')
print('this is game_board',game_board)
print('(this gameboard)',game_board())
print(None)
print(type(game_board))
print('this is a',type(game_board()))
print('this is b',type(100))
print('this is c',int)
# x=game_board
# y=x
# game_board()

# game[0][1] = 2
# x()
# game[2][2] = 1
# y()
# # game[0][1] = 1
# # game_board()
