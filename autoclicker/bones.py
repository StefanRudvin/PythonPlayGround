import ast
import os
import random
import time

from framework.input.Keyboard import Keyboard
from framework.input.FastMouse import FastMouse
from framework.utils import set_location


def main():

    altar_pos = (229, 1017)

    print('--- Stefan\'s Bones clicker ---')
    keyboard = Keyboard()
    mouse = FastMouse()
    # self.mouse.click(self.prayer_flick_location, 0.7)

    time.sleep(0.2)

    print('Starting in 5: ')
    time.sleep(1)
    print('4')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    #while True:
    #    time.sleep(0.2)
    #    print(mouse.get_pos())

    for i in range(0,80):
        cur_pos = mouse.get_pos()
        # print(mouse.get_pos())
        mouse.click_cur_pos()
        mouse.click(altar_pos, 0.01)
        mouse.move_mouse(cur_pos)
        time.sleep(0.5)
        print(str(80 - i))


main()
