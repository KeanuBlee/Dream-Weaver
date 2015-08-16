from Team_member import Team_member
import random
import math

class Okabe(Team_member):

	def __init__(self, name='Okabe', health=150, mp=300, stats={'Attack':15,'Defense':20,'Magic Attack':40,'Magic Defense':35,'Skill':5},
		level=18,currentxp=1000, xpneeded=1, is_alive=True, affinity={'Physical':0.75, 'Fire': 1, 'Ice': 1.5, 'Electricity': 0.5, 'Wind': 1, 'Light': 1, "Dark": 1},
		status={'Normal':True}, stat_multiplier={'Attack':1,'Defense':1,'Magic Attack':1,'Magic Defense':1,'Skill':1}):

		Team_member.__init__(self, name, health, mp, stats, level, currentxp, xpneeded, is_alive, affinity, status, stat_multiplier )
		self.attack_targets = ['enemy','enemy','enemy','enemy','friend']

	def get_attack_targets(self):
		return self.attack_targets


	def battle(self, enemy, action):

		if action == 1:
			return self.bit_particle_cannon(enemy)
		elif action == 2:
			return self.moad_snake(enemy)
		elif action == 3:
			return self.cyolume_saber(enemy)
		elif action == 4:
			return self.phone_microwave(enemy)
		elif action == 5:
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
			print("Okabe did " + str(damage) + " damage to", enemy.get_name())

		else:
			damage = (attack_power / enemy_defense) * attack_base_power * effectiveness
			damage = math.floor(damage * random.randint(math.floor(damage * .8), math.floor(damage * 1.2)))
			print("Okabe did " + str(damage) + " damage to", enemy.get_name())
		return {'HP_Cost': 0, 'MP_Cost': 0, 'Damage': damage, 'Effectiveness': effectiveness, "Status": 'Normal', "Rotate": 0}



	def bit_particle_cannon(self, enemy): # Future Gadget #1 Magic attack that deals electric damage
		attack_base_power = 15
		attack_power = self.get_base_mg_atk() * self.get_stat_multiplier()['Magic Attack']
		enemy_defense = enemy.get_base_def() * enemy.get_stat_multiplier()['Magic Defense']
		affinity = enemy.get_current_affinity()['Electricity'] 
		effectiveness = affinity

		if random.randint(0,100) <= self.get_base_skill():
			damage = attack_power / (enemy_defense / 2) * attack_base_power * 1.2 * affinity 
			effectiveness = "Critical"
		else:
			damage = (attack_power / enemy_defense) * attack_base_power * effectiveness
			damage = damage * random.randint(math.floor(damage * .8), math.floor(damage * 1.2))
		damage = math.floor(damage)
		print("Okabe's bit particle cannon did " + str(damage) + " damage to", enemy.get_name())

		return {'HP_Cost': 0, 'MP_Cost': 25, 'Damage': damage, 'Effectiveness': effectiveness, "Status": {}, "Rotate": 0}



	def moad_snake(self, enemy): #Future Gadget #4 temporarily debuffs enemy to skill of 0 and paralyzes
		return {'HP_Cost': 0, 'MP_Cost': 30, 'Damage': 0, 'Effectiveness': 'Debuff', "Status": {'Paralyze': True, 'Skill': 0}, "Rotate": 0}

	def cyolume_saber(self, enemy): # Future Gadget # 6 light physical with chance of poisoning
		attack_base_power = 5
		attack_power = self.get_base_atk() * self.get_stat_multiplier()['Attack']
		enemy_defense = enemy.get_base_def() * enemy.get_stat_multiplier()['Defense']
		affinity = enemy.get_current_affinity()['Physical'] 
		effectiveness = affinity

		if random.randint(0,100) <= self.get_base_skill():
			damage = attack_power / (enemy_defense / 2) * attack_base_power * 1.2 * affinity 
			effectiveness = "Critical"
		else:
			damage = (attack_power / enemy_defense) * attack_base_power * effectiveness
			damage = damage * random.randint(math.floor(damage * .8), math.floor(damage * 1.2))
		damage = math.floor(damage)
		print("Okabe's cyolume saber did " + str(damage) + " damage to", enemy.get_name())

		return {'HP_Cost': 10, 'MP_Cost': 0, 'Damage': damage, 'Effectiveness': effectiveness, "Status": {'Poison': True}, "Rotate": 0}

	def phone_microwave(self, friend): #Future Gadget #8 Fully heals one party member
		friend.set_current_hp(friend.get_base_hp())
		print("Okabe fully healed", friend.get_name() + "!")
		return {'HP_Cost': 0, 'MP_Cost': 80, 'Damage': 0, 'Effectiveness': 0, "Status": {}, "Rotate": 0}
		

	def list_out_skills(self):
		print("list of skills include:")
		print("1.) Bit Particle Cannon: Base Power: 15, MP Cost: 25, Affinity: Elec")
		print("2.) Moad Snake: Base Power: --, MP Cost: 30, Desc: 'Temporarily debuffs enemy's skill and paralyzes'")
		print("3.) Cyolume Saber Base Power: 5, HP Cost: 10, Desc: 'Light attack with chance of poisoning'")
		print("4.) Phone Microwave Base Power: --, MP Cost: 80, Desc: 'Fully heals one party member'")
		print("5.) Back")
		choice = int(input("Please enter your choice: "))
		if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
			print("Please type in 1, 2, 3, 4, or 5.")
			return self.list_out_skills()
		else:
			return {'choice' : choice, 'length': 5}

	def get_party_status(self):
		print('\nName: Okabe')
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