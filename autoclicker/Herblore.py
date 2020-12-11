import ast
import os
import random
import time

from framework.input.Keyboard import Keyboard
from framework.input.Mouse import Mouse
from framework.utils import set_location


class Herblore:
    def __init__(self):
        pass

    use_current_mouse_pos = False
    offscreen_mouse_pos = None

    banker_location = None

    supply_1_bank_location = None
    supply_2_bank_location = None

    bank_all_location = None

    supply_1_inv_location = None
    supply_2_inv_location = None

    off_screen_locations = []

    keyboard = Keyboard()
    mouse = Mouse()

    potion_create_seconds = 17.5

    total_rounds = 100

    def run(self):
        os.system('clear')
        print('---                            ---')
        print('--- Stefan\'s Herb AutoClicker  ---')
        print('---                            ---')

        self.get_locations()

        os.system('clear')
        suggested_rounds = str(input("-> Number of rounds (Enter to start with default:" + str(self.total_rounds) + ")"))

        if suggested_rounds != "":
            self.total_rounds = suggested_rounds

        os.system('clear')
        print('---                            ---')
        print('--- Stefan\'s Herb AutoClicker  ---')
        print('---                            ---')
        self.click_loop()
        print('Finished.')

    def click_loop(self):
        currentRound = 0
        while currentRound < int(self.total_rounds):
            currentRound += 1
            time.sleep(0.5)
            self.click_all(currentRound, self.total_rounds)
            time.sleep(self.potion_create_seconds)

    def get_locations(self):
        if not os.path.isfile('./herb_locations.txt') or not input(
                "Previous locations found - use them? (enter for yes)") == "":
            self.set_locations()
            return

        file = open("./herb_locations.txt", "r")

        self.banker_location = list(ast.literal_eval(file.readline()))

        self.supply_1_bank_location = list(ast.literal_eval(file.readline()))
        self.supply_2_bank_location = list(ast.literal_eval(file.readline()))

        self.bank_all_location = list(ast.literal_eval(file.readline()))

        self.supply_1_inv_location = list(ast.literal_eval(file.readline()))
        self.supply_2_inv_location = list(ast.literal_eval(file.readline()))

        self.off_screen_locations = list(ast.literal_eval(file.readline()))

    def set_locations(self):
        self.banker_location = set_location("Banker", self.mouse)
        self.supply_1_bank_location = set_location("First Supply in bank", self.mouse)
        self.supply_2_bank_location = set_location("Second Supply in bank", self.mouse)
        self.supply_1_inv_location = set_location("First Supply in inventory", self.mouse)
        self.supply_2_inv_location = set_location("Second Supply in inventory", self.mouse)
        self.bank_all_location = set_location("Bank all", self.mouse)
        self.set_offscreen_locations()

        with open("./herb_locations.txt", "w") as f:
            f.write(str(self.banker_location))
            f.write("\n")
            f.write(str(self.supply_1_bank_location))
            f.write("\n")
            f.write(str(self.supply_2_bank_location))
            f.write("\n")
            f.write(str(self.bank_all_location))
            f.write("\n")
            f.write(str(self.supply_1_inv_location))
            f.write("\n")
            f.write(str(self.supply_2_inv_location))
            f.write("\n")
            f.write(str(self.off_screen_locations))

    def set_offscreen_locations(self):
        print('Setting offscreen locations')

        for i in range(0, 4):
            print('Click offscreen location #{0}'.format(i))
            time.sleep(0.1)
            self.off_screen_locations.append(set_location(" offscreen location #" + str(i), self.mouse))

    def move_mouse_off_screen(self):
        if self.use_current_mouse_pos:
            self.mouse.move_mouse(self.offscreen_mouse_pos)
        else:
            self.mouse.move_mouse(self.off_screen_locations[random.randint(0, 3)])

    def click_all(self, current_round, round_total):
        self.offscreen_mouse_pos = self.mouse.get_pos()

        print("Round: " + str(current_round) + " of:" + str(round_total))

        time.sleep(random.randint(500, 1000) / 1000)

        self.mouse.click(self.banker_location, 0.2)

        self.mouse.click(self.bank_all_location, 0.7)

        self.mouse.click(self.supply_1_bank_location, 0.3)

        self.mouse.click(self.supply_2_bank_location, 0.2)

        time.sleep(0.4)
        self.keyboard.close_interface()

        self.mouse.click(self.supply_1_inv_location, 0.4)

        self.mouse.click(self.supply_2_inv_location, 0)

        time.sleep(0.9)
        self.move_mouse_off_screen()
        self.keyboard.choose_default_action()


herb = Herblore()
herb.run()
