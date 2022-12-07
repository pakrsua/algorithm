# 1475 방 번호
import math

num = list(input())
sets = {}

for n in num:
    if n in sets:
        if n == '9' or n == '6':
            sets['6'] += 1
            sets['9'] += 1
        else:
            sets[n] += 1
    else:
        if n == '9' or n == '6':
            sets['9'] = 1
            sets['6'] = 1
        else:
            sets[n] = 1

if '6' in sets:
    sets['6'] = math.ceil(sets['6']/2)
if '9' in sets:
    sets['9'] = math.ceil(sets['9']/2)

print(max(sets.values()))
# print(sets)