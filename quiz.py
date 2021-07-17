guesses = []
no_of_guesses = 0
score = 0

def check_answer(answer, guess):
    global score
    if answer == guess:
        print("Correct:")
        score += 1

    else:
        print("Incorrect!")

questions = {
    "Who is hacker rhoemon?": "A",
    "Who learned mysql?": "B",
    "What is javascript use in?":"A"
}

options = [["A. Hacker", "B. Programmer"],
           ["A. Database Management System", "B. RDBMS"],
           ["A. Front End Web Development", "B. Back End Development"]]


for question in questions:
    print(question)
    for option in options[no_of_guesses]:
        print(option)

    no_of_guesses = no_of_guesses + 1

    guess = input("Enter your guess (A,B):")
    guess.upper()
    if guess != "A" and guess != "B":
        print("You typed something else")
        break
    else:
        guesses.append(guess)


    check_answer(questions.get(question), guess)

print("You scored " +str(score) +"out of "+ str(len(questions)))













