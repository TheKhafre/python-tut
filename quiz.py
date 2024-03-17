def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print(key)
        for i in Options[question_num - 1]:
            print(i)
        guess = input("Enter answer (A, B, C, or D): ").upper()
        print("__________________________")
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
        print("__________________________")
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0

def display_score(correct_guesses, guesses):
    print("________________________")
    print("RESULT")
    print("________________________")

    print("answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")

    print()

    score = int((correct_guesses/len(questions))*100)
    print("you score is: "+str(score) +"%")

def play_again():
    response = input("Do you want to play again?(yes/no): ").lower()
    if response == "yes":
        return True
    else:
        return False

questions = {"What is the capital of Germany?":"A",
"Who created Python?":"B",
"Where is Ile-Ife?":"D",
"Whats is the color of Snow?":"C"}

Options = [["A. Berlin","B. Dutchland","C. Slovenia","D. Krav Maga"],
["A. Guido Reisin","B. Guido Van Rossum","C. Guido Alv Reisin","D. Van de Vick"],
["A. Ondo State","B. Ipetumodu State","C. Oyo State","D. Osun State"],
["A. Bright Yellow","B. Sky Blue","C. White","D. Tulip"]]

new_game()
while play_again():
    new_game()

print("byeeeeeeeeee!")
