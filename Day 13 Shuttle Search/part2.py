with open('input.txt') as file:
	raw_ports = [int(i) if i != 'x' else i for i in [i.strip() for i in file.readlines()][1].split(',')]



rules = {port:-index % port for index,port in enumerate(raw_ports) if port != 'x'}
ports = sorted(list(rules.copy()),reverse=True)
pos_now = rules[ports[0]]
port_now = ports[0]

for port in ports[1:]:
	while pos_now % port != rules[port]:
		pos_now += port_now
	port_now *= port

print(pos_now)