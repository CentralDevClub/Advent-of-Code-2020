## :thinking: Penyelesaian
### Part 1
Menggunakan `file.readline()` untuk melakukan iterasi pada setiap baris input. line x 32 karena untuk mengextend index sesuai dengan pola yang sama. Dengan posisi += 3 maka dapat dilakukan pengecekan apakah karakter dari posisi tersebut adalah pohon atau ruang.

```python
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
```

Output :
```
Banyak pohon yang dilewati : 184 
Banyak ruang yang dilewati : 138
```

### Part 2
Dilakukan nested loop terhadap slopes dan iterasi baris per baris dari input. file.readline() akan diulangi sesuai dengan slope y untuk melompati baris input, dan slope x adalah posisi atau index dari satu baris. 1 baris dikalikan dengan rumus `322//(32/slope x) + 1` dimana 322 adalah jumlah baris input dan 32 adalah panjang 1 pola dalam 1 baris. Mengingat panjang slope x yang berbeda beda maka dilakukan rumus tersebut untuk mengurangi penggunaan resource.

```python
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
```

Output :
```
Slope : (1, 1)
Iterasi : 322
Banyak pohon yang dilewati : 62 
Banyak ruang yang dilewati : 260 

Slope : (3, 1)
Iterasi : 322
Banyak pohon yang dilewati : 184 
Banyak ruang yang dilewati : 138 

Slope : (5, 1)
Iterasi : 322
Banyak pohon yang dilewati : 80 
Banyak ruang yang dilewati : 242 

Slope : (7, 1)
Iterasi : 322
Banyak pohon yang dilewati : 74 
Banyak ruang yang dilewati : 248 

Slope : (1, 2)
Iterasi : 161
Banyak pohon yang dilewati : 36 
Banyak ruang yang dilewati : 125 

Hasil Perkalian : 2431272960
```
