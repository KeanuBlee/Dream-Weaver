class Team_member:

	def __init__(self, name, health, mp, stats, level, currentxp, xpneeded, is_alive, affinity, status, stat_multiplier):
		'''
		name is represented by a string
		stats is represented as a dictionary of ints
		affinity is represented as a dictionary of floats (<1 : they resist, 1 : normal, >1 : weak to)
		status is represnted by a string
		everything else is represented by an int
		'''
		self.name = name
		self.base_health = health
		self.current_health = health
		self.base_mp = mp
		self.current_mp = mp
		self.stats = stats
		self.level = level
		self.currentxp = currentxp
		self.xpneeded = xpneeded
		self.alive = is_alive
		self.base_affinity = affinity # Character's base affinity
		self.current_affinity = affinity # Character's affinity including equipment/skills
		self.battle_affinity = affinity  # Character's affinity including buffs/debuffs at the battle level
		self.status = status
		self.stat_multiplier = stat_multiplier
		self.already_attacked = False


	def get_name(self):
		return self.name

	def get_base_health(self):
		return self.base_health

	def get_current_health(self):
		return self.current_health

	def get_base_mp(self):
		return self.base_mp

	def get_current_mp(self):
		return self.current_mp

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

	def is_alive(self):
		return self.alive

	def get_base_affinity(self):
		return self.base_affinity

	def get_current_affinity(self):
		return self.current_affinity

	def get_battle_affinity(self):
		return self.battle_affinity

	def get_status(self):
		return self.status

	def get_stat_multiplier(self):
		return self.stat_multiplier

	def get_already_attacked(self):
		return self.already_attacked

	def set_name(self, new_name):
		self.name = new_name

	def set_base_health(self, new_health):
		self.base_health = new_health

	def set_current_health(self, new_health):
		self.current_health = new_health

	def set_base_mp(self, new_mp):
		self.base_mp = new_mp

	def set_current_mp(self, new_mp):
		self.current_mp = new_mp

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
		self.alive = live_status

	def set_base_affinity(self, new_affinity):
		self.base_affinity = new_affinity

	def set_current_affinity(self, new_affinity):
		self.current_affinity = new_affinity

	def set_battle_affinity(self, new_affinity):
		self.battle_affinity = new_affinity

	def set_status(self, new_status):
		self.status = new_status

	def set_stat_multiplier(self, new_mult):
		self.stat_multiplier = new_mult

	def set_already_attacked(self, boole):
		self.already_attacked = boole