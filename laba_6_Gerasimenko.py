#1
def is_year_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
test_d = [1900, 2000, 2016, 1987]
test_r = [False, True, True, False]

for i in range(len(test_d)):
    yr = test_d[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_r[i]:
        print("OK")
    else:
        print("Failed")
#2
def is_year_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def days_m(year, month):
    if month < 1 or month > 12:
        return None
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year):
        return 29

    return days_per_month[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_m(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
#3
def is_year_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_year_leap(year):
        return 29
    return days_per_month[month - 1]
def day_of_year(year, month, day):
    if month < 1 or month > 12 or day < 1:
        return None
    days_in_current_month = days_in_month(year, month)
    if day > days_in_current_month:
        return None
    day_of_year = sum(days_m(year, m) for m in range(1, month)) + day
    return day_of_year
test_cases = [
    (2000, 12, 31, 366),
    (2023, 1, 15, 15),
    (1998, 5, 25, 145),
    (2022, 2, 29, None),
    (2021, 13, 1, None),
    (2024, 4, 31, None)
]
for year, month, day, expected_result in test_cases:
    result = day_of_year(year, month, day)
    if result == expected_result:
        print(f"{year}-{month:02d}-{day:02d} -> {result} (OK)")
    else:
        print(f"{year}-{month:02d}-{day:02d} -> {result} (Failed)")
#4
def is_prime (num):
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        if num == 2 or num == 3 or num == 5 or num == 7:
            return True
        else:
            return False
    else:
        return True

for i in range(1, 20):
  if is_prime(i + 1):
          print(i + 1, end=" ")
print()
#5
def liters_100km_to_miles_gallon(liters):
    miles_per_gallon = 100 / (liters * 0.621371 / 3.785411784)
    return miles_per_gallon
def miles_gallon_to_liters_100km(miles):
    liters_per_100km = 1 / (miles / 0.621371 * 0.264172) * 100
    return liters_per_100km
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
#6
def is_a_triangle(a, b, c):
    return (a + b > c) and (b + c > a) and (a + c > b)
print(is_a_triangle(3, 4, 5))
print(is_a_triangle(1, 1, 3))
#7
def is_a_triangle(a, b, c):
    return (a + b > c) and (b + c > a) and (a + c > b)
def is_a_right_triangle(a, b, c):
    if is_a_triangle(a, b, c):
        return a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2
    else:
        return False
print(is_a_right_triangle(3, 4, 5))
print(is_a_right_triangle(1, 1, 3))