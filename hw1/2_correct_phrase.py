name = input('Input name: ')
gender = input('Input gender: ')
age = int(input('Input age: '))
if gender == "male":
    print(f'Его зовут {name}.Ему {age} лет')
else:
    print(f'Её зовут {name}.Ей {age} лет')
