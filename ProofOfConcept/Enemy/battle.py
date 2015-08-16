turn_count = 2
enemy_turn_count = 0
active_member = 0
player_turn = True
time_to_update = True

def battle(party, enemies):
	beginning()
	global player_turn
	global turn_count
	global enemy_turn_count
	global active_member
	global time_to_update

	enemy_turn_count = 2 if len(enemies) <= 2 else len(enemies)
	base = enemy_turn_count
	while (not is_dead(enemies) and (not is_dead(party))):
		if time_to_update:
			update(party, enemies)
			time_to_update = False


		if player_turn:
			player = party[active_member]
			player_choice(party, enemies)
			if is_dead(enemies):
				print("Congrats! You Win!")
			if turn_count <= 0:
				player_turn = False
				enemy_turn_count = base
				time_to_update = True

		elif enemy_turn_count > 0:
			player = party[active_member]
			for enemy in enemies:
				print('')
				outcome = enemy.battle_logic(player)
				if outcome == 0:
					print("Ogre was paralyzed and cold not move!")
				else:
					enemy.set_current_health(enemy.get_current_health() - outcome['HP_Cost'])
					enemy.set_current_mp(enemy.get_current_health() - outcome['MP_Cost'])
					player.set_current_health(player.get_current_health() - outcome['Damage'])
				
					if (outcome['Effectiveness'] == "Critical" or outcome['Effectiveness'] > 1) and not player.get_already_attacked():
						if outcome['Effectiveness'] == "Critical":
							print(enemy.get_name() + " got a critical hit!")
						elif outcome['Effectiveness'] > 1:
							print(enemy.get_name() + " hit a weak spot!")
						enemy_turn_count += 1
						player.set_already_attacked(True)

					if outcome['Rotate'] != 0:
						force_rotate(party,outcome['Rotate'])
					enemy_turn_count -= 1

				if player.get_current_health() <= 0:
					player.set_alive(False)
					if is_dead(party):
						print("Sorry, you lose! Bitch")
						print(enemies[0].get_current_health())
					else:
						switch(party, enemies, True)

			if enemy_turn_count <= 0:
				player_turn = True
				turn_count = 2
				time_to_update = True
def beginning():
	global turn_count
	turn_count = 2
	global enemy_turn_count
	enemy_turn_count = 0
	global active_member
	active_member = 0
	global player_turn
	player_turn = True
	global time_to_update
	time_to_update = True

def force_rotate(party, amount):
	global active_member
	player = party[active_member]
	if amount > 0:
		direction = 'right'
	elif amount < 0:
		direction = 'left'
	new_member = (active_member + amount) % len(party)
	while not party[new_member].is_alive() :
		if direction == 'right':
			new_member += 1
		elif direction == 'left':
			new_member -= 1
	active_member = new_member

def update(party, enemies):
	for member in party:
		status = member.get_status();
		member.set_already_attacked(False)
		for ailment in status:
			if ailment != 'Normal':
				if status[ailment] > 0:
					status[ailment] -= 1
				if ailment in ['Attack', 'Defense', 'Magic Attack', 'Magic Defense', 'Skill'] and status[ailment] <= 0:
					stats = member.get_stat_multiplier()
					stats[ailment] = 1
					member.set_stat_multiplier(stats)

	for enemy in enemies:
		status = enemy.get_status();
		enemy.set_already_attacked(False)
		for ailment in status:
			if ailment != 'Normal':
				if status[ailment] > 0:
					status[ailment] -= 1
				if ailment in ['Attack', 'Defense', 'Magic Attack', 'Magic Defense', 'Skill'] and status[ailment] <= 0:
					stats = enemy.get_stat_multiplier()
					stats[ailment] = 1
					enemy.set_stat_multiplier(stats)



def is_dead(array):
	for entry in array:
		if (entry.is_alive()):
			return False
	return True

def print_battle_screen(party, enemies):
	print("\n\nActive Member:", party[active_member].get_name())
	print("Current HP: " + str(party[active_member].get_current_health()) + " Current MP: " + str(party[active_member].get_current_mp()))
	print("Turn Count: " + str(turn_count))

