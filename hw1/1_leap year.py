def is_leap(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        print("The year is NOT leap")
    else:
        print("The year is leap year")


user_year = input('Input the year to check: ')

while not user_year.isdigit():
    print("Not a number entered")
    year = input("Input the year to check:  ")
year = int(user_year)
is_leap(year)
