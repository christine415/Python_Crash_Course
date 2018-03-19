class Settings():
    '''A class stores all the settings for Alien Invasion'''

    def __init__(self):
        '''Initialize the game's settings'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135,206,250)
        
        # Ship setting
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet setting
        # The bullet will travel slightly slower than the ship
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # Alien setting
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1