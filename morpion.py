
def length(list):             # Little function to return length of a list (or a string)
    c = 0
    for i in list:
        c += 1
    return c

def list_to_formated_string(LIST):      # convert a list to a string
    string = ''                         # It will be use for printing scores
    fstring = ''                        # The list contains a username in each odd number position of the list
    c = 0                               # And a number of victory (as a string) in each even number position
    for i in LIST:
        string += i
    for j in range(0,length(string)):
        if string[j] != '\n':           # If actual char isn't '\n'
            fstring += string[j]        # add it
        else:                           # else, actual char is '\n'
            c += 1                      # let's increase "c"
            if c%2 == 0:                # if c is an even number (we are at the number of victory)
                fstring += ' victoires\n\n' # add ' victoires\n\n' instead of '\n'
            else:                       # else, c is an odd number (we are at the username)
                fstring += ' : '        # add ' : '

    return fstring                      # At the end, we return the new string (it will be like : 'username : x victoires\n\n')

def list_to_string(LIST,add,x):   #function to convert a list to a string (each value of the list is concatenated into the string)
    string = ''                   # You can append a new char (or string) after x elements
    for i in range(0,length(LIST),x):       # For example, you can add a '\n' at each 2 elements of the list
        string += LIST[i]+add               # like that : list_to_string(LIST,'\n',2)
    return string

######################################################################################

print ('')

