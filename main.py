import itertools

def win(curr_game):
    def all_same(l):
        if row.count(row[0]) == len(game) and row[0] != 0:
            return True
        else:
            return False


#horizontally deciding the winner            
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally(---)")
            return True

    #diagonally
    diagonals = []
    for row in range(len(game)):
        diagonals.append(game[row][row])#for 00,11,22...
    if all_same(diags):
        print(f"Player {diagonals[0]} is the winner diagonally(\\)")
        return True
      
    diagonals = []
    for row,col in enumerate(reversed(range(len(game)))):
        diagonals.append(game[row][col]) #for 02,11,20...
    if all_same(diags):
        print(f"Player {diagonals[0]} is the winner diagonally(/)")
        return True
  
    #vertically deciding the winner
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically(|)")
            return True        

#playing the game
def game_board(game_map, player=0, row=0, column=0, just_display=False):
            try:
                if game_map[row][column] != 0:
                    print ("Oops! Position is already occupied, try something else")
                    return game_map,False
                print ("   " + "  ".join([str(i) for i in range(len(game_map))])) 
                if not just_display:
                    game_map[row][column] = player
                for count,row in enumerate(game_map):
                    print(count,row)
                return game_map, False  

            except IndexError as e:
                print ("Make sure you give row/column as only 0/1/2:", e)
                return game_map,False
            except Exception as e:
                print ("Something is very very wrong. Please check:", e)
                return game_map,False


play = True
players = [1,2]
while play:
    game_size = int(input("what size of tic tac toe do you wanna play: "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won=False
    game, _ =game_board(game, just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        curr_player = next(player_choice)
        print(f"Current player playing is {curr_player}")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? 0 or 1 or 2 :"))
            row_choice = int(input("What row do you want to play? 0 or 1 or 2 : "))
            game, played=game_board(game,curr_player,row_choice,column_choice)


        if win(game):
            game_won = True
            again = input("Game is over. would you like to play again (y/n)")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("Okk byee")
                play =  False  
            else:
                print("Not a valid answer, so okay byee")
                play = False
                  

