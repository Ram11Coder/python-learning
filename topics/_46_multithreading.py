# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading.Thread(target=my_function)


import threading
import time


def walk_dog(first):
    time.sleep(8)
    print(f"You finish walking {first}")


def read_book():
    time.sleep(2)
    print(f"You finish reading book")


def send_mail():
    time.sleep(4)
    print(f"You finish sending mail")


chore1 = threading.Thread(target=walk_dog, args=(
    "Scooby",))  # if it is only one arg then we need to end with , then python consider as tuple
chore1.start()

chore2 = threading.Thread(target=read_book)
chore2.start()

chore3 = threading.Thread(target=send_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()
print("All chores are completed!")
