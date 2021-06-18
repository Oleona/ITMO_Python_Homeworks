import math

prime_numbers = []
user_num = int(input(" Input a number fo search  prime numbers: "))
for num in range(3, user_num + 1, 2):
    is_prime = True
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)
prime_numbers.insert(0, 2)
print(prime_numbers)
