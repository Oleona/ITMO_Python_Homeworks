unique = []
for i in range(1023, 9876):
    s = str(i)
    if (s[0] != s[1] and s[0] != s[2] and s[0] != s[3]) and (s[1] != s[2] and s[1] != s[3]) and (s[2] != s[3]):
        unique.append(int(s))
print(unique)

uniq_numbers = []
for i in range(1023, 9876):
    uniq = set(str(i))
    if len(uniq) == 4:
        num=int(str(i))
        uniq_numbers.append(num)

print(uniq_numbers)
