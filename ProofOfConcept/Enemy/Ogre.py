from Enemy import Enemy
import random
import math
class Ogre(Enemy):

	def __init__(self, name='Ogre', health=1800, mp=200, stats={'Attack':100,'Defense':35,'Magic Attack':15,'Magic Defense':8,'Skill':20},
		level=20,xp=1000, is_alive=True, affinity={'Physical':1, 'Fire': 1, 'Ice': 0.5, 'Electricity': 1.25, 'Wind': 0.5, 'Light': 1.25, "Dark": 0.75},
		status={'Normal':True}, stat_multiplier={'Attack':1,'Defense':1,'Magic Attack':1,'Magic Defense':1,'Skill':1}):
		Enemy.__init__(self, name, health, mp, stats, level, xp, is_alive, affinity, status, stat_multiplier )


	def battle_logic(self, enemy):

		if 'Paralyze' in self.get_status() and self.get_status()['Paralyze'] > 0:
			chance = random.randint(0,2)
			if chance == 1:
				print("Ogre was paralyzed and couldn't move!")
				return 0

		if 'Posion' in self.get_status() and self.get_status()['Poison'] > 0:
			poison_damage = .05 * self.get_base_health()
			self.set_current_health(self.get_current_health() - math.floor(poison_damage))
			print("Ogre was poisoned and took " + str(poison_damage) + " damage!")

		if enemy.get_current_affinity()["Ice"] > 1 and self.get_current_mp() > 15:
			return self.ogre_icy_club(enemy)

		elif (enemy.get_current_health() / enemy.get_base_health()) < .5 and self.get_current_health() > 30:
			return self.ogre_crushing_blow(enemy)

		else: 
			randNum = random.randint(0,100)
			if (randNum < 30) and self.get_current_health() > 15:
				return self.ogre_club_attack(enemy)
			elif (randNum >= 70) and self.get_current_health() > 30:
				return self.ogre_crushing_blow(enemy)
			elif (randNum >= 30 and randNum < 70):
				return self.attack(enemy)
			else:
				if self.get_current_mp() > 15 and self.get_current_health > 5:
					return self.ogre_icy_club(enemy)
				else: 
					return self.attack(enemy)

	def attack(self, enemy):
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
			print('Ogre attack did', str(damage) + " damage to", enemy.get_name())

		return {'HP_Cost': 0, 'MP_Cost': 0, 'Damage': damage, 'Effectiveness': effectiveness, "Status": 'Normal', "Rotate": 0}


	def ogre_club_attack(self, enemy): # Does physical damage and moves rotation one to the right
		attack_base_power = 10
		rotate = 1
		attack_power = self.get_base_atk() * self.get_stat_multiplier()['Attack']
		enemy_defense = enemy.get_base_def() * enemy.get_stat_multiplier()['Defense']
		affinity = enemy.get_current_affinity()['Physical'] 
		effectiveness = affinity

		if random.randint(0,100) <= self.get_base_skill():
			damage = attack_power / (enemy_defense / 2) * attack_base_power * 1.2 * affinity 
			effectiveness = "Critical"
			damage = math.floor(damage)

		else:
			damage = (attack_power / enemy_defense) * attack_base_power * effectiveness  # gets base power
			damage = damage * random.randint(math.floor(damage * .8), math.floor(damage * 1.2))
			damage = math.floor(damage)

		print('Ogre club attack did', str(damage) + " damage to", enemy.get_name())
		if enemy.get_current_affinity()['Physical'] < 1:
			rotate = 0

		return {'HP_Cost': 15, 'MP_Cost': 0, 'Damage': damage, 'Effectiveness': effectiveness, "Status": 'Normal', "Rotate": rotate}


	def ogre_icy_club(self, enemy): # Covers club in ice and whacks opponent with it. Consumes both mp and hp as a cost.
		attack_base_power = 20
		attack_power = self.get_base_atk() * self.get_stat_multiplier()['Attack']
		enemy_defense = enemy.get_base_def() * enemy.get_stat_multiplier()['Defense']
		affinity = enemy.get_current_affinity()['Ice'] 
		effectiveness = affinity

		if random.randint(0,100) <= self.get_base_skill():
			damage = attack_power / (enemy_defense / 2) * attack_base_power * 1.2 * affinity 
			effectiveness = "Critical"

		else:
			damage = (attack_power / enemy_defense) * attack_base_power * effectiveness
			damage = damage * random.randint(math.floor(damage * .8), math.floor(damage * 1.2))

		damage = math.floor(damage)
		print('Ogre icy club attack did', str(damage) + " damage to", enemy.get_name())

		return {'HP_Cost': 5, 'MP_Cost': 15, 'Damage': damage, 'Effectiveness': effectiveness, "Status": 'Normal', "Rotate": 0}


	def ogre_crushing_blow(self, enemy): # Does immense physical damage
		attack_base_power = 35
		attack_power = self.get_base_atk() * self.get_stat_multiplier()['Attack']
		enemy_defense = enemy.get_base_def() * enemy.get_stat_multiplier()['Defense']
		affinity = enemy.get_current_affinity()['Physical'] 
		effectiveness = affinity

		if random.randint(0,100) <= self.get_base_skill():
			damage = attack_power / (enemy_defense / 2) * attack_base_power * 1.2 * affinity 
			effectiveness = "Critical"
		else:
			damage = (attack_power / enemy_defense) * attack_base_power * effectiveness  # gets base power
			damage = damage * random.randint(math.floor(damage * .8), math.floor(damage * 1.2))
		damage = math.floor(damage)
		print('Ogre crushing blow attack did', str(damage) + " damage to", enemy.get_name())

		return {'HP_Cost': 35, 'MP_Cost': 0, 'Damage': damage, 'Effectiveness': effectiveness, "Status": 'Normal', "Rotate": 0}
