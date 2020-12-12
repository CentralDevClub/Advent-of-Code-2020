# Loading Data
with open('./input.txt') as file:
	array = file.readlines()
array = list(map(lambda x: int(x[:-1]) if x[-1:] == '\n' else int(x), array))

high_to_low = array.copy()
high_to_low.sort(reverse=True)
low_to_high = sorted(array)

# Puzzle solving
stored = []
for high in high_to_low:
	for low in low_to_high:
		if high + low < 2020:
			for i in low_to_high:
				if high + low + i == 2020:
					kali = high*low*i
					if kali not in stored:
						print(f'Ketemu! {high} + {low} + {i} = {high+low+i}. Hasil kali = {kali}')
						stored.append(kali)
		elif high + low > 2020:
			break
