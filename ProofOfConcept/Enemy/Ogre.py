from Enemy import Enemy
import random
class Ogre(Enemy):

	def __init__(self, name='ogre', health=500, mp=200, stats={'Attack':100,'Defense':35,'Magic Attack':15,'Magic Defense':8,'Skill':20},
		level=20,xp=1000, is_alive=True, affinity={'Physical':1, 'Fire': 1, 'Ice': 0.5, 'Electricity': 1.5, 'Wind': 0.5, 'Light': 1, "Dark": 0.75},
		status='Normal', stat_multiplier={'Attack':1,'Defense':1,'Magic Attack':1,'Magic Defense':1,'Skill':1}):
		Enemy.__init__(self, name, health, mp, stats, level, xp, is_alive, affinity, status, stat_multiplier )


	def battle_logic(self, enemy):
		if self.get_status == "Paralyzed":
			chance = randNum(0,2)
			if chance == 1:
				print("Ogre was paralyzed and couldn't move!")
				return 0

		if self.get_status == "Posoined":
			poison_damage = .05 * self.get_base_health()
			self.set_current_health(self.get_current_health() - poison_damage)
			print("Ogre was poisoned and took " + str(poison_damage) + " damage!")

		if enemy.get_current_affinity()["Ice"] > 1 and self.get_current_mp() > 15:
			return self.ogre_icy_club(enemy)

		elif (enemy.get_current_health() / enemy.get_base_health()) < .5 and self.get_current_health() > 30:
			return self.ogre_crushing_blow(enemy)

		else: 
			randNum = random.randint(0,100)
			if (randNum < 70) and self.get_current_health() > 15:
				return self.ogre_club_attack(enemy)
			elif (randNum >= 70) and self.get_current_health() > 30:
				return self.ogre_crushing_blow(enemy)
			else:
				if self.get_current_mp() > 15 and self.get_current_health > 5:
					return self.ogre_icy_club(enemy)
				else: 
					print("Ogre was unable to do anything.")
					return 0


	def ogre_club_attack(self, enemy): # Does physical damage and moves rotation one to the right
		attack_base_power = 10
		rotate = 1
		attack_power = self.get_base_attack() * self.get_stat_multiplier()['Attack']
		enemy_defense = enemy.get_base_def() * enemy.get_stat_multiplier()['Defense']
		affinity = enemy.get_current_affinity()['Physical'] 
		effectiveness = affinity

		if random.randint(0,100) <= self.get_base_skill():
			damage = attack_power / (enemy_defense / 2) * attack_base_power * 1.2 * affinity 
			effectiveness = "Critical"
		else:
			damage = (attack_power / enemy_defense) * attack_base_power * effectiveness  # gets base power
			damage = damage * random.randint(damage * .8, damage * 1.2) # adds the random element

		if enemy.get_current_affinity()['Physical'] < 1:
			rotate = 0

		return {'HP_Cost': 15, 'MP_Cost': 0, 'Damage': damage, 'Effectiveness': effectiveness, "Status": Normal, "Rotate": rotate}


	def ogre_icy_club(self, enemy): # Covers club in ice and whacks opponent with it. Consumes both mp and hp as a cost.
		attack_base_power = 20
		attack_power = self.get_base_attack() * self.get_stat_multiplier()['Attack']
		enemy_defense = enemy.get_base_def() * enemy.get_stat_multiplier()['Defense']
		affinity = enemy.get_current_affinity()['Ice'] 
		effectiveness = affinity

		if random.randint(0,100) <= self.get_base_skill():
			damage = attack_power / (enemy_defense / 2) * attack_base_power * 1.2 * affinity 
			effectiveness = "Critical"
		else:
			damage = (attack_power / enemy_defense) * attack_base_power * effectiveness
			damage = damage * random.randint(damage * .8, damage * 1.2)

		return {'HP_Cost': 5, 'MP_Cost': 15, 'Damage': damage, 'Effectiveness': effectiveness, "Status": Normal, "Rotate": 0}


	def ogre_crushing_blow(self, enemy): # Does immense physical damage
		attack_base_power = 35
		attack_power = self.get_base_attack() * self.get_stat_multiplier()['Attack']
		enemy_defense = enemy.get_base_def() * enemy.get_stat_multiplier()['Defense']
		affinity = enemy.get_current_affinity()['Physical'] 
		effectiveness = affinity

		if random.randint(0,100) <= self.get_base_skill():
			damage = attack_power / (enemy_defense / 2) * attack_base_power * 1.2 * affinity 
			effectiveness = "Critical"
		else:
			damage = (attack_power / enemy_defense) * attack_base_power * effectiveness  # gets base power
			damage = damage * random.randint(damage * .8, damage * 1.2) # adds the random element

		return {'HP_Cost': 35, 'MP_Cost': 0, 'Damage': damage, 'Effectiveness': effectiveness, "Status": Normal, "Rotate": 0}
