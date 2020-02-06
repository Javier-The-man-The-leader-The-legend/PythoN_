import arcade
from sesion05 import data, bubble
def map_value(value, prev_min, prev_max, new_min, new_max):
    previous_range = prev_max - prev_min
    new_range = new_max - new_min
    position_of_value = (value - prev_min) / previous_range
    new_value = position_of_value * new_range
    return new_value + new_min
class Window(arcade.Window):
    def __init__(self):
        super().__init__(1000, 700, "Bubble Sort Visualisation")
        arcade.set_background_color((255, 255, 255))
        self.bars = [Bar(self.width / len(data), map_value(d, 0, 100, 50, self.height)) for d in data]
        self.j = 0
        self.i = 0
        # for d in data:
            # self.barsappend(Bar(self.width / len(data), d))
    def on_draw(self):
        arcade.start_render()
        # for bar in self.bars:
        for i, bar in enumerate(self.bars):
            bar = self.bars[i]
            bar.set_x_position(i * bar.width)
            bar.draw()
    def on_update(self, delta_time):
        self.j, self.i = bubble(self.bars, self.j, self.i)
class Bar(arcade.Sprite):
    def __init__(self, width, height):
        super().__init__("black.png")
        self.width = width
        self.height = height
        self.bottom = 0
    def set_x_position(self, left):
        self.left = left
    def __gt__(self, other):
        return self.height > other.height
Window()
arcade.run()