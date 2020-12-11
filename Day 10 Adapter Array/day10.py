with open('input.txt') as file:
    adapter = sorted([int(j.strip()) for j in file.readlines()]+[0])


# Part 1
jolts = {1: 0, 3: 1}
for i in range(1, len(adapter)):
    diff = adapter[i] - adapter[i-1]
    jolts[diff] += 1
print(jolts[1]*jolts[3])


# Part 2
adapter = adapter + [adapter[-1]+3]
total_combination = 1


def reduce(combination):
    global total_combination
    for i in range(1, len(combination)-1):
        reduced = combination.copy()
        diff_back = combination[i] - combination[i-1]
        diff_front = combination[i+1] - combination[i]
        if diff_back == 1 and diff_front == 1:
            reduced.remove(combination[i])
            total_combination += 1
            # print(total_combination)
            reduce(reduced)


# print(adapter)
reduce(adapter)
print(total_combination)
