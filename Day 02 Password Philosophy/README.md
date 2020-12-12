## :thinking: Penyelesaian
### Part 1
Pertama data dibaca setiap baris dan dirposes menjadi bentuk dictionary atau object. Kemudian dilakuan iterasi. Dilakukan linear scan untuk setiap password untuk menghitung jumlah karakter ke dalam variabel counter. Jika jumlahnya memenuhi kriteria, maka password tersebut valid.
```python
# Loading Data
with open('./input.txt') as file:
	array = file.readlines()
array = list(map(lambda x: x[:-1] if x[-1:] == '\n' else x, array))


def process(arr):
	a = []
	for r in arr:
		pol = r.split(':')[0]
		pol = ' '.join(pol.split('-')).split()
		pas = r.split(':')[1][1:]
		a.append({'min': int(pol[0]), 'max': int(pol[1]), 'value': pol[2], 'password': pas})
	return a


array = process(array)
valid = []
for i in array:
	counter = 0
	# Linear scan
	for character in i['password']:
		if character == i['value']:
			counter += 1

	# Check password validation
	if counter >= i['min']:
		if counter <= i['max']:
			valid.append(i['password'])

print(f'Terdapat total {len(array)} password')
print(f'Ditemukan {len(valid)} password valid')
```
Output :
```
Terdapat total 1000 password
Ditemukan 660 password valid
```

### Part 2
Pertama data dibaca setiap baris dan dirposes menjadi bentuk dictionary atau object. Kemudian dilakuan iterasi. Dilakukan pengecekan menggunakan XOR logic untuk dua posisi atau index password. Jika outputnya True, maka password tersebut valid.

```python
# Loading Data
with open('./input.txt') as file:
    array = file.readlines()
array = list(map(lambda x: x[:-1] if x[-1:] == '\n' else x, array))


def process(arr):
    a = []
    for r in arr:
        pol = r.split(':')[0]
        pol = ' '.join(pol.split('-')).split()
        pas = r.split(':')[1][1:]
        a.append({'first': int(pol[0]), 'second': int(pol[1]), 'value': pol[2], 'password': pas})
    return a


array = process(array)
valid_password = 0
for i in array:
    if (i['password'][i['first']-1] == i['value']) ^ (i['password'][i['second']-1] == i['value']):
        valid_password += 1

print(f'Terdapat total {len(array)} password')
print(f'Ditemukan {valid_password} password valid')
```

Output :
```
Terdapat total 1000 password
Ditemukan 530 password valid
```
