import ast
import os
import random
import time

from framework.input.Keyboard import Keyboard
from framework.input.Mouse import Mouse
from framework.utils import set_location

def get_int_time():
    return int(time.time())

class NmzAutoClicker:
    use_current_mouse_pos = True
    offscreen_mouse_pos = None

    delay = 30.0
    overload_locations = []
    absorption_pot_locations = []

    orb_location = None
    prayer_flick_location = None

    overload_sip_count = 4
    absorption_pot_sip_count = 4

    keyboard = Keyboard()
    mouse = Mouse()

    last_overload_sip_time = None
    last_pray_flick = None

    off_screen_locations = []

    def run(self):
        os.system('clear')
        print('---                           ---')
        print('--- Stefan\'s Nmz AutoClicker ---')
        print('---                           ---')

        self.get_locations()

        os.system('clear')
        input("Enter Nmz now and place your character in the middle with autoretaliate on and rapid heal on quick prayer.")
        os.system('clear')
        print('---                           ---')
        print('--- Stefan\'s Nmz AutoClicker ---')
        print('---                           ---')
        self.setup_loop()
        self.click_loop()
        print('Finished.')

    def get_locations(self):
        if not os.path.isfile('./nmz_absorb_work_locations.txt') or not input(
                "Previous locations found - use them? (y)") == "y":
            self.set_locations()
            return

        file = open("./nmz_absorb_work_locations.txt", "r")

        self.overload_locations = list(ast.literal_eval(file.readline()))
        self.absorption_pot_locations = list(ast.literal_eval(file.readline()))
        self.prayer_flick_location = ast.literal_eval(file.readline())
        self.orb_location = ast.literal_eval(file.readline())
        self.off_screen_locations = list(ast.literal_eval(file.readline()))

        print(self.overload_locations)
        print(self.absorption_pot_locations)
        print(self.prayer_flick_location)
        print(self.orb_location)

    def set_locations(self):
        self.set_enhance_pot_locations()
        os.system('clear')
        self.set_absorption_pot_locations()
        os.system('clear')
        self.orb_location = set_location("Rock cake / Locator Orb ", self.mouse)
        os.system('clear')

        self.prayer_flick_location = set_location("Quick prayer ", self.mouse)
        # self.set_offscreen_locations()

        os.system('clear')

        with open("./nmz_absorb_work_locations.txt", "w") as f:
            f.write(str(self.overload_locations))
            f.write("\n")
            f.write(str(self.absorption_pot_locations))
            f.write("\n")
            f.write(str(self.prayer_flick_location))
            f.write("\n")
            f.write(str(self.orb_location))
            f.write("\n")
            f.write(str(self.off_screen_locations))

    def set_offscreen_locations(self):
        print('Setting offscreen locations')

        for i in range(0, 4):
            print('Click offscreen location #{0}'.format(i))
            time.sleep(0.1)
            self.off_screen_locations.append(set_location(" offscreen location #" + str(i), self.mouse))

    def flick_pray(self):
        print('Flicking prayer...')
        self.mouse.click(self.prayer_flick_location, 2)
        self.mouse.click(self.prayer_flick_location, 0.2)
        self.last_pray_flick = get_int_time()

    def use_locator_orb(self):
        print('Using locator orb/rock cake...')
        self.mouse.click(self.orb_location, 0.8)

    def sip_absorptions(self):
        print('Sipping absorption potions...')

        for loc in self.absorption_pot_locations:
            self.mouse.click(loc, 0.8)

    def sip_overload_and_use_orb(self):
        time.sleep(1)
        if self.overload_locations:
            print('Sipping overload potion...')
            self.mouse.click(self.overload_locations[len(self.overload_locations) - 1], 2)
            self.last_overload_sip_time = get_int_time()

            self.overload_sip_count -= 1
            if self.overload_sip_count == 0:
                self.overload_locations.pop()
                self.overload_sip_count = 4

        time.sleep(9)
        self.use_locator_orb()
        self.use_locator_orb()
        self.use_locator_orb()
        self.use_locator_orb()
        self.use_locator_orb()

    def set_enhance_pot_locations(self):
        enhance_pot_count = int(input("Number of overload potions: "))
        for i in range(0, enhance_pot_count):
            self.overload_locations.append(set_location("Overload pot #" + str(i + 1), self.mouse))

    def set_absorption_pot_locations(self):
        absorption_pot_count = int(input("Number of absorption potions: "))
        for i in range(0, absorption_pot_count):
            self.absorption_pot_locations.append(set_location("Absorption pot #" + str(i + 1), self.mouse))

    def setup_loop(self):
        print("Starting Nmz run...")
        self.offscreen_mouse_pos = self.mouse.get_pos()
        self.sip_absorptions()
        self.sip_overload_and_use_orb()
        self.flick_pray()
        self.use_locator_orb()
        self.use_locator_orb()
        self.use_locator_orb()
        self.use_locator_orb()
        self.use_locator_orb()
        self.use_locator_orb()
        self.use_locator_orb()
        self.use_locator_orb()
        time.sleep(1)
        self.move_mouse_off_screen()

    def move_mouse_off_screen(self):
        if self.use_current_mouse_pos:
            self.mouse.move_mouse(self.offscreen_mouse_pos)
        else:
            self.mouse.move_mouse(self.off_screen_locations[random.randint(0, 3)])

    def click_loop(self):
        print("Starting loop...")
        start_time = get_int_time()
        overload_total_time = 305
        regen_time = 55
        run_time = 160 * 60
        drinking_ovl = False

        while get_int_time() - start_time < run_time:
            current_time = get_int_time()
            move_offscreen = False

            if current_time - self.last_overload_sip_time >= overload_total_time:
                drinking_ovl = True
                self.offscreen_mouse_pos = self.mouse.get_pos()
                self.sip_overload_and_use_orb()
                move_offscreen = True
                self.sip_absorptions()
                drinking_ovl = False

            if not drinking_ovl and (current_time - self.last_pray_flick) >= regen_time and (current_time - self.last_overload_sip_time) <= (overload_total_time - 120):
                self.offscreen_mouse_pos = self.mouse.get_pos()
                self.flick_pray()
                self.use_locator_orb()

                move_offscreen = True

            if move_offscreen:
                self.move_mouse_off_screen()

            time.sleep(1)

nmz = NmzAutoClicker()
nmz.run()
