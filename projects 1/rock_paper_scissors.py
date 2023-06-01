import random
choices = ['rock', 'paper', 'scissors']
try:
    userChoices = int(
        input('choose from 1 to 3:\n1 - Rock 2 - Paper 3 - Scissors '))
    if userChoices > 3:
        print('number above the specified')
    userChoices = choices[userChoices - 1]
    computerChoice = random.choice(choices)
    print('Your choice was', userChoices,
          ' Computer choice was', computerChoice)
except ValueError:
    print('Please, type a number')
