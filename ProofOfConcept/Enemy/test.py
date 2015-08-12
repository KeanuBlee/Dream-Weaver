from Ogre import Ogre

ogre = Ogre()
ogre_affinity = ogre.get_battle_affinity()

for thing in ogre_affinity:
	if ogre_affinity[thing] < 1:
		print("ogre resists", thing)
	elif ogre_affinity[thing] == 1:
		print("ogre is neutral to", thing)
	else:
		print("ogre is weak to", thing)
