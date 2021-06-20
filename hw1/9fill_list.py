
n = 5
m = 4
x = 1
y = 1
arr = [[x * y for x in range(1, m+1)] for y in range(1, n+1)]
for row in arr:
    for elem in row:
        print(elem, end='  ')
    print()
print(arr)
