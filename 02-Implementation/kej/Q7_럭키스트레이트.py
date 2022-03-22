arr = list(map(int, list(input())))
half = len(arr)//2

left = arr[0:half]
right = arr[half:]

if sum(left) == sum(right):
    print("Lucky")
else:
    print("Ready")
