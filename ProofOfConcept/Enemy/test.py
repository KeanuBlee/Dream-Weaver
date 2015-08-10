from Orc import Orc

orc = Orc()
orc_affinity = orc.get_battle_affinity()

for thing in orc_affinity:
	if orc_affinity[thing] < 1:
		print("Orc resists", thing)
	elif orc_affinity[thing] == 1:
		print("Orc is neutral to", thing)
	else:
		print("Orc is weak to", thing)
