import time
import threading
import random
import pynput
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 1.0
random_delay = 200
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')
counter = 0

mouse = Controller()


def start_timer():
    print('Starting in: ')
    counter = 3

    while counter > 0:
        print(counter)
        counter -= 1
        time.sleep(1)

def click():
    mouse.click(button)
    time.sleep(delay)
    time.sleep(random.randint(0, random_delay) * 0.005)


def click_loop(counter, times_to_run):
    while True:
        if counter < times_to_run:
            click()
            click()
            counter += 1

            print('Click #', counter, ',', (times_to_run - counter), 'times left')
        else:
            break

print('--- Stefan\'s AutoClicker ---')
times_to_run = int(input("Times to run: "))
start_timer()
click_loop(counter, times_to_run)

print('Finished. Ran ', times_to_run, ' times.')
