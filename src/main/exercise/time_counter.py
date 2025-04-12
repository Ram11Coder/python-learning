import time

time_in_sec = int(input("Enter the time in seconds : "))

for x in range(time_in_sec, 0, -1):
    sec = x % 60
    min = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{min:02}:{sec:02}")
    time.sleep(1)

print("TIMES UP!!")