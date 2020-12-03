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
