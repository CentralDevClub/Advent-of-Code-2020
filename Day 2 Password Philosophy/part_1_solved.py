# Loading Data
with open('./input.txt') as file:
	array = file.readlines()
array = list(map(lambda x : x[:-1] , array))

policy, password = [], []
for i in array:
	pol = i.split(':')[0]
	pol = ' '.join(pol.split('-')).split()
	pas = i.split(':')[1]

	policy.append({'min':int(pol[0]),'max':int(pol[1]),'value':pol[2]})
	password.append(pas)

valid = []
for pol,pas in zip(policy,password):
	counter = 0

	# Linear scan
	for character in pas:
		if character == pol['value']:
			counter += 1

	# Check password validation
	if counter >= pol['min']:
		if counter <= pol['max']:
			valid.append(pas)

print(f'Terdapat total {len(array)} password')
print(f'Ditemukan {len(valid)} password valid')