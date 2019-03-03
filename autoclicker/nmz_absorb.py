import time
import threading
import random
import pynput
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from pynput import mouse
import os
import ast


class NmzAutoClicker:

	delay = 30.0
	ranging_pot_locations = []
	absorption_pot_locations = []

	rock_cake_location = None

	prayer_flick_location = None

	ranging_pot_sip_count = 4
	absorption_pot_sip_count = 4


	ranging_pot_counter = 4

	cmouse = Controller()

	def run(self):
		os.system('clear')
		print('---                           ---')
		print('--- Stefan\'s Nmz AutoClicker ---')
		print('---                           ---')

		self.get_locations()

		os.system('clear')
		input("Enter to start")
		os.system('clear')
		print('---                           ---')
		print('--- Stefan\'s Nmz AutoClicker ---')
		print('---                           ---')
		self.click_loop()
		print('Finished.')

	def get_locations(self):
		if not os.path.isfile('./locations.txt') or not input("Previous locations found - use them? (y)") == "y":
			self.set_locations()
			return

		file = open("./locations.txt", "r")

		self.ranging_pot_locations = list(ast.literal_eval(file.readline()))
		self.absorption_pot_locations = list(ast.literal_eval(file.readline()))
		self.prayer_flick_location = ast.literal_eval(file.readline())

		print(self.ranging_pot_locations)
		print(self.absorption_pot_locations)
		print(self.prayer_flick_location)

	def set_locations(self):
		self.set_range_pot_locations()
		os.system('clear')
		self.set_absorption_pot_locations()
		os.system('clear')
		self.set_prayer_flick_location()
		os.system('clear')

		with open("./locations.txt", "w") as f:
			f.write(str(self.ranging_pot_locations))
			f.write("\n")
			f.write(str(self.absorption_pot_locations))
			f.write("\n")
			f.write(str(self.prayer_flick_location))

	def click_list(self, location):
		randint = random.randint(0, 2)
		self.cmouse.position = (location[0][0] + float(randint), location[0][1] + float(randint))
		self.cmouse.click(Button.left, 1)
		time.sleep(0.4)

	def click(self, location):
		randint = random.randint(0, 2)
		self.cmouse.position = (location[0] + float(randint), location[1] + float(randint))
		self.cmouse.click(Button.left, 1)
		time.sleep(0.4)

	def flick_pray(self):
		print('Flicking prayer...')
		self.click(self.prayer_flick_location)
		time.sleep(0.2)
		self.click(self.prayer_flick_location)

	def eat_rock_cake(self):
		print('Eating rock cake...')
		location = self.rock_cake_location
		self.cmouse.position = location
		self.cmouse.click(Button.right, 1)
		time.sleep(0.6)
		self.cmouse.click(Button.left, 1)
		time.sleep(0.6)

	def sip_absorption(self):
		print('Sipping absorption potions...')

		for loc in self.absorption_pot_locations:
			self.click(loc)
			time.sleep(0.4)

	def sip_ranging_pot(self):
		if self.ranging_pot_locations:
			print('Sipping ranging potion...')
			self.click_list(self.ranging_pot_locations)
			self.ranging_pot_sip_count -= 1

	def set_range_pot_locations(self):
		range_pot_count = int(input("Number of ranging potions: "))

		for i in range(0, range_pot_count):
			print('Click range pot #{0}'.format(i))

			with mouse.Listener(on_click=self.set_ranging_pot) as listener:
				listener.join()
			time.sleep(0.1)

	def set_rock_cake_location(self):
		print('Click rock cake')

		with mouse.Listener(on_click=self.set_rock_cake) as listener:
			listener.join()
		time.sleep(0.1)

	def set_prayer_flick_location(self):

		print('Click prayer flick')

		with mouse.Listener(on_click=self.set_prayer_flick) as listener:
			listener.join()
		time.sleep(0.1)

	def set_prayer_flick(self, x, y, button, pressed):
		position = self.cmouse.position
		print('Prayerflick pot added at pos {0}'.format(
			position))
		self.prayer_flick_location = position
		return False

	def set_rock_cake(self, x, y, button, pressed):
		position = self.cmouse.position
		print('Rock cake added at pos {0}'.format(
			position))
		self.rock_cake_location = position
		return False

	def set_ranging_pot(self, x, y, button, pressed):
		position = self.cmouse.position
		print('Ranging pot added at pos {0}'.format(
			position))
		self.ranging_pot_locations.append(position)
		return False

	def set_absorption_pot_locations(self):
		absorption_pot_count = int(input("Number of absorption potions: "))

		for i in range(0, absorption_pot_count):
			print('Click absorption pot #{0}'.format(i))

			with mouse.Listener(on_click=self.set_absorption_pot) as listener:
				listener.join()
			time.sleep(0.1)

	def set_absorption_pot(self, x, y, button, pressed):
		position = self.cmouse.position
		print('absorption pot added at pos {0}'.format(
			position))
		self.absorption_pot_locations.append(position)
		return False

	def click_loop(self):

		# Every 30s click rock cake and flick pray.

		# Every now and then click all the other bullshit.
		# All of it? Sure.
		# Range pots? Idk man. whenever. Everyyy 5 min? sure. 5 * 5 * 4 = 100 minutes.
		# 100 minutes at first.

		ratio = 300 / 30
		counter = 400
		while counter > 0:
			counter -= 1
			time.sleep(0.2)
			self.flick_pray()
			# self.eat_rock_cake()

			if counter % ratio == 0:
				self.sip_ranging_pot()
				self.sip_absorption()

				if self.ranging_pot_sip_count == 0:
					self.ranging_pot_sip_count = 4
					self.ranging_pot_locations.pop(0)
					print('Finished sipping one ranging potion.')

				time.sleep(self.delay - 0.2 - 1.0 - 0.4 - len(self.absorption_pot_locations) * 0.4)

			else:
				time.sleep(self.delay - 0.2 - 1.0)

nmz = NmzAutoClicker()
nmz.run()
