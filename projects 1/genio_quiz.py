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
    correct_guesses = None
    question_num = 1
    for key in questions:
        print('---------------')
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input('Enter (A, B, C or D)').upper()
        guesses.append(guess)
        question_num += 1
# ------------------------
def check_answer(userInput, correctAnswer):
    score = 0
    if userInput == correctAnswer:
        print('Correct!!!')
        score += 1
        print('Next one...')
        return score
    else:
        return score
# -------------------------
def display_score(score_num):
    pass
# -------------------------
def play_again():
    pass
# -------------------------
new_game()
