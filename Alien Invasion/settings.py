class Settings:
# A class to store all the settings for Alien Invasion.
    def __init__(self):
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10,10,10)
        # Ship Settings.
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet Settings.
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # Alien Settings
        self.alien_speed = 0.5 
        self.fleet_drop_speed = 10

        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        self.increase_speed()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1

        # Scoring.
        self.alien_points = 50
    
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
    
        self.alien_points = int(self.alien_points * self.score_scale)

        # fleet_direction of 1 represents to right; -1 represents to left.
        self.fleet_direction = 1