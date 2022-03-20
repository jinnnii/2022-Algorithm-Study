import math

num = input()
count = 0
num_len = len(num)

for i in range(num_len-1):
  count += (i+1)*math.pow(10,i)*9

count += (int(num) - math.pow(10,num_len-1) +1) * num_len
print(int(count))