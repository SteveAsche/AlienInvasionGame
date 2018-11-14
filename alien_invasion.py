""" First attempt at an graphical game"""


import pygame
from settings import Settings 
from ship import Ship 
import game_functions as gf 
from pygame.sprite import Group
from alien import Alien



def run_game():
	# Initialize game and create screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#Make a ship and group of bullets an alien and a group of Aliens
	ship = Ship(ai_settings, screen)
	# Make a Group to store bullets in
	bullets = Group()
	# Make an alien group
	aliens = Group()

	#create a fleet of aliens
	gf.create_fleet(ai_settings, screen, ship, aliens)



	bg_color = ai_settings.bg_color 
	while True:
		#watch for keyboard input
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
		gf.update_aliens(ai_settings, aliens)

		gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
