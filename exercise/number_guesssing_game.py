# Number guessing game
import random

low_num = 10
high_num = 100

rand_num = random.randint(low_num, high_num)

is_running = True
guessing_count = 0
while is_running:
    num = input("Guess the number : ")
    guessing_count += 1
    if num.isdigit():
        number_guess = int(num)
        if not low_num < number_guess < high_num:
            print(f"Enter the number between {low_num} and {high_num}")
        elif number_guess > rand_num:
            print("Too high... try again!")
        elif number_guess < rand_num:
            print("Too low... try again!")
        else:
            print(f"CORRECT! number was : {rand_num}")
            print(f"No of guesses : {guessing_count}")
            break
    else:
        print("Invalid guess!!")
        print(f"Enter the number between {low_num} and {high_num}")
