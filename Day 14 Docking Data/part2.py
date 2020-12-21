import fileinput
import re

def indices(newidx, floating):
	if len(floating) == 0:
		return [newidx]
	else:
		b0 = floating.pop(0)
		ans = indices(newidx, list(floating)) + indices(newidx+2**b0, list(floating))
		return ans

mask = ''
mem = {}
lines = list(fileinput.input('input.txt'))
for line in lines:
	line = line.strip()
	if line.startswith('mask'):
		newmask = line.split()[-1]
		mask = newmask
	else:
		assert len(mask) == 36
		idx, _, value = line.split()
		idx = int(idx.split('[')[-1][:-1])
		value = int(value)
		newidx = 0
		floating = []
		for i, bit in enumerate(reversed(mask)):
			ibit = idx & (2**i)
			if bit == 'X':
				floating.append(i)
			elif bit == '1':
				newidx += 2**i
			elif bit == '0':
				newidx += ibit
				pass
			else:
				assert False
		for idx2 in indices(newidx, list(floating)):
			mem[idx2] = value

ans = 0
for k,v in mem.items():
	ans += v
print(ans)