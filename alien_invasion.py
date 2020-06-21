import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from alien import Alien


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen, ai_settings)
    # Make the Play btton.
    play_button = Button(ai_settings , screen , "Play")
    # Make an alien
    # alien = Alien(ai_settings, screen)
    # Make a group to store bullets,aliens in.
    bullets = Group()
    aliens = Group()

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    # Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for game
    while True:
        # watch for keyboard and mouse event

        gf.check_events(ai_settings, screen,stats , play_button ,  ship,aliens, bullets)
        if stats.game_active:

            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets )

        gf.update_screen(ai_settings, screen,stats, ship, aliens, bullets , play_button)


run_game()
