class Settings():
    """A class to store all settings for alien_convention"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        # ship settings

        self.ship_limit = 3

        #Bullet settings

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,160,60
        self.bullets_allowed = 3

        # Alien Setting

        self.fleet_drop_speed = 10


        # Initialize the game's static settings
        self.spedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the time"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction of 1 represnets right; -1 represents left.
        self.fleet_direction = 1

    def increse_speed(self):
        """Increase speed settings"""
        self.ship_speed_factor *= self.spedup_scale
        self.bullet_speed_factor *= self.spedup_scale
        self.alien_speed_factor *= self.spedup_scale
