word = input("Enter your sentence: ")

flag = 0
for i in word.split() :
    if i.isalpha() :
        flag += 1
        if flag == 3 :
            print("True")
    else :
        flag = 0

if (flag < 3):
    print("False")
