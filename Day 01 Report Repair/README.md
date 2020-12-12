## :thinking: Penyelesaian
### Part 1

Pertama loading file txt menjadi array, kemudian dilakukan copy array sehingga memiliki dua array. Array pertama dilakukan sorting asceding sedangkan array kedua dilakukan sorting descending. Setelah itu dilakukan nested looping terhadap array descending, didalamnya terdapat looping array ascending.
Dilakukan pengecekan jika nilai pertama yang berasal dari array descending ditambah nilai kedua yang berasal dari array ascending berjumlah 2020, maka angka tersebut dikalikan dan di print hasilnya. Jika jumlah kedua angka tersebut berjumlah lebih dari 2020, maka looping akan di break.
Tujuan dari sorting array dan melakukan break jika angka lebih dari 2020 adalah untuk mengurangi jumlah iterasi yang diperlukan dalam menyelesaikan masalah tersebut.

```python
# Loading Data
with open('./input.txt') as file:
	array = file.readlines()
array = list(map(lambda x: int(x[:-1]) if x[-1:] == '\n' else int(x), array))

high_to_low = array.copy()
high_to_low.sort(reverse=True)
low_to_high = sorted(array)

# Puzzle solving
solved = []
for high in high_to_low:
	for low in low_to_high:
		if high + low == 2020:
			if high*low not in solved:
				solved.append(high*low)
				print(f'Ketemu {high+low} = {high} + {low}')
				print(f'Hasil perkalian = {high*low}')
		elif high + low > 2020:
			break
```

Output :

```
Ketemu 2020 = 1228 + 792
Hasil perkalian = 972576
```

### Part 2

Pertama loading file txt menjadi array, kemudian dilakukan copy array sehingga memiliki dua array. Array pertama dilakukan sorting asceding sedangkan array kedua dilakukan sorting descending. Setelah itu dilakukan nested looping 3 tingkat terhadap array descending, didalamnya terdapat looping array ascending, dan didalamnya terdapat looping lagi terhadap array ascending.
Pada looping tingkat kedua, dilakukan pengecekan jika nilai pertama yang berasal dari array descending ditambah nilai kedua yang berasal dari array ascending kurang dari 2020, maka akan diteruskan dengan looping tingkat ketiga. 
Pada looping tingkat ketiga yaitu looping terhadap array ascending, diakukan pengecekan bertingkat. Jika jumlah ketiga nilai iterasi sama dengan 2020, maka angka akan dikalikan dan dimasukan ke dalam array solved yang kosong.

```python
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
```

Output :

```
Ketemu! 1030 + 268 + 722 = 2020. Hasil kali = 199300880
```
