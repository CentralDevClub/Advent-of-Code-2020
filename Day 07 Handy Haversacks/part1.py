with open('input.txt') as f:
    file = f.readlines()
    file = map(lambda x : x[:-2],file)
    file = map(lambda x:x.split(' bags contain '), file)

rules = {}
for f in file:
    rules[f[0]] = list(map(lambda x: ' '.join(x.split(' ')[1:-1]),f[1:][0].split(', '))) if f[1:][0] != 'no other bags' else ['None']

def contain(color):
    if color == 'shiny gold':
        return True
    if color == 'None':
        return False
    for c in rules[color]:
        if contain(c):
            return True
    return False

hasShinyGold = 0
for color in filter(lambda x: x != 'shiny gold',list(rules)):
    if contain(color):
        hasShinyGold += 1

print(hasShinyGold)
