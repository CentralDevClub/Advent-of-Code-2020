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
