class Enemy:

	def __init__(self, name, health, mp, stats, level, xp):
		self.name = name
		self.health = health
		self.mp = mp
		self.stats = stats
		self.level = level
		self.xp = xp
		self.name = name
		
	def get_name(self):
		return self.name

	def get_health(self):
		return self.health

	def get_mp(self):
		return self.mp

	def get_base_atk(self):
		return self.stats[0]

	def get_base_def(self):
		return self.stats[1]

	def get_base_mg_atk(self):
		return self.stats[2]

	def get_base_mg_def(self):
		return self.stats[3]

	def get_base_skill(self):
		return self.stats[4]

	def get_level(self):
		return self.level

	def get_xp(self):
		return self.xp


