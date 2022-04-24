import itertools
# length = [int(input()) for _ in range(9)]
length = [20, 7, 23, 19, 10, 15, 25, 8, 13]
# combs = list(itertools.combinations(length, 7))

# for comb in combs:
#     if sum(comb) == 100:
#         print('\n'.join(map(str, sorted(list(comb)))))
#         break

combs = list(itertools.combinations(length, 2))

lsum = sum(length)
for comb in combs:
    if lsum - sum(comb) == 100:
        length.remove(comb[0])
        length.remove(comb[1])
        break
print('\n'.join(map(str, sorted(length))))
