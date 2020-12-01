# Loading Data
with open('./input.txt') as file:
	array = file.readlines()

array = list(map(lambda x : int(x[:-1]),array))
high_to_low = array.copy()
high_to_low.sort(reverse=True)
low_to_high = sorted(array)

# Puzzle solving
for high in high_to_low:
	for low in low_to_high:
		if high + low == 2020:
			print(f'Ketemu {high+low} = {high} + {low}')
			print(f'Hasil perkalian = {high*low}')
		elif high + low > 2020:
			break