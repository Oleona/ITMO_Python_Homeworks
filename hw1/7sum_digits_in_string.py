user_str = "Пр4о6г ра7м0му7д31ля по60132дсч9ет а21об87ще9й"  # input('Введите строку из цифр и букв без знаков препинания: ')
user_str = user_str.replace(" ", "")
print(user_str)
while not user_str.isalnum():
    print("Введена строка неправильного формата")
    user_str = input('Введите строку из цифр и букв без знаков препинания: ')

counter = []
sum = 0
for char in user_str:
    if char.isdigit():
        counter.append(char)
for num in counter:
    num = int(num)
    sum += num
print(counter)
print(sum)
