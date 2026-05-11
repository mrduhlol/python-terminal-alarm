import time
import datetime as dt
import pygame

def set_alarm(alarm_time):
    print(f"Alarm has been set to {alarm_time}")
    sound_file = "my_music.mp3"
    is_rurnning = True

    while is_rurnning:
        current_time = dt.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("Wake up IDIOT!!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)


            is_rurnning = False

        time.sleep(1)

if __name__=="__main__":
    alarm = input("Enter the time to set alarm : ")
    set_alarm(alarm)