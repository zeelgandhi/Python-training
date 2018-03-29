def odd_value(n):
    for x in n:
        if x%2 != 0:
            yield x
result  = odd_value(range(10))
for y in result:
    if result.__next__() == 3:
        print(result.__next__())
