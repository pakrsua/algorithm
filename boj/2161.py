# 2161 카드

n = int(input())
card = []

for i in range(1, n+1):
    card.append(i)
while len(card) > 1:
    print(card[0],end=' ')
    card.pop(0)
    card.append(card[0])
    card.pop(0)
print(card[0])