#Horizontal Winner

game=[[ 1, 0, 0],
      [ 3, 3, 3],
      [ 0, 1, 0],]

def win(current_game):
    for row in current_game:
        print(row)
        if row.count(row[0]) == len(row) :
             print("winner")

win(game)

# Vertical Winner

game=[[ 0, 0, 3],
      [ 3, 0, 3],
      [ 0, 0, 3],]

for col in range(len(game)):
    check = []
    for row in game:
        check.append(row[col])
    if check.count(check[0]) == len(game) and check[0] !=0 :
       print("winner!")
'''If the condition is met, which means that all elements in the column are the same
  and not equal to zero, it prints "winner!" to indicate that a player has won the game ''' 
  
#diagonal Winner

game=[[ 0, 0, 2],
      [ 3, 2, 3],
      [ 2, 0, 3],]

diags = []
for col,row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])
print(diags)
diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])
print(diags)

# Just practice
'''game=[[ 1, 0, 2],
      [ 3, 1, 3],
      [ 2, 0, 1],]
if game[0][0] == game[1][1] == game[2][2]:
    print("Winner!")

if game[2][0] == game[1][1] == game[0][2]:
    print("Winner!")'''