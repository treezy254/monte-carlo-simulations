import random
import numpy as np
import seaborn as sns
import matplotlib.pytplot as plt

nba_heights = [196, 191, 198, 216, 188, 185, 211, 201, 188, 191, 201, 208, 191, 183, 196]
simu_height = []

for i in range(1000):
	boostrap_sample = random.choices(nba_heights, k=15)
	simu_height.append(np.mean(boostrap_sample))
upper = np.quantile(simu_heights, 0.975)
lower = np.quantile(simu_heights, 0.025)
print([np.mean(simu_heights), lower, upper])

sns.displot(simu_heights)
plt.axvline(191.8, color='red')
plt.axvline(201.2, color="red")
plt.axvline(196.3, color="green")