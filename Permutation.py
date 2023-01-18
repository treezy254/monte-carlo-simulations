import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

us_heights = [165, 185, 179, 187, 193, 178, 180. 179, 171, 176, 169, 160, 140, 199, 176, 185, 175, 196, 190, 176]
nba_heights = [196, 191, 198, 216, 188, 185, 211, 201, 188, 191, 201, 208, 191, 183, 196]

all_heights = us_heights + nba_heights

simu_diff = []
for i in range(1000):
	perm_sample = np.random.permutation(all_heights)
	perm_nba, perm_adult = perm_sample[0:15], perm_sample[15:35]
	perm_diff = np.mean(perm_nba) - np.mean(perm_adult)
	simu_diff.append(perm_diff)

np.mean(nba_heights) - np.mean(us_heights)

upper = np.quantile(simu_diff, 0.975)
lower = np.quantile(simu_diff, 0.025)
print([lower, upper])


sns.displot(simu_diff)
plt.axvline(-10.03, color="red")
plt.axvline(10.03, color="red")
plt.axvline(18.32, color="green")