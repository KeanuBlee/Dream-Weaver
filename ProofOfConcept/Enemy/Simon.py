from Team_member import Team_member
import random
import math

class Simon(Team_member):

	def __init__(self, name='Simon', health=250, mp=100, stats={'Attack':20,'Defense':30,'Magic Attack':25,'Magic Defense':25,'Skill':40},
		level=18,currentxp=1000, xpneeded=1, is_alive=True, affinity={'Physical':1, 'Fire': 0.5, 'Ice': 1, 'Electricity': 0.75, 'Wind': 1, 'Light': 1, "Dark": 1},
		status={'Normal':True}, stat_multiplier={'Attack':1,'Defense':1,'Magic Attack':1,'Magic Defense':1,'Skill':1}):
		Team_member.__init__(self, name, health, mp, stats, level, currentxp, xpneeded, is_alive, affinity, status, stat_multiplier )
		self.attack_targets = ['enemy','friend','enemy','friend']

	def get_attack_targets(self):
		return self.attack_targets

	def battle(self, enemy, action):
		if action == 1:
			return self.rally(enemy)
		elif action == 2:
			return self.giga_drill_break(enemy)
		elif action == 3:
			return self.pierce_the_heavens(enemy)
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
			print("Simon did " + str(damage) + " damage to", enemy.get_name())

		else:
			damage = (attack_power / enemy_defense) * attack_base_power * effectiveness
			damage = math.floor(damage * random.randint(math.floor(damage * .8), math.floor(damage * 1.2)))
			print("Simon did " + str(damage) + " damage to", enemy.get_name())

		return {'HP_Cost': 0, 'MP_Cost': 0, 'Damage': damage, 'Effectiveness': effectiveness, "Status": 'Normal', "Rotate": 0}

	def rally(self, friend): #a Team member beside Simon get 1.5 in all stat multipliers(does not stack)
		return {'HP_Cost': 0, 'MP_Cost': 10, 'Damage': 0, 'Effectiveness': 'Debuff', "Status": {'Attack': 1.5, 'Magic Attack': 1.5, 'Magic Defense':1.5, 'Defense' : 1.5, 'Skill': 1.5}, "Rotate": 0}


	def giga_drill_break(self, enemy): #Doubles crit rate, halves enemy's defense(for attack) and does heavy physical damage
		attack_base_power = 35
		attack_power = self.get_base_atk() * self.get_stat_multiplier()['Attack']
		enemy_defense = enemy.get_base_def() * enemy.get_stat_multiplier()['Defense']
		affinity = enemy.get_current_affinity()['Physical'] 
		effectiveness = affinity

		if random.randint(0,100) <= (self.get_base_skill() * 2):
			damage = attack_power / (enemy_defense / 4) * attack_base_power * 1.2 * affinity 
			effectiveness = "Critical"
		else:
			damage = (attack_power / (enemy_defense/2)) * attack_base_power * effectiveness  # gets base power
			damage = damage * random.randint(math.floor(damage * .8), math.floor(damage * 1.2))

		damage = math.floor(damage)
		print("Simon's Giga Drill Break did", str(damage) + " damage to", enemy.get_name())

		return {'HP_Cost': 50, 'MP_Cost': 0, 'Damage': damage, 'Effectiveness': effectiveness, "Status": 'Normal', "Rotate": 0}

	def pierce_the_heavens(self, friend): # Spend mp to revive fallen team mate 
		friend.set_current_hp(friend.get_base_hp())
		friend.set_alive(True)
		print("Simon fully healed", friend.get_name() + "!")
		return {'HP_Cost': 0, 'MP_Cost': 70, 'Damage': 0, 'Effectiveness': 0, "Status": {}, "Rotate": 0}

	def list_out_skills(self):
		print("list of skills include:")
		print("1.) Rally: Base Power: --, MP Cost: 10, Desc: a Team member beside Simon get 1.5 in all stat multipliers")
		print("2.) Giga Drill Break: Base Power: 35, HP Cost: 50, Desc: 'Attacks with giant drill. Enemy's defense is halved and crit rate is doubled for attack")
		print("3.) Pierce The Heavens: Base Power: --, MP Cost: 70, Desc: 'Fully heals/revives ally'")
		print("4.) Back")
		choice = int(input("Please enter your choice: "))
		if choice != 1 and choice != 2 and choice != 3 and choice != 4:
			print("Please type in 1, 2, 3, or 4.")
			return self.list_out_skills()
		else:
			return {'choice' : choice, 'length': 4}

	def get_party_status(self):
		print('\nName: Simon')
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