from random import randint
from sys import exit
print('ROCKS, PAPERS, SCISSORS')
wins = 0
losses = 0
ties = 0
while True:
    print('%s win, %s losses, %s ties'%(wins, losses, ties))
    while True:
        playerMove = input("Enter: (r)ocks, (p)apers, (s)cissors, (q)uit:")
        if playerMove == 'q':
            exit(print('%s win, %s losses, %s ties'%(wins, losses, ties)))
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print("Enter r- rocks , p- papers, s -scissors, q-quit")
    if playerMove == 'r':
        print('Rock versus')
    elif playerMove == 'p':
        print('Paper versus')
    elif playerMove== 's':
        print('Scissors versus')
    computerMove=''
    randomNumber = randint(1, 3)
    if randomNumber == 1 :
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
            
print('%s win, %s losses, %s ties'%(wins, losses, ties))