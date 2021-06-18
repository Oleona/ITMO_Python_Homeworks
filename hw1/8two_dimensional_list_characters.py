el = []
array = []

for i in range((ord("А")), (ord("Я")) + 1):
    el.append(chr(i))
    array.append(''.join(el.copy()))
print(array)
for row in array:
    for elem in row:
        print(elem, end=' ')
    print()
