
# Random

import random

low = 1
high = 100
print(random.randint(low, high))
options = ["rock", "paper", "scissor"]

option = random.choice(options)
print(option)

print(random.random())

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "A", "K", "Q"]
random.shuffle(cards)
print(cards)
