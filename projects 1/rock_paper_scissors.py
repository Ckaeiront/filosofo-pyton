import random
choices = ['rock', 'paper', 'scissors']
c = 1
try:
    while c == 1:
        userChoices = int(
            input('choose from 1 to 3:\n1 - Rock 2 - Paper 3 - Scissors '))
        if userChoices > 3:
            print('number above the specified')
        userChoices = choices[userChoices - 1]
        computerChoice = random.choice(choices)
        results = [userChoices, computerChoice]
        if results[0] == 'rock' and results[1] == 'scissors':
            print('you choose ' + results[0] + ' against ' + results[1] + '...\nYou won! 😆')
        elif results[0] == 'paper' and results[1] == 'rock':
            print('you choose ' + results[0] + ' against ' + results[1] + '...\nYou won! 😆')
        elif results[0] == 'scissors' and results[1] == 'paper':
            print('you choose ' + results[0] + ' against ' + results[1] + '...\nYou won! 😆')
        elif results[0] == results[1]:
            print('you choose ' + results[0] + ' against ' + results[1] + '...\nDraw!')
        else:
            print('you choose ' + results[0] + ' against ' + results[1] + '...\nYou lost! 😔')
except ValueError:
    print('Please, type a number')
