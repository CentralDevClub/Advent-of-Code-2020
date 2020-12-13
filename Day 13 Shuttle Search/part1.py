with open('input.txt') as file:
	port = [i.strip() for i in file.readlines()]
	bus_id = int(port[0])
	port = [int(i) for i in list(filter(lambda x: True if x != 'x' else False, port[1].split(',')))]

print(f'Bus ID : {bus_id}')

min_value = 0
min_id = 0
def generate(step,limit):
	global min_value, min_id
	value = limit % step
	value = limit - value
	value = value + step
	if min_value == 0:
		min_value = value
	elif value < min_value:
		min_value = value
		min_id = step
	print(f'Bus: {step}, timestamp : {value}')

for i in port:
	generate(i,bus_id)

print(min_value,min_id, min_value-bus_id, (min_value-bus_id)*min_id)