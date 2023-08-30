import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    """
    Spawn a player
    """

    def __init__(self, pong_game):
        """Create a player object at the both sides of the screen"""

        super().__init__()
        self.screen = pong_game.screen
        self.settings = pong_game.settings
        self.color = self.settings.player_color

        