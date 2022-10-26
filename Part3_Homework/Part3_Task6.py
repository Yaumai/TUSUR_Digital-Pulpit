num = int(input("Enter your number:"))
mult = 1

while (num != 0):
    mult = mult * (num % 10)
    num = num // 10
print("Result:", mult)