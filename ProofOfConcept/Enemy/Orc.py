from Enemy import Enemy
class Orc(Enemy):

	def __init__(self, health=500, mp=200, stats=[100,50,15,10,20],level=20,xp=1000, name='Orc'):
		Enemy.__init__(self, health, mp, stats, level, xp)


