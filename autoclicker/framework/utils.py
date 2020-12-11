import os
import time

from pynput import mouse


def set_location(name, this_mouse):
    os.system('clear')
    input('Click ' + name)
    with mouse.Listener(on_click=set_location_listener) as listener:
        listener.join()
    time.sleep(0.1)
    return this_mouse.get_pos()

def set_location_listener(x, y, button, pressed):
    time.sleep(0.1)
    return False