def player_choice(party, enemies):
	global turn_count
	turn_complete = False
	print_battle_screen(party, enemies)
	player = party[active_member]
	print("\nYour current choices are:")
	print("1.) Attack")
	print("2.) Skills")
	print("3.) Switch")
	print("4.) Status of Party")
	choice = int(input("Please input your choice here: "))

	while (choice != 1 and choice != 2 and choice != 3 and choice != 4):
		print("Please type in 1, 2, 3, or 4.")
		choice = int(input("Please input your choice here: "))
	print('')
	if choice == 1:
		turn_complete = True
		ec = enemy_choice(enemies)
		if ec > len(enemies):
			player_choice(party, enemies)
			turn_complete = False
		else:
			enemy = enemies[ec - 1]
			print('')
			outcome = player.attack(enemy)
			if (outcome['Effectiveness'] == "Critical" or outcome['Effectiveness'] > 1) and not enemy.get_already_attacked():
				if outcome['Effectiveness'] == "Critical":
					print(player.get_name() + " got a critical hit!")
				elif outcome['Effectiveness'] > 1:
					print(player.get_name() + " hit a weak spot!")
				turn_count += 1
				enemy.set_already_attacked(True)
			enemy.set_current_health(enemy.get_current_health() - outcome['Damage'])
			status_changer(outcome['Status'], enemy)
			if enemy.get_current_health() <= 0:
				enemy.set_alive(False)
	elif choice == 2:
		turn_complete = skill_select(party, enemies)
	elif choice  == 3:
		turn_complete = switch(party, enemies, False)
	elif choice == 4 :
		for party_member in party:
			party_member.get_party_status()
	if turn_complete:
		turn_count -= 1


def skill_select(party, enemies):
	global turn_count
	player = party[active_member]
	print_battle_screen(party, enemies)
	skill_choice = player.list_out_skills()

	if skill_choice['choice'] == skill_choice['length']:
		player_choice(party, enemies)
		return False

	if player.get_attack_targets()[skill_choice['choice']] == 'friend': # for healing buffing moves
		enemy = party[ally_choice(party)]

	else:
		ec = enemy_choice(enemies)
		if ec > len(enemies):
			skill_select()
			return False
		enemy = enemies[ec-1]
	outcome = player.battle(enemy, skill_choice['choice'])
	player.set_current_health(player.get_current_health() - outcome['HP_Cost'])
	player.set_current_mp(player.get_current_health() - outcome['MP_Cost'])
	enemy.set_current_health(enemy.get_current_health() - outcome['Damage'])
	status_changer(outcome['Status'], enemy)
	if (outcome['Effectiveness'] != "Debuff" and (outcome['Effectiveness'] == "Critical" or outcome['Effectiveness'] > 1) and not enemy.get_already_attacked()):
		if outcome['Effectiveness'] == "Critical":
			print(player.get_name() + " got a critical hit!")
		elif outcome['Effectiveness'] > 1:
			print(player.get_name() + " hit a weak spot!")
		turn_count += 1
		enemy.set_already_attacked(True)
	if enemy.get_current_health() <= 0:
			enemy.set_alive(False)
	return True
	
def ally_choice(party):
	i = 1
	for player in party:
		print(str(i) + ".)")
		player.get_party_status()
		i += 1
	choice = int(input("What ally will you choose? "))
	choice -= 1
	if choice < 0 or choice > len(party):
		choice = ally_choice(party)
	return choice



def enemy_choice(enemies):
	i = 1
	for enemy in enemies:
		print(str(i) + ").", enemy.get_name() + "\tAlive:", str(enemy.is_alive()))
		i += 1
	print (str(i) + "). Back")
	choice = int(input("What enemy would you like to attack: "))
	if choice < 1 or choice > len(enemies) + 1:
		print("Invalid choice. Please try again.")
		return enemy_choice(enemies)
	if choice != len(enemies) + 1:
		if not enemies[choice - 1].is_alive():
			print("Invalid choice. Please try again.")
			return enemy_choice(enemies)
	return choice

