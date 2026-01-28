year = int(input("Enter a year: "))

while not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
    print("Invalid year. Try again.")
    year = int(input("Enter a year: "))

print("Valid leap year:", year)






