import arcade as arc
from player import Player


class SpaceInvaders(arc.Window):
    def __init__(self):
        super().__init__(800, 600, "Space Invaders", fullscreen=True)
        self.player = Player(self.width / 2, self.height * 0.04)
    
    def on_key_press(self, symbol, modifiers):
        if symbol == arc.key.ESCAPE:
            arc.close_window()
        if symbol == arc.key.A:
            self.player.move_left()
        if symbol == arc.key.D:
            self.player.move_right()

    def on_key_release(self, symbol, modifiers):
        if symbol == arc.key.A:
            self.player.stop()
        if symbol == arc.key.D:
            self.player.stop()
    
    def on_draw(self):
        arc.start_render()
        self.player.draw()

    def on_update(self, time):
        self.player.update()
if __name__ == "__main__":
    from sys import argv
    from os import chdir
    chdir(argv[0].rpartition("/")[0])
    SpaceInvaders()
    arc.run()
