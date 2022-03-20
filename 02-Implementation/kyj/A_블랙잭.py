import itertools 

n,m = map(int,input().split())
card = list(map(int,input().split()))

combi = list(map(sum,itertools.combinations(card,3)))
combi.sort()
idx = combi.count(m)

if idx > 0:
    print(m)
else:
    combi.append(m)
    combi.sort()
    idx1 = combi.index(m)
    print(combi[idx1-1])



#####
from itertools import conbinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
biggest_num = 0

for card in combinations(cards,3):
	tmp_sum = sum(card)
	if biggest_sum < tmp_sum <= m:
		biggest_sum = tmp_sum

print(biggest_sum)