# def addition(x,y):
#     print('x',x,type(x),'y',y,type(y))
#     return x+y


# total=addition(5,'6')
# # total='lal' + ' tiwari'

# print(total)

game = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def game_board(player=0, row=0, column=0,just_display=False):
    print("   0  1  2")
    if not just_display:
        game[row][column] = player
    for count, row in enumerate(game):
        print(count, row)

# game_board()
game_board(just_display=True)
game_board(2,0,0)
game_board(2,1,0)
game_board(column=0,row=1,player=2)

