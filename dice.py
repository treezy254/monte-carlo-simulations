import random
import numpy as np

def roll_dice(n, seed):
	random.seed(seed)
	total_dice = 0
	point_dice = []
	for i in range(n):
		total_dice += 1
		point_dice.append(random.randint(1, 6))
	mean_point_dice = np.mean(point_dice)
	return([total_dice, mean_point_dice])