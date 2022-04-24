# s = list(input())
# is_str = ''
# sum = 0

# for i in s:
#     if i.isnumeric():
#         sum += int(i)
#     else:
#         is_str += i
# print(''.join(sorted(is_str))+str(sum))

for step in range(1, 10):
    for i in range(step, 10, step):
        print(i)
