import arcade as arc
from player import Player


class SpaceInvaders(arc.Window):
    def __init__(self):
        super().__init__(800, 600, "Space Invaders", fullscreen=True)
        self.player = Player()
    def on_key_press(self, symbol, modifiers):
        if symbol == arc.key.ESCAPE:
            arc.close_window()
    def on_draw(self):
        arc.start_render()
        
if __name__ == "__main__":
    SpaceInvaders()
    arc.run()
