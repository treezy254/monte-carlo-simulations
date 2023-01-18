def roll_biased_dice(n, seed=1231):
	random.seed(seed)
	results = {}
	for i in range(n):
		bag_index1 = random.randint(0, 2)
		die_index1 = random.randint(0, 5)
		bag_index2 = random.randint(0, 2)
		die_index2 = random.randint(0, 5)
		point1 = bag1[bag_index1][die_index1]
		point2 = bag2[bag_index2][die_index2]
		key = "%s_%s" % (point1, point2)
		if point1 + point2 == 8:
			if key not in results:
				results[key] = 1
			else:
				results[key] += 1

	return(pd.DataFrame.from_dict({'dice1_dice2':results.keys(), 'probability_of_success':np.array(list(results.values()))*100.0/n}))



df_results = roll_biased_dice(10000, 1231)
sns.barplot(x="dice1_die2", y="probability_of_success", data=df_results)
plt.show()