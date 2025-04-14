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
                print(f"{number_guess} is greater than guessing number")
        elif number_guess < rand_num:
                print(f"{number_guess} is lower than guessing number")
        else:
                print(f"{number_guess} is CORRECT!")
                break
    else:
        print("Invalid guess!!")
        print(f"Enter the number between {low_num} and {high_num}")

print(f"Total guessing : {guessing_count} , number was : {rand_num}")
