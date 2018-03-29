list = []
num = int(input('How many numbers you want to enter?: '))
# try:
for n in range(num):
    numbers = int(input('Enter number of your choice: '))
    list.append(numbers)
        # continue
avg = sum(list)//len(list)
print("Results are below:")
print("Maximum element in the list is: ", max(list))
print("Minimum element in the list is: ", min(list))
print("The total of all the numbers enterd is: ", sum(list))
print("The average of all numbers entered is: ", avg)
        # continue
# except:
#     print("Please enter valid input!!")
