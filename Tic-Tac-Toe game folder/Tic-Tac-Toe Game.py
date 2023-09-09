import itertools



def win(current_game):
    
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    # Horizonatal Winner
    for row in game:
            print(row)
            if all_same(row):
                print(f"player {row[0]} is the Winner horizontally!")
                return True

    #Diagonal Winner
    diags = []
    for col,row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"player {diags[0]} is the Winner diagonally(/)!")
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"player {diags[0]} is the Winner diagonally(\\)!")
        return True

    # Vertical Winner
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"player {check[0]} is the Winner vertically!(|)")
            return True
    return False


def game_board(game_map,player=0,row=0,column=0,just_display=False):
    try:
         if game_map[row][column] !=0:
             print("This position is occupado! Choose another!")
             return  game_map, False
         print("  "+"  ".join([str(i) for i in range(len(game_map))]))
         if not just_display:
            game_map[row][column] = player                      # Here I use try except block to handle errors
         for count,row in enumerate(game_map):
            print(count, row)
         return game_map, True 
    
    except IndexError as e:
        print("Error:Make sure you input row/column 0 1 OR 2?",e)
        return game_map, False
    
    except Exception as e:
        print("Something went very wrong",e) 
        return game_map, False       

play = True
players = [1, 2]
while play:
    game_size = int(input("What size game of tic tac toe?"))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game,just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"current_player:{current_player}")
        played = False

        while not played:
            column_choice = int(input("what column do you want to play? (0, 1, 2):"))
            row_choice = int(input("what row do you want to play? (0, 1, 2):"))
            game, played = game_board(game, current_player, row_choice, column_choice)
        

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n)")
            if again.lower()=="y":
                print("restarting")
            elif again.lower()=="n":
                print("byeeeee")
            else:
                print("Not a valid answer, so... c u l8r aligator")
                play = False




#game = game_board(game, just_display=True)
#game = game_board(game_board,player=1, row=3, column=1)      # here i given row=3 then I'will get error index out of range


'''game_size = int(input("What size game of tic tac toe?"))
game = [[0 for i in range(game_size)] for i in range(game_size)]'''

'''game= [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
    game_won = False'''













'''import itertools

def win(current_game):
    
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    
    # Horizontal Winner
    for row in current_game:
        if all_same(row):
            print(f"Player {row[0]} is the Winner horizontally!")
            return True

    # Diagonal Winner
    diags = []
    for col, row in enumerate(reversed(range(len(current_game)))):
        diags.append(current_game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the Winner diagonally(/)!")
        return True

    diags = []
    for ix in range(len(current_game)):
        diags.append(current_game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the Winner diagonally(\\)!")
        return True

    # Vertical Winner
    for col in range(len(current_game)):
        check = []
        for row in current_game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the Winner vertically!(|)")
            return True
    return False

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupado! Choose another!")
            return game_map, False
        
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
    
    except IndexError as e:
        print("Error: Make sure you input row/column 0, 1, or 2?", e)
        return game_map, False
    
    except Exception as e:
        print("Something went very wrong", e)
        return game_map, False

play = True
players = [1, 2]

while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle(players)

    while not game_won:
        current_player = next(player_choice)
        print(f"Current player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2):"))
            row_choice = int(input("What row do you want to play? (0, 1, 2):"))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over. Would you like to play again? (y/n)")
            if again.lower() == "y":
                print("Restarting")
            elif again.lower() == "n":
                print("Goodbye!")
                play = False
            else:
                print("Not a valid answer, so... see you later, alligator")
                play = False '''
