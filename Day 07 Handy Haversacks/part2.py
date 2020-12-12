with open('input.txt') as f:
    file = f.readlines()
    file = map(lambda x : x[:-2],file)
    file = list(map(lambda x:x.split(' bags contain '), file))

rules = {}
for f in file:
    contains = [i.split(', ') for i in f[1:]][0]
    contains = [' '.join(i.split()[:-1]) for i in contains]
    rules[f[0]] = {' '.join(i.split()[1:]):i.split()[0] for i in contains}

print(rules)

def contain(color):
    total = 1
    for c,jml in color.items():
        if list(color.values())[0] == 'no':
            return 1
        total += int(jml) * contain(rules[c])
    return total


print(contain(rules['shiny gold'])-1)
