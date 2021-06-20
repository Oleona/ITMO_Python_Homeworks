from math import sqrt

a1 = (0, 0)
a2 = (1, 4)
a3 = (5, 6)
a4 = (7, 2)
a5 = (4, 0)


def triangle_side(a, b):
    side = sqrt((b[0] - a[0]) * (b[0] - a[0]) + (b[1] - a[1]) * (b[1] - a[1]))
    return side


def triangle_square(a, b, c):
    p = (a + b + c) / 2
    square = sqrt(p * (p - a) * (p - b) * (p - c))
    return square

firstside = triangle_side(a1, a2)
secondside = triangle_side(a2, a3)
thirdside = triangle_side(a3, a1)
print(firstside,secondside,thirdside)
fist_square = triangle_square(firstside, secondside, thirdside)
print(fist_square)

firstside =thirdside
secondside = triangle_side(a3, a4)
thirdside = triangle_side(a4, a1)
print(firstside,secondside,thirdside)
second_square=triangle_square(firstside, secondside, thirdside)
print(second_square)

firstside = thirdside
secondside = triangle_side(a4, a5)
thirdside = triangle_side(a5, a1)
print(firstside,secondside,thirdside)
third_square=triangle_square(firstside, secondside, thirdside)
print(third_square)

pentagon_square=fist_square+second_square+third_square
print(pentagon_square)