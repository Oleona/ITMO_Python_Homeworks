# Решить задачу не заглядывая в инет не смогла
def roman_to_arab(roman):
    matchlist = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                 (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    result = 0
    index = 0
    for arabnum, romannum in matchlist:
        while roman[index: index + len(romannum)] == romannum:
            result += arabnum
            index += len(romannum)
    print(result)
    return result


roman = input("Input roman number")
roman = roman.lstrip()
digit = roman_to_arab(roman)
print(digit)
