class Settings:
    """A class to store all settings for Pong."""

    def __init__(self) -> None:
        """Initialize the game's static settings"""

        # Screen settings

        # Window mode
        self.screen_width = 1280
        self.screen_height = 720

        self.bg_color = (0, 0, 0)

        # Player settings
        self.player_width = 3
        self.player_height = 30

        