replay = 'o'                    # Variable to handle choice of users at the end of a game, does user want to replay (o) or quit (n or anything else)
while replay == 'o':            # Loop for replay

    menu_choice = 0              #Variable to store choice of user (Does he want to play, see scores, erase scores or quit)

    player1 = ''                   #Variables to store player's usernames
    player2 = ''
    last_player = 'p2'              # This one will store who played last turn

    player1_played_line = [0]       # We'll use 4 lists to store players move :
    player1_played_column = [0]     # 2 for each player, one will contain the number of the line played
    player2_played_line = [0]       # The other will contain the number of the column played
    player2_played_column = [0]     # For example, if player1 played '1 2' at turn 1 : player1_played_line[1] = 1
                                    # and player1_played_column[1] = 2

    turn = 1                        # Variable to store current turn of the game (beginning at turn 1)

    victory = False                 # When a player will win a game, this variable will be set to "True"
    egalite = False                 # If any player win after turn 9, egalite will be set to "True"

    winner = ''                     # To store the username of the winner
    winner_is_in_score = False      # This variable will be use to check if winner of the last game is already in the score file or not

    line1 = ['- ','- ','-']         # 3 lists to store each line of the grid
    line2 = ['- ','- ','-']
    line3 = ['- ','- ','-']

    #############################

    # Now that our variables are set , let's go for the core :

    # Let's ask the user for his choice in the main menu
    menu_choice = int(input ("Bonjour, souhaites-tu :\n1 Jouer\n2 Voir les scores\n3 Réinitialiser les scores\n4 Quitter\n? > "))
    print ('')

    if menu_choice == 1:                          #If users want to play

        player1 = input ("Username 1 , Croix : ")   #Ask for their usernames
        player2 = input ("Username 2, Rond : ")
        print ('')

        for i in range(3):                         # Print a blank grid at the beginning ( with only '-')
            for j in range(3):
                if j < 2:
                    print("- " , end = '')
                else:
                    print("-")
        print ('')

        ########################################################################

        while not victory:                      # Go for the game, this loop will ask players to play till
                                                # someone win.

            # If last_player = p2, then player 1 must play now
            if last_player == 'p2':
                x , y = [int(x) for x in input("%s joue (ligne puis colonne) : "  %(player1)).split()]  #Ask player1 for line and column
                player1_played_line.append(x)                    # Add the line he played in the dedicated list
                player1_played_column.append(y)                  # Add the column he played in the dedicated list
                player2_played_line.append(0)                    # Player2's lists must be appended too, cause we need them to be the same size
                player2_played_column.append(0)                  # player1's lists
                last_player = 'p1'                               # Set last_player to 'p1' so that the next turn, player2 will play (else statement just after)

            # Basically the same but for player2's turn.
            else:
                x , y = [int(x) for x in input("%s joue (ligne puis colonne) : "  %(player2)).split()]
                player2_played_line.append(x)
                player2_played_column.append(y)
                player1_played_line.append(0)
                player1_played_column.append(0)
                last_player = 'p2'

            turn += 1           #Increase turn at each turn

            for i in range(1,4):                # We use a double loop to parse the grid (one for lines and the other one for columns)
                for j in range(1,4):
                    for k in range(1,turn):     # We use this loop to parse lists of played coordonates

                        # If the current line and column are the same as coordonates stored ( for player1 )
                        if player1_played_line[k] == i and player1_played_column[k] == j:
                            # if the actual line is line1 and if line1[j-1] (case of the column in line1) hasn't been already played by player2:
                            if i == 1 and line1[j-1] != 'O ':
                                line1[j-1] = 'X '               #Then write 'X'
                            elif i == 2 and line2[j-1] != 'O ':     #Same tests are done for line2 and line3
                                line2[j-1] = 'X '
                            elif i == 3 and line3[j-1] != 'O ':
                                line3[j-1] = 'X '


                        # And same again for player 2
                        elif player2_played_line[k] == i and player2_played_column[k] == j:
                            if i == 1 and line1[j-1] != 'X ':
                                line1[j-1] = 'O '
                            elif i == 2 and line2[j-1] != 'X ':
                                line2[j-1] = 'O '
                            elif i == 3 and line3[j-1] != 'X ':
                                line3[j-1] = 'O '

                        # If actual case of the grid has not been played by any players, just keep an '- '
                        elif [player1_played_line[k] != i or player1_played_column[k] != j or player2_played_line[k] != i or player2_played_column[k] != j]:
                            if i == 1 and line1[j-1] != 'X ' and line1[j-1] != 'O ':
                                line1[j-1] = '- '
                            elif i == 2 and line2[j-1] != 'X ' and line2[j-1] != 'O ':
                                line2[j-1] = '- '
                            elif i == 3 and line3[j-1] != 'X ' and line3[j-1] != 'O ':
                                line3[j-1] = '- '

            # Then, print the updated grid ! :

            print ('')
            print (list_to_string(line1,'',1))
            print (list_to_string(line2,'',1))
            print (list_to_string(line3,'',1))
            print ('')

            ####################################################################

            # We will now check if there's an alignment (of 'X' or 'O ')
            # I know it could be better to implement another solution than checking each possibility.
            # But for only 8 cases, it was faster for me to do it like that than thinking about how to do it better

            # Check each column for 'X ' or 'O '
            # If there's an alignment, set winner at "username of player" and victory at "True". Print "Victoire for playerx"
            for l in range(3):
                if line1[l] == 'X ' and line2[l] == 'X ' and line3[l] == 'X ':
                    print("Victoire pour ", player1)
                    winner = player1
                    victory = True
                elif line1[l] == 'O ' and line2[l] == 'O ' and line3[l] == 'O ':
                    print("Victoire pour ", player2)
                    winner = player2
                    victory = True

            # Now we look at each line for each player
            if line1[0] == "X " and line1[1] == "X " and line1[2] == "X "  or line2[0] == 'X ' and line2[1] == 'X ' and line2[2] == 'X ' or line3[0] == 'X ' and line3[1] == 'X ' and line3[2] == 'X ':
                print ("Victoire pour ", player1)
                winner = player1
                victory = True
            elif line1[0] == 'O ' and line1[1] == 'O ' and line1[2] == 'O ' or line2[0] == 'O ' and line2[1] == 'O ' and line2[2] == 'O ' or line3[0] == 'O ' and line3[1] == 'O ' and line3[2] == 'O ':
                print ("Victoire pour ", player2)
                winner = player2
                victory = True

            # Then , check diagonals
            elif line1[0] == 'X ' and line2[1] == 'X ' and line3[2] == 'X ' or line1[2] == 'X ' and line2[1] == 'X ' and line3[0] == 'X ':
                print ("Victoire pour ", player1)
                winner = player1
                victory = True
            elif line1[0] == 'O ' and line2[1] == 'O ' and line3[2] == 'O ' or line1[2] == 'O ' and line2[1] == 'O ' and line3[0] == 'O ':
                print ("Victoire pour ", player2)
                winner = player2
                victory = True

            # If turn is > 9, then it's a draw ! Cause in case of victory, we would be out of the loop cause it's the stopping condition.
            if turn > 9:
                print ("Egalité !\n")
                egalite = True
        # Now that we are out of the loop, just to be sure that it's a draw, check "turn" and "egalite".
        # We'll go to the beginning of the loop to play again with "continue" and avoid the next part of the code (handling of scores) as no one has win
        if turn > 9 and egalite == True:
            continue

        #####################################################################################################################################

        # This part will handle scores

        # First, we'll try to read score.txt to check if the winner is in it and to increase his score.
        # So if the file exists, we'll search for the winner's name in it and we will increase his score.
        try:
            #The file is formated : One string per line, First line with a username, Second line with a score, etc
            # So even numbers lines will contain a username and odd numbers lines will contain a score
            with open("score.txt") as score:
                string_score = score.read()                 # String of the entire file
                list_score = string_score.splitlines()      # Convert the string to a list (each line of the string as an element of the list)
                for m in range(0,length(list_score),2):     #parse the list (stepping up by 2 at each turn)
                    if list_score[m] == winner:             # If winner's name is equal to a username (even number)
                        list_score[m+1] = int(list_score[m+1]) # get the next element (the score) as an int
                        list_score[m+1] += 1                   # add 1 to it
                        list_score[m+1] = str(list_score[m+1]) # convert it to a string again
                        winner_is_in_score = True              # store the fact that winner's name is in score file

        except FileNotFoundError:       # If the file doesn't exist, just print a blank new line
            print("")

        if winner_is_in_score:          # Now if winner's name is in score :
            with open("score.txt" , "w") as scor:               # We just need to write previously updated list in the file
                scor.write(list_to_string(list_score,'\n',1))   # We convert what we need to write to a string first and we add '\n' at the end of each element
        # else, winner's name isn't in score file, so we can append his name and his first point
        else:
            with open("score.txt" , "a") as sco:
                sco.write("%s\n1\n" %(winner))

        print('')
        replay = input ("Revenir au menu ? [o|n] ")         # Ask players if they want to go back to menu or quit

    #################################################################################

    # Now we handle others possible choices of the user ( Menu choice)

    elif menu_choice == 2:      #If choice = 2 ( See scores )
        # We try to open the score file
        try:
            with open("score.txt") as score:
                scores = score.readlines()                          # We get the content of the file as a list of each line
                                                                    # So even numbers elements will be only usernames
                                                                    # and odd numbers elements will be only scores numbers

                print(list_to_formated_string(scores), end = '')    # Then we use the "list_to_formated_string" function
                continue  #continue at the beginning of the loop    # to print the content (see the function at the beginning
                                                                    # to understand how it print each username and associated score on the same line)

        except FileNotFoundError:                                   # If file doesn't exists
            print ("\nPas de scores enregistrés ! Jouez une partie\n")
            continue

    elif menu_choice == 3:                                      # If user wants to reset scores
        with open("score.txt" , "w") as score:
            score.write('')                                     #Just write '' (nothing) to the file
            continue

    elif menu_choice == 4:                                  # If user wants to quit
        print ("A la prochaine !\n")
        exit()                                              # Then quit
    else:
        print("Erreur, entrez 1, 2, 3 ou 4")
        continue
