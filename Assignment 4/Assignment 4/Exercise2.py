﻿while True:
    userInput1 = str(raw_input('rock, paper or scissors player 1: ')).lower()
    userInput2 = str(raw_input('rock, paper or scissors player 2: ')).lower()
    user1 = bool()
    user2 = bool()
    if userInput1 != 'rock' and userInput1 != 'paper' and userInput1 != 'scissors':
        print('Not a valid input for player 1, choose between rock, paper or scissors.')
    else:
        user1 = True
        if userInput2 != 'rock' and userInput2 != 'paper' and userInput2 != 'scissors':
            print('Not a valid input for player 2, choose between rock, paper or scissors.')
        else:
            user2 = True
    if user1 and user2:
        if userInput1 == 'rock' and userInput2 == 'paper':
            print('Player 2 wins because paper beats rock')
        elif userInput1 == 'rock' and userInput2 == 'scissors':
            print('Player 1 wins because rock smashes scissors')
        elif userInput1 == 'paper' and userInput2 == 'rock':
            print('Player 1 wins because paper beats rock')
        elif userInput1 == 'paper' and userInput2 == 'scissors':
            print('Player 2 wins because scissors cut paper')
        elif userInput1 == 'scissors' and userInput2 == 'rock':
            print('Player 2 wins because rock smashes scissors')
        elif userInput1 == 'scissors' and userInput2 == 'paper':
            print('Player 1 wins because scissors cut paper')
        else:
            print('No winner!')
        break