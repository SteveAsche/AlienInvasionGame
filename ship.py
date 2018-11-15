"""This module will define the ship class"""
import pygame

class Ship():

	"""This is the ship class"""

	def __init__(self, ai_settings, screen):
		"""initialize the ship an its starting position"""
		self.screen = screen
		self.ai_settings = ai_settings
		#load the ship image and get its rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		#Start each ship at the bottom center
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#Store a dicimal value for the ship's center
		self.center = float(self.rect.centerx)
		self.center_y = float(self.rect.centery)

		#Movement flage
		self.moving_right = False
		self.moving_left = False
		#added to control up and down movement
		self.moving_up = False
		self.moving_down = False


	def update(self):
		"""Update the ship's position based on the movement flags"""
		#update the ships cetner value, not the rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top > 0:
			self.center_y -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.center_y += self.ai_settings.ship_speed_factor
		# Update rect object from self.center
		self.rect.centerx = self.center
		self.rect.centery = self.center_y





	def blitme(self):
		"""Draw teh ship at its current location"""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""Center the ship on hte screen"""
		self.center = self.screen_rect.centerx

