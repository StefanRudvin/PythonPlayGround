import random
import time

from pynput.mouse import Button
from pynput.mouse import Controller as MouseController

from framework.input.MouseCurve import get_curve_points


class FastMouse:
    random_delay = 100
    controller = MouseController()

    def get_pos(self):
        return self.controller.position

    def click(self, location):
        try:
            self.controller.click(location, 0)
        except:
            print("Error clicking location")
        time.sleep(0.1)

    def click_cur_pos(self):
        self.controller.click(Button.left, 1)
        time.sleep(0.1)

    def click(self, location, wait):
        self.move_mouse(location)
        time.sleep(0.05 + wait)
        self.controller.click(Button.left, 1)
        time.sleep(0.05)
        time.sleep(random.randint(0, self.random_delay) * 0.0005)

    def move_mouse(self, location):
        randint = random.randint(0, 3)
        randomized_location = (location[0] + float(randint), location[1] + float(randint))
        curve = self.get_curve_list(self.controller.position, randomized_location)
        speed_counter = 0
        while self.controller.position != randomized_location:
            self.controller.position = curve.pop(0)
            if (len(curve) > 100):
                curve.pop(100)
            else:
                curve.pop(len(curve) - 1)
            randint = random.randint(0, 30)
            if randint == 1:
                time.sleep(0.0000000001 + speed_counter)
            # speed_counter += 0.000000001

    def mid_point(self, point_a, point_b):
        return int(point_a + ((point_b - point_a) / 2))

    def get_curve_list(self, start, end):
        curvature = 1
        mid_point = (self.mid_point(start[0], end[0]) + random.randint(7, 15) * curvature,
                     self.mid_point(start[1], end[1]) + random.randint(7, 15) * curvature)
        return get_curve_points([start, start, mid_point, end, end, end, end])
    #
    # def get_curve_list(self, start, end):
    #     return get_curve_points([start, start, end, end, end, end])
