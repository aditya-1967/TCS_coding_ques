#Check if given year is leap year or not
year = int(input('Enter year: '))
if year % 100 == 0 and year % 400 == 0 or year % 4 == 0:
    print('True')
else:
    print('False')
