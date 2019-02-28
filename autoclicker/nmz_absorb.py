import time
import threading
import random
import pynput
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from pynput import mouse
import os


class NmzAutoClicker():
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

		self.getRangePotLocations()
		os.system('clear')
		self.getAbsorptionPotLocations()
		os.system('clear')
		self.setPrayerFlickLocation()
		os.system('clear')
		self.setRockCakeLocation()
		os.system('clear')
		input("Enter to start")
		os.system('clear')
		print('---                           ---')
		print('--- Stefan\'s Nmz AutoClicker ---')
		print('---                           ---')
		self.click_loop()
		print('Finished.')

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
		print(self.prayer_flick_location)
		self.click(self.prayer_flick_location)
		self.click(self.prayer_flick_location)

	def eat_rock_cake(self):
		print('Eating rock cake...')
		randint = random.randint(0, 2)
		location = self.rock_cake_location
		self.cmouse.position = (location[0] + float(randint), location[1] + float(randint))
		self.cmouse.click(Button.right, 1)
		time.sleep(0.4)
		self.click(self.rock_cake_location)
		time.sleep(0.2)

	def sip_absorption(self):
		print('Sipping absorption potions...')

		for loc in self.absorption_pot_locations:
			self.click(loc)
			time.sleep(0.4)

	def sip_ranging_pot(self):
		print('Sipping ranging potion...')
		self.click_list(self.ranging_pot_locations)
		self.ranging_pot_sip_count -= 1

	def getRangePotLocations(self):
		self.range_pot_count = int(input("Number of ranging potions: "))

		for i in range(0, self.range_pot_count):
			print('Click range pot #{0}'.format(i))

			with mouse.Listener(on_click=self.setRangingPot) as listener:
				listener.join()
			time.sleep(0.1)

	def setRockCakeLocation(self):
		print('Click rock cake')

		with mouse.Listener(on_click=self.setRockCake) as listener:
			listener.join()
		time.sleep(0.1)

	def setPrayerFlickLocation(self):

		print('Click prayer flick')

		with mouse.Listener(on_click=self.setPrayerFlick) as listener:
			listener.join()
		time.sleep(0.1)

	def setRockCake(self, x, y, button, pressed):
		position = self.cmouse.position
		print('Rock cake added at pos {0}'.format(
			position))
		self.rock_cake_location = position
		return False

	def setPrayerFlick(self, x, y, button, pressed):
		position = self.cmouse.position
		print('Rock cake added at pos {0}'.format(
			position))
		self.rock_cake_location = position
		return False

	def setRangingPot(self, x, y, button, pressed):
		position = self.cmouse.position
		print('Pray flick added at pos {0}'.format(
			position))
		self.ranging_pot_locations.append(position)
		return False

	def getAbsorptionPotLocations(self):
		self.absorption_pot_count = int(input("Number of absorption potions: "))

		for i in range(0, self.absorption_pot_count):
			print('Click absorption pot #{0}'.format(i))

			with mouse.Listener(on_click=self.setAbsorptionPot) as listener:
				listener.join()
			time.sleep(0.1)

	def setPrayerFlick(self, x, y, button, pressed):
		position = self.cmouse.position
		print('Prayerflick pot added at pos {0}'.format(
			position))
		self.prayer_flick_location = position
		return False

	def setAbsorptionPot(self, x, y, button, pressed):
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
		counter = 200
		while counter > 0:
			counter -= 1
			time.sleep(0.2)
			self.flick_pray()
			self.eat_rock_cake()

			if counter % ratio == 0:
				self.sip_ranging_pot()
				self.sip_absorption()
				self.ranging_pot_sip_count -= 1

				if self.ranging_pot_sip_count == 0:
					self.ranging_pot_sip_count = 4
					self.ranging_pot_locations.pop(0)
					print('Finished sipping one ranging potion.')

				time.sleep(self.delay - 0.2 - 0.8 - 1 - 0.4 - len(self.absorption_pot_locations)*0.4)

			else:
				time.sleep(self.delay - 0.2 - 0.8 - 1)


nmz = NmzAutoClicker()
nmz.run()
