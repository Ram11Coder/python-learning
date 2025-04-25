import time
import datetime
import pygame


def alarmClock(alarm_time):
    print(f"Alarm set for {alarm_time}")
    is_running = True
    alarm_music = "hacker-alarm-124960.mp3"
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("WAKE UP 😪")
            is_running = False
            pygame.mixer.init()
            pygame.mixer.music.load(alarm_music)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)

        time.sleep(1)


if __name__ == '__main__':
    alarm_time = input("Enter the time format in (HH:MM:SS) : ")
    alarmClock(alarm_time)


# multi threading