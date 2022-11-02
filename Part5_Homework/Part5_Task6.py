word = []
for i in range(int(input("Enter count of words: "))):
    word.append(input("Enter {} word: ".format(i + 1)))

print(word)

my_string = ','.join([str(elem) for elem in word])

my_string = my_string.replace("right", "left")

print("Edited: ", my_string)
