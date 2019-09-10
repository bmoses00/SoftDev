import random

def randName(dict):
	teamNum = random.randint(0, len(dict) - 1)
	return teamNum

print randName({"orpheus": [1, 2, 3], "rex": [4, 5, 6]})
