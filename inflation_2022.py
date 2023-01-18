# Deterministic
def deterministic_inflation(year, yearly_increase_percent):
	inflation_rate = 8.6
	inflation_rate = inflation_rate*((100 + yearly_increase_percent)/100)**(year-2022)
	return (inflation_rate)

# Stochastic
def monte_carlo_inflation(year, seed):
	random.seed(seed)
	inflation_rate = 8.6
	yearly_increase = random.randint(1, 3)
	for i in range(year - 2022):
		inflation_rate = inflation_rate*((100 + yearly_increase)/100)
		return(inflation_rate)

rates_1 = []
for i in range(1000):
	seed = random.randint(0, 20000)
	rates_1.append(monte_carlo_inflation(2050, seed))
	print(np.mean(rates_1))