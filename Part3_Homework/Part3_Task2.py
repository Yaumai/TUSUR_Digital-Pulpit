print("Enter figure's thickness(should be %number% mod 3 = 0)")
thickness = int(input())

print("Enter figure's marker")
marker = str(input())

# Top Cone
for i in range(thickness):
    print((marker * i).rjust(thickness - 1) + marker + (marker * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((marker * thickness).center(thickness * 2) + (marker * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((marker * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((marker * thickness).center(thickness * 2) + (marker * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(((marker * (thickness - i - 1)).rjust(thickness) + marker + (marker * (thickness - i - 1)).ljust(
        thickness)).rjust(
        thickness * 6))
