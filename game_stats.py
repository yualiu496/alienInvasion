class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = 0
        self.read_high_score()


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        filename = "high_score.txt"
        with open(filename,"r") as f:
            self.high_score = int(f.read())

    def save_high_score(self):
        filename = "high_score.txt"
        with open(filename,"w") as f :
            f.write(f"{self.high_score}")