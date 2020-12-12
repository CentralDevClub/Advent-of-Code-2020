slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
perkalian_pohon = 1

for slope in slopes:
    position = 0
    trees = 0
    space = 0
    with open('input.txt') as file:
        # Skip 1st line
        line = file.readline()[:-1]
        for i in range(slope[1]):
            line = file.readline()[:-1]
        iterasi = 0
        while line:
            iterasi += 1
            line *= 322//(31//slope[0]) + 1
            position += slope[0]
            if line[position] == '#':
                trees += 1
            elif line[position] == '.':
                space += 1
            for i in range(slope[1]):
                line = file.readline()[:-1]

    perkalian_pohon *= trees
    print(f'Slope : {slope}')
    print(f'Iterasi : {iterasi}')
    print(f'Banyak pohon yang dilewati : {trees} \nBanyak ruang yang dilewati : {space} \n')

print(f'Hasil Perkalian : {perkalian_pohon}')
