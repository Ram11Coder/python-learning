# Puzzle quiz game

questions = ("How many elements in the periodic table?",
             "How many bones in the human body?",
             "Which state is capital of india?")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. 216", "B. 217", "C. 218", "D. 219"),
           ("A. Tamil nadu", "B. Delhi", "C. Mumbai", "D. Kolkata"))

answers = ("C", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("_______________________________________________")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter the option (A,B,C,D ) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("------------------------------------------------")
print("                   RESULT                       ")
print("------------------------------------------------")
print("Answers : ")
for answer in answers:
    print(answer, end=" ")
print()
print("Guesses : ")
for guess in guesses:
    print(guess, end=" ")
print()
percentage = round(score / len(answers) * 100, 2)
print(f"Total percentage : {percentage}%")