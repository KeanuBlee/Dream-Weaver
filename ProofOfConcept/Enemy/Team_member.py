class Team_member:

	def __init__(self, name, health, mp, stats, level, currentxp, xpneeded, is_alive):
		self.name = name
		self.health = health
		self.mp = mp
		self.stats = stats
		self.level = self.level
		self.currentxp = currentxp
		self.xpneeded = xpneeded
		self.is_alive = is_alive

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

	def get_currentxp(self):
		return self.currentxp

	def get_xpneeded(self):
		return self.xpneeded

	def is_Alive(self):
		return self.is_alive

	def set_health(self, new_health):
		self.health = new_health

	def set_mp(self, new_mp):
		self.mp = new_mp
