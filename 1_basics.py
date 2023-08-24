"""
- create list of 100 random numbers from 0 to 1000
- sort list from min to max (without using sort())
- calculate average for even and odd numbers
- print both average result in console

Each line of code should be commented with description.
"""
# import library
import random

# create list of 100 random numbers from 0 to 1000
# starting from empty list
rand_list = []

# in a loop from 0 to 99 (100 elements)
for i in range(100):
    # define a random number from 0 to 1000
    n = random.randint(0, 1000)
    # add this number to the list
    rand_list.append(n)
print(rand_list)


# sort list from min to max (without using sort())
# use quicksort algorithm to swap pairs
for i in range(len(rand_list)):
    for j in range(i + 1, len(rand_list)):
        if rand_list[i] > rand_list[j]:
            rand_list[i], rand_list[j] = rand_list[j], rand_list[i]
print(rand_list)


# calculate average for even and odd numbers
# create helper parameters
even_sum = 0
even_amount = 0

odd_sum = 0
odd_amount = 0

# go through all elements of rand_list created above
for i in rand_list:
    # if element is even sum up values into even_sum and increase count of even_amount
    if i % 2 == 0:
        even_sum += i
        even_amount += 1
    # if element is odd sum up values into odd_sum and increase count of odd_amount
    if i % 2 == 1:
        odd_sum += i
        odd_amount += 1

# avoid devision by 0 and check amounts first
if even_amount == 0:
    print(f'even_avg: 0')
else:
    print(f'even_avg: {even_sum/even_amount}')

if odd_amount == 0:
    print(f'odd_avg: 0')
else:
    print(f'odd_avg: {odd_sum/odd_amount}')


