from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key


class Keyboard:
    controller = KeyboardController()

    def close_interface(self):
        self.click_esc()

    def choose_default_action(self):
        self.click_space()

    def click_space(self):
        self.controller.press(Key.space)

    def click_esc(self):
        self.controller.press(Key.esc)
