sentence = input("Enter your sentence: ")
word = ""

for i in sentence:
    if i.isupper():
        word += i

print(word)
