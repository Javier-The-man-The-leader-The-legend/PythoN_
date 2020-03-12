from arcade import Sprite
class Player(Sprite):
    def __init__(self):
        super().__init__("SpaceInvaders/spaceship.png", image_x=0, image_y=0, image_width=72, image_height=72)
