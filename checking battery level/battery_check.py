import psutil
import playsound
import time
import os

check_count = 0
playing_audio = False

while True:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    os.system('cls')

    if percent < 90 and not plugged and not playing_audio:
        playsound.playsound('Air-Raid.mp3')
        print(f"Low battery! Your laptop's battery is at {percent}%.")


    print(f"Battery level: {percent}%")
    print(f"Plugged in: {plugged}")
    print(f"Check count: {check_count}")

    time.sleep(3)
    check_count += 1
