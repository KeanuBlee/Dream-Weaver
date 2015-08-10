class Team_member:

	def __init__(self, name, health, mp, stats, level, currentxp, xpneeded, is_alive, affinity):
		'''
		name is represented by a string
		stats is represented as a dictionary of ints
		affinity is represented as a dictionary of floats (<1 : they resist, 1 : normal, >1 : weak to)
		everything is represented by an int
		'''
		self.name = name
		self.health = health
		self.mp = mp
		self.stats = stats
		self.level = self.level
		self.currentxp = currentxp
		self.xpneeded = xpneeded
		self.is_alive = is_alive
		self.base_affinity = base_affinity # Character's base affinity
		self.current_affinity = base_affinity # Character's affinity including equipment/skills
		self.battle_affinity = base_affinity  # Character's affinity including buffs/debuffs at the battle level

	def get_name(self):
		return self.name

	def get_health(self):
		return self.health

	def get_mp(self):
		return self.mp

	def get_base_atk(self):
		return self.stats['Attack']

	def get_base_def(self):
		return self.stats['Defense']

	def get_base_mg_atk(self):
		return self.stats['Magic Attack']

	def get_base_mg_def(self):
		return self.stats['Magic Defense']

	def get_base_skill(self):
		return self.stats['Skill']

	def get_level(self):
		return self.level

	def get_currentxp(self):
		return self.currentxp

	def get_xpneeded(self):
		return self.xpneeded

	def is_Alive(self):
		return self.is_alive

	def get_base_affinity(self):
		return self.base_affinity

	def get_current_affinity(self):
		return self.current_affinity

	def get_battle_affinity(self):
		return self.battle_affinity

	def set_name(self, new_name):
		self.name = new_name

	def set_health(self, new_health):
		self.health = new_health

	def set_mp(self, new_mp):
		self.mp = new_mp

	def set_base_atk(self, new_atk):
		self.stats['Attack'] = new_atk

	def set_base_def(self, new_def):
		self.stats['Defense'] = new_def

	def set_base_mg_atk(self, new_mg_atk):
		self.stats['Magic Attack'] = new_mg_atk

	def set_base_mg_def(self, nw_mg_def):
		self.stats['Magic Defense'] = new_mg_def

	def set_base_skill(self, new_skill):
		self.stats['Skill'] = new_skill

	def set_level(self, new_level):
		self.level = new_level

	def set_currentxp(self, new_xp):
		self.currentxp = new_xp

	def set_xpneeded(self, new_xp):
		self.xpneeded = new_xp

	def set_alive(self, live_status):
		self.is_alive = live_status

	def set_base_affinity(self, new_affinity):
		self.base_affinity = new_affinity

	def set_current_affinity(self, new_affinity):
		self.current_affinity = new_affinity

	def set_battle_affinity(self, new_affinity):
		self.battle_affinity = new_affinity


