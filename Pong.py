import pygame

from settings import Settings

class Pong:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and create game resourcers."""

        # pygame setup
        pygame.init()
        self.settings = Settings()

        # Run in window mode
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()

    def run_game(self):
        """Start the main loop for the game."""
        running = True
        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill(self.settings.bg_color)

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    pong = Pong()
    pong.run_game()