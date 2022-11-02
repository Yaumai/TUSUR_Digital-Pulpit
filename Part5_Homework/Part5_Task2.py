x = int(input("Enter your number (x > 0): "))

if x % 2 != 0:
    print("Bad")

elif (2 <= x <= 5) and x % 2 == 0:
    print("Not bad")

elif (6 <= x <= 20) and x % 2 == 0:
    print("So-so")

elif (x > 20) and x % 2 == 0:
    print("Excellent")
