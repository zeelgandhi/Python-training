str1= input("Enter the first string: ")
str2 = input("Enter the second string: ")

s = list(set(str1)&set(str2))


if len(s) <= 0:
    print("There are no common charcters!")
else:
    print("The common charcaters are: ")

    for i in s:
        print(i)

#I just tried to add some comments if there are no common characters
#so there is some more code to this!! Thanks
