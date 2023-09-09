# How to handle errors

game= [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],]

def game_board(game_map,player=0,row=0,column=0,just_display=False):
    try:
         print("   0  1  2")
         if not just_display:
            game_map[row][column] =player                      # Here In use try except block to handle errors
         for count,row in enumerate(game_map):
            print(count,row)
         return game_map
    except IndexError as e:
        print("Error:Make sure you input row/column 0 1 OR 2?",e)
    except Exception as e:
        print("Something went very wrong",e)        



game = game_board(game, just_display=True)
game = game_board(game_board,player=1, row=3, column=1)      # here i given row=3 then I'will get error index out of range