# var1 = lambda var: var * 2
# ret = lambda var: var * 3
# result = 2
# result1 = var1(result)
# result2 = ret(result1)
# result3 = var1(result2)
# print(result3)

# var1 = True
# var2 = False
# var3 = False
#
# # if var1 or var2 and var3:
# #  print("True")
# # else:
# #  print("False")
#
# ints = set([1,1,2,3,3,3,4])
# print(len(ints))

# def test1(param):
#  return str(param)
#
# def test2(param):
#  return str(2 * param)
#
# result = test1(1) + test2(2)
# print(result)
#
# for i in range(1,6):
#     print(str(i)* 5)
#
# print(int('0'))

# try:
#  if '1' != 1:
#   raise "firstError"
#  else:
#   print("firstError has not occured")
# except "firstError":
#  print("firstError has occured")

# def myfunc():
#  try:
#   print('Monday')
#  finally:
#   print('Tuesday')
# myfunc()
#
# def test1(param):
#  return param
#
# def test2(param):
#  return param * 2
#
# def test3(param):
#  return param + 3
#
# result = test1(test2(test3(1)))
# print(result)
#
# var1 = 4.5
# var2 = 2
# print(var1//var2)
#
# import random
# mylist = [10, 20, 30]
# random.shuffle(mylist)
# print(mylist)

testArr = [11, 22, 33, 35, 11]
result = testArr[0]
for iter in testArr:
 if iter > result:
  result = iter

print(result)

# mylist=['abc','cde','abcde','efg']
# print(max(mylist))
#
# mylist=['a', 'aa', 'aaa', 'b', 'bb', 'bbb']
# print(mylist[:-1])

# class Ubuntu: #create instance oof the class!
#  def __init__(self, ramsize):
#   self.ram = ramsize
#   self.type = 'server'
# ubuntu = Ubuntu(2000)
#
# print(list("hello"))

mylist=['a', 'aa', 'aaa', 'b', 'bb', 'bbb']
print(mylist[int(-1/2)])

def test():
 try:
  return 1
 finally:
  return
result = test()
print(result)

import random
print(random.seed(3))
