#list comprehension-allows the program to run very fast
# l = [1,2,3,4]
#
# result = [i*5 for i in l]
# print(result)
#
# result1 = [x for x in range(21) if x%2==0 ]
# print(result1)
#
# result2 = [x for x in range(21) if x%2==0 if x%5==0 ]
# print(result2)
#
# result3 = ["even" if i%2==0 else "odd" for i in range(11) ]
# print(result3)

mylist=[x*y for x in range(20,40,60) for y in range(2,4,6)]
print(mylist)


# Dictionary comprehension: dict([expression for --- in ---])

# x = dict {(i,char(65+i)) for i in range(10)}
# print(x)

# dic = {'a':1 , 'b':2 , 'c':3}
# print(dic.keys())
# print(dic.values())
