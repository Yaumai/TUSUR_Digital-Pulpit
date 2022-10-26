print("Enter your mat height size(should be %number% mod 2 != 0):")

height = int(input())
width = height * 3

print("Enter your welcome text:")
text = str(input())

for stick_count in range(1, height, 2):
    print(('.|.' * stick_count).center(width, '-'))

print('{0}'.center(width, '-').format(text))

for stick_count in range(height - 2, 0, -2):
    print(('.|.' * stick_count).center(width, '-'))
