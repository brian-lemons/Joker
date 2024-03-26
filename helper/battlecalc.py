import math

def calculate_battle(defenders_bonus, defenders_ships, attackers_weapons, attackers_ships, defenders_weapons):
  #Calculate Defenders Bonus
  
  if defenders_bonus == True:
    defenders_weapons += 1
    defenders_bonus_text = "Yes"
  else:
    defenders_bonus_text = "No"

  #Set minimum hits needed to destory all of the opposing ships
  attacker_min_hits = math.ceil(defenders_ships / attackers_weapons)
  defenders_min_hits = math.ceil(attackers_ships / defenders_weapons)

  #Calculate attacking and defending ships lost
  if attacker_min_hits > defenders_min_hits or attacker_min_hits == defenders_min_hits and defenders_bonus == True:
    defenders_ships_lost = (defenders_min_hits - 1) * attackers_weapons
    attacker_ships_lost = defenders_min_hits * defenders_weapons
  else:
    defenders_ships_lost = attacker_min_hits * attackers_weapons
    attacker_ships_lost = attacker_min_hits * defenders_weapons

  #Calculate who wins combat
  if attacker_ships_lost > attackers_ships:
    attacking_ships_remaining = 0
  else:
    attacking_ships_remaining = attackers_ships - attacker_ships_lost

  if defenders_ships_lost > defenders_ships:
    defending_ships_remaining = 0
  else:
    defending_ships_remaining = defenders_ships - defenders_ships_lost

  if attacking_ships_remaining > defending_ships_remaining:
    who_won = "Attacker"
  else:
    who_won = "Defender"

  if attacking_ships_remaining == defending_ships_remaining:
    who_won = "No One"
    attacking_ships_remaining = 0
    defending_ships_remaining = 0