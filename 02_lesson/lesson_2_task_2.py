def is_year_leap(year):
    return year % 4 == 0

year = 2323 
result = is_year_leap(year)
print("Год " + str(year) + ": " + str(result))