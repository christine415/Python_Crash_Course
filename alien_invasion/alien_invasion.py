import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    '''Initialize game and creat a screen object'''
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make a ship
    ship = Ship(screen)

    # Make an alien
    alien = Alien(screen)

    # Start the main loop for the game
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship, alien)

run_game()