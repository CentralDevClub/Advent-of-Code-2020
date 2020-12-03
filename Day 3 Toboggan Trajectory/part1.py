position = 0
trees = 0
space = 0

with open('input.txt') as file:
    # Skip 1st line
    line = file.readline()[:-1]
    line = file.readline()[:-1]

    while line:
        line *= 32
        position += 3
        if line[position] == '#':
            trees += 1
        elif line[position] == '.':
            space += 1
        line = file.readline()[:-1]

print(f'Banyak pohon yang dilewati : {trees} \nBanyak ruang yang dilewati : {space}')