def switch(party, enemies, required):
	global active_member
	player = party[active_member]
	left_counter = 1
	right_counter = 1
	left = party[(active_member - 1) % len(party)]
	right = party[(active_member + 1) % len(party)]
	while (not left.is_alive()):
		left = party[(active_member - left_counter) % len(party)]
		left_counter += 1

	while (not right.is_alive()):
		right = party[(active_member - right_counter) % len(party)]
		right_counter += 1

	print("1.) To Left:", left.get_name())
	print("2.) To Right:", right.get_name())
	if (not required): 
		print("3.) Back")
	choice = int(input("What would you like to do: "))
	if (not required): 
		while (choice != 1 and choice != 2 and choice != 3):
			print("Please input a correct response")
			print("1.) To Left:", left.get_name())
			print("2.) To Right:", right.get_name())
			print("3.) Back")
			choice = int(input("What would you like to do: "))
	else:
		while (choice != 1 and choice != 2):
			print("Please input a correct response")
			print("1.) To Left:", left.get_name())
			print("2.) To Right:", right.get_name())
			choice = int(input("What would you like to do: "))
	if choice == 1:
		active_member = (active_member - left_counter) % len(party)
	elif choice == 2:
		active_member(active_member - right_counter) % len(party)
	elif choice == 3:
		player_choice(party,enemies)
		return False
	return True



def status_changer(status_dict, enemy):
	for entry in status_dict:
		if enemy.get_status()['Normal'] == True:
			if entry == 'Paralyze':
				enemy_status = enemy.get_status()
				enemy_status['Paralyze'] = 3
				enemy_status['Normal'] = False
				enemy.set_status(enemy_status)
				print(enemy.get_name() + " has been paralyzed!")

			if entry == 'Poison':
				enemy_status = enemy.get_status()
				enemy_status['Poison'] = 3
				enemy_status['Normal'] = False
				enemy.set_status = enemy_status
				print(enemy.get_name() + " has been poisoned!")

		if entry == 'Attack':
			enemy_stats = enemy.get_stat_multiplier()
			enemy_stats['Attack'] = status_dict[entry]
			enemy.set_stat_multiplier(enemy_stats)
			enemy_status = enemy.get_status()
			enemy_status['Attack'] = 3
			enemy.set_status(enemy_status)
			print(enemy.get_name() + "'s attack has changed!")

		if entry == 'Defense':
			enemy_stats = enemy.get_stat_multiplier()
			enemy_stats['Defense'] = status_dict[entry]
			enemy.set_stat_multiplier(enemy_stats)
			enemy_status = enemy.get_status()
			enemy_status['Defense'] = 3
			enemy.set_status(enemy_status)
			print(enemy.get_name() + "'s defense has changed!")

		if entry == 'Magic Attack':
			enemy_stats = enemy.get_stat_multiplier()
			enemy_stats['Magic Attack'] = status_dict[entry]
			enemy.set_stat_multiplier(enemy_stats)
			enemy_status = enemy.get_status()
			enemy_status['Magic Attack'] = 3
			enemy.set_status(enemy_status)
			print(enemy.get_name() + "'s Magic Attack has changed!")

		if entry == 'Magic Defense':
			enemy_stats = enemy.get_stat_multiplier()
			enemy_stats['Magic Defense'] = status_dict[entry]
			enemy.set_stat_multiplier(enemy_stats)
			enemy_status = enemy.get_status()
			enemy_status['Magic Defense'] = 3
			enemy.set_status(enemy_status)
			print(enemy.get_name() + "'s Magic Defense has changed!")

		if entry == 'Skill':
			enemy_stats = enemy.get_stat_multiplier()
			enemy_stats['Skill'] = status_dict[entry]
			enemy.set_stat_multiplier(enemy_stats)
			enemy_status = enemy.get_status()
			enemy_status['Skill'] = 3
			enemy.set_status(enemy_status)
			print(enemy.get_name() + "'s skill has gone down!")
