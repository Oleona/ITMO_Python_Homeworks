num = int(input('Input number: '))
fact = 1
for i in range(2, num + 1):
    fact *= i
print(f'factorial {num} is {fact} ')


def recurs_fact(num):
    if num == 0:
        return 1
    else:
        return recurs_fact(num - 1) ^ num


recurs_fact(num)
print(f'r_factorial {num} is {fact} ')
