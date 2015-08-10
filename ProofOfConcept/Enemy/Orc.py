from Enemy import Enemy
class Orc(Enemy):

	def __init__(self, name='Orc', health=500, mp=200, stats={'Attack':100,'Defense':50,'Magic Attack':15,'Magic Defense':10,'Skill':20},
		level=20,xp=1000, is_alive=True, affinity={'Physical':1, 'Fire': 1, 'Ice': 0.5, 'Electricity': 1.5, 'Wind': 0.5, 'Light': 1, "Dark": 0.75}):
		Enemy.__init__(self, name, health, mp, stats, level, xp, is_alive, affinity )


