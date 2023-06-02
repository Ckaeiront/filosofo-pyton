questions = {
    'who created python?': 'A',
    'What year was python created?': 'B',
    'python is tributed to which comedy group?': 'C',
    'Is the earth round?': 'A',
}
options = [['A. Guido van Rossum', 'B. Elon Musk', 'C. Bill Gates', 'D. Mark Zuckerburg'],
           ['A. 1989', 'B. 1991', 'C. 2000', 'D. 2016'],
           ['A. Lonely Island', 'B. Smosh', 'C. Monty Python', 'D. SNL'],
           ['A. True', 'B. False', 'C. sometimes', 'D. What\'s earth?']]
# -------------------------
def new_game():
    print('The genius quiz')
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print('---------------')
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input('Enter (A, B, C or D)').upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)
    play_again()
# ------------------------
def check_answer(answer, guess):
    if answer == guess:
        print('Correct!!!')
        return 1
    else:
        print("Wrooong!")
        return 0
# -------------------------
def display_score(correct_guesses, guesses):
    print('-------------------------')
    print('RESULTS')
    print('-------------------------')
    print('Answers: ', end='')
    for i in questions:
        print(questions.get(i), end='')
    print()
    print('guesses: ', end='')
    for i in guesses:
        print(i, end='')
    print()
    score = int(correct_guesses/len(questions) * 100)
    print('Your score is ' + str(score) + '%')
# -------------------------
def play_again():
    res = input('you wanna play again?\n1 - Yes / 2 - No ')
    if res == 1:
        return True
    else:
        return False
# -------------------------
new_game()

while play_again() == True:
    new_game()

print('byeee!!!')
