from Team_member import Team_member
import random
import math
class Link(Team_member):

	def __init__(self, name='Link', health=250, mp=250, stats={'Attack':30,'Defense':30,'Magic Attack':25,'Magic Defense':25,'Skill':15},
		level=18,currentxp=1000, xpneeded=1, is_alive=True, affinity={'Physical':1, 'Fire': 0.5, 'Ice': 0.5, 'Electricity': 1, 'Wind': 1, 'Light': 1, "Dark": 1},
		status={'Normal':True}, stat_multiplier={'Attack':1,'Defense':1,'Magic Attack':1,'Magic Defense':1,'Skill':1}):
		Team_member.__init__(self, name, health, mp, stats, level, currentxp, xpneeded, is_alive, affinity, status, stat_multiplier )

		self.attack_targets = ['enemy','enemy','friend','enemy']

	def get_attack_targets(self):
		return self.attack_targets

	def battle(self, enemy, action):
		if action == 1:
			return self.light_arrow(enemy)
		elif action == 2:
			return self.nayru_love(enemy)
		elif action == 3:
			return self.farore_wind(enemy)
		elif action == 4:
			return 0


	def attack(self, enemy):
		attack_base_power = 5
		attack_power = self.get_base_atk() * self.get_stat_multiplier()['Attack']
		enemy_defense = enemy.get_base_def() * enemy.get_stat_multiplier()['Defense']
		affinity = enemy.get_current_affinity()['Physical'] 
		effectiveness = affinity

		if random.randint(0,100) <= self.get_base_skill():
			damage = attack_power / (enemy_defense / 2) * attack_base_power * 1.2 * affinity 
			effectiveness = "Critical"
			print("Link did " + str(damage) + " damage to", enemy.get_name())

		else:
			damage = (attack_power / enemy_defense) * attack_base_power * effectiveness
			damage = math.floor(damage * random.randint(math.floor(damage * .8), math.floor(damage * 1.2)))
			print("Link did " + str(damage) + " damage to", enemy.get_name())

		return {'HP_Cost': 0, 'MP_Cost': 0, 'Damage': damage, 'Effectiveness': effectiveness, "Status": 'Normal', "Rotate": 0}

	def light_arrow(self, enemy): #Light magic(ish) damage and reduce enemy to 1 turn
		attack_base_power = 20
		attack_power = self.get_base_mg_atk() * self.get_stat_multiplier()['Magic Attack']
		enemy_defense = enemy.get_base_def() * enemy.get_stat_multiplier()['Magic Defense']
		affinity = enemy.get_current_affinity()['Light'] 
		effectiveness = affinity

		if random.randint(0,100) <= self.get_base_skill():
			damage = attack_power / (enemy_defense / 2) * attack_base_power * 1.2 * affinity 
			effectiveness = "Critical"
		else:
			damage = (attack_power / enemy_defense) * attack_base_power * effectiveness
			damage = damage * random.randint(math.floor(damage * .8), math.floor(damage * 1.2))
		damage = math.floor(damage)
		print("Link's light arrow did " + str(damage) + " damage to", enemy.get_name())

		return {'HP_Cost': 0, 'MP_Cost': 25, 'Damage': damage, 'Effectiveness': effectiveness, "Status": {}, "Rotate": 0}

	def nayru_love(self, friend): #tripples defense and reflects magic attacks for 1 turn
		print('Link protected', friend.get_name())
		return {'HP_Cost': 0, 'MP_Cost': 20, 'Damage': 0, 'Effectiveness': 'Debuff', "Status": {'Defense': 3, 'Magic Defense': 3}, "Rotate": 0}


	def farore_wind(self, enemy): #light wind attack and move to right
		attack_base_power = 10
		rotate = 1
		attack_power = self.get_base_atk() * self.get_stat_multiplier()['Attack']
		enemy_defense = enemy.get_base_def() * enemy.get_stat_multiplier()['Defense']
		affinity = enemy.get_current_affinity()['Wind'] 
		effectiveness = affinity

		if random.randint(0,100) <= self.get_base_skill():
			damage = attack_power / (enemy_defense / 2) * attack_base_power * 1.2 * affinity 
			effectiveness = "Critical"
			damage = math.floor(damage)

		else:
			damage = (attack_power / enemy_defense) * attack_base_power * effectiveness  # gets base power
			damage = damage * random.randint(math.floor(damage * .8), math.floor(damage * 1.2))
			damage = math.floor(damage)

		print("Link's Farore's Wind did", str(damage) + " damage to", enemy.get_name())
		if enemy.get_current_affinity()['Wind'] < 1:
			rotate = 0

		return {'HP_Cost': 0, 'MP_Cost': 15, 'Damage': damage, 'Effectiveness': effectiveness, "Status": 'Normal', "Rotate": rotate}

	def list_out_skills(self):
		print("list of skills include:")
		print("1.) Light Arrow: Base Power: 20, MP Cost: 25, Desc: Link shoots a light arrow at the enemy")
		print("2.) Nayru's Love: Base Power: --, HP Cost: 20, Desc: 'Triples an ally's defense'")
		print("3.) Farore's Wind: Base Power: 10, MP Cost: 10, Desc: 'Hits with a light wind attack and then switches one to right'")
		print("4.) Back")
		choice = int(input("Please enter your choice: "))
		if choice != 1 and choice != 2 and choice != 3 and choice != 4:
			print("Please type in 1, 2, 3, or 4.")
			return self.list_out_skills()
		else:
			return {'choice' : choice, 'length': 4}

	def get_party_status(self):
		print('\nName: Link')
		print('Current HP:', str(self.get_current_health()))
		print('Current MP:', str(self.get_current_mp()))
		print("Alive status:", str(self.is_alive()))
		print('Affinities:')
		for affinity in self.get_current_affinity():
			if self.get_current_affinity()[affinity] < 1:
				print("Resists", affinity)
			elif self.get_current_affinity()[affinity] == 1:
				print("Neutral to", affinity)
			else:
				print("Weak to", affinity)