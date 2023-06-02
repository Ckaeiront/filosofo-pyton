import random
choices = ['rock', 'paper', 'scissors']
while True:
    userChoices = int(
        input('choose from 1 to 3:\n1 - Rock 2 - Paper 3 - Scissors '))
    if userChoices > 3 or userChoices < 0:
        print('invalid number')
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
    playAgain = int(input('you wanna play again?:\n1 - Yes / 2 - No '))
    if playAgain != 1:
        break

# 👆 my version of the code
