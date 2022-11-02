x = int(input("Enter your number(int):"))

if (x % 3 == 0 and x % 5 == 0):
    print("Fizz Buzz")

elif (x % 3 == 0):
    print("Fizz")

elif (x % 5 == 0):
    print("Buzz")

else:
    print(x)
