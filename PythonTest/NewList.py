def century_from_year(year):

    if (year <= 0):
        print("0 and negative is not allow for a year")

    elif (year <= 100):
        print("1st century")
    elif (year % 100 == 0):
        print(year // 100)
    else:
        print(year // 100 + 1)


century_from_year(2005)
century_from_year(1950)
century_from_year(1900)
