class GameStats():
	"""Track statistics for Alien Invasion"""
	def __init__(self, ai_settings):
		"""Initial stats"""
		self.ai_settings = ai_settings
		self.ships_left = ai_settings.ship_limit
		self.reset_stats()
		self.game_active = True

	def reset_stats(self):
		"""Initialize stas that can cnage during the game"""
		self.ships_left = self.ai_settings.ship_limit