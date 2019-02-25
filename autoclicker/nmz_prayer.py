import time
import threading
import random
import pynput
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from pynput import mouse
import os

class NmzAutoClicker():

    delay = 80.0
    random_delay_const = 200
    random_delay = 0

    ranging_pot_locations = []
    prayer_pot_locations = []

    ranging_pot_sip_count = 4
    prayer_pot_sip_count = 4

    ranging_pot_counter = 4

    cmouse = Controller()

    delay_bool = False

    def run(self):
        os.system('clear')
        print('---                           ---')
        print('--- Stefan\'s Nmz AutoClicker ---')
        print('---                           ---')

        self.setNewRandomDelay()
        self.getRangePotLocations()
        os.system('clear')
        self.getPrayerPotLocations()
        os.system('clear')
        input("Enter to start")
        os.system('clear')
        print('---                           ---')
        print('--- Stefan\'s Nmz AutoClicker ---')
        print('---                           ---')
        self.click_loop()
        print('Finished.')

    def setNewRandomDelay(self):
        random_delay = random.randint(0, self.random_delay_const) * 0.005

    def start_timer(self):
        print('Starting in: ')
        counter = 3

        while counter > 0:
            print(counter)
            counter -= 1
            time.sleep(1)

    def click(self,location):
        randint = random.randint(0, 2)
        self.cmouse.position = (location[0][0] + float(randint), location[0][1] + float(randint))
        self.cmouse.click_list(Button.left, 1)
        time.sleep(0.2)

    def sip_prayer_pot(self):
        print('Sipping prayer potion...')
        self.click(self.prayer_pot_locations)
        self.prayer_pot_sip_count -= 1

    def sip_ranging_pot(self):
        print('Sipping ranging potion...')
        self.click(self.ranging_pot_locations)
        self.ranging_pot_sip_count -= 1

    def getRangePotLocations(self):
        self.range_pot_count = int(input("Number of ranging potions: "))

        for i in range(0, self.range_pot_count):
            print('Click range pot #{0}'.format(i))

            with mouse.Listener(on_click=self.setRangingPot) as listener:
                listener.join()
            time.sleep(0.1)

    def setRangingPot(self, x, y, button, pressed):
        position = self.cmouse.position
        print('Ranging pot added at pos {0}'.format(
        position))
        self.ranging_pot_locations.append(position)
        return False

    def getPrayerPotLocations(self):
        self.prayer_pot_count = int(input("Number of prayer potions: "))

        for i in range(0, self.prayer_pot_count):
            print('Click prayer pot #{0}'.format(i))

            with mouse.Listener(on_click=self.setPrayerPot) as listener:
                listener.join()
            time.sleep(0.1)

    def setPrayerPot(self, x, y, button, pressed):
        position = self.cmouse.position
        print('Prayer pot added at pos {0}'.format(
        position))
        self.prayer_pot_locations.append(position)
        return False

    def click_loop(self):
        pot_ratio = int(len(self.prayer_pot_locations) / len(self.ranging_pot_locations))
        print("Prayer to ranging pot ratio: {0}".format(pot_ratio))
        while len(self.prayer_pot_locations) != 0:
            self.sip_prayer_pot()
            
            self.ranging_pot_counter += 1

            if self.ranging_pot_counter == pot_ratio:
                self.sip_ranging_pot()
                self.ranging_pot_counter = 0

            if self.prayer_pot_sip_count == 0:
                self.prayer_pot_sip_count = 4
                self.prayer_pot_locations.pop(0)
                print('Finished sipping one prayer potion.')

            if self.ranging_pot_sip_count == 0:
                self.ranging_pot_sip_count = 4
                self.ranging_pot_locations.pop(0)
                print('Finished sipping one ranging potion.')

            if self.delay_bool:
                self.setNewRandomDelay()
                time.sleep(self.delay - self.random_delay)
            else:
                time.sleep(self.delay + self.random_delay)

            self.delay_bool = not self.delay_bool

nmz = NmzAutoClicker()
nmz.run()