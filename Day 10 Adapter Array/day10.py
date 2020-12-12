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
DP = {}


def dp(i):
    if i == len(adapter)-1:
        return 1
    if i in DP:
        return DP[i]
    ans = 0
    for j in range(i+1, len(adapter)):
        if adapter[j] - adapter[i] <= 3:
            ans += dp(j)
    DP[i] = ans
    return ans


print(dp(0))
