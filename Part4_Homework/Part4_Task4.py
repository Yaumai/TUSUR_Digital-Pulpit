x = int(input())
x1 = x
x2 = 0

flag = 0

# инвертирование битов если отрицательное
if (x < 0):
    x1 = ~x1 + 1
    flag = 1

while x1 > 0:
    a = x1 % 10
    x1 = x1 // 10
    x2 = x2 * 10
    x2 = x2 + a

if (flag == 1):
    print(x, "->", ~x2 + 1)

else:
    print(x, "->", x2)
