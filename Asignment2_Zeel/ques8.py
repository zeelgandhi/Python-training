# num_one = 0
# num_two = 1
# count = 0
# n_terms = 10
#
#
# if n_terms <= 0:
#     print("pls enter positive int")
# elif n_terms == 1:
#     print("Fibonacci series upto", n_terms)
#     print(num_one)
# else:
#     print("Fibonacci seris upto", n_terms)
#     while count < n_terms:
#         print(num_one, end= None)
#         nth_term = num_one + num_two
#         num_one = num_two = nth_term
#         count += 1

number = int(input("Please enter the range of number: "))
first_val = 0
sec_val = 1

for num in range(0, number):
    if (num <= 1):
        next = num
    else:
        next = first_val + sec_val
        first_val = sec_val
        sec_val = next
    print(next)
