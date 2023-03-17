# 01: Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(num):
    return [i for i in range(num, -1, -1)]

print(countdown(5))

# 02: Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def pnr(num_list):
    if type(num_list) != list:
        return f'Error: You need to pass a list of 2 numbers as an argument.'
    else:
        print(num_list[0])
        return num_list[1]

print(pnr([1, 2]))

# 03: First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def first_plus_length(lst):
    if type(lst) != list:
        return f'Error: You need to pass a list of numbers as an argument.'
    else:
        return lst[0] + len(lst)

print(first_plus_length([1, 2, 3, 4, 5]))

# 04: Values Greater Than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False.

def values_greater_than_second(num_list):
    if type(num_list) != list:
        return f'Error: You need to pass a list of numbers as an argument.'
    elif len(num_list) < 2:
        return False
    else:
        new_list = [i for i in num_list if i > num_list[1]]
        print(len(new_list))
        return new_list

print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([3]))

#05: This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def length_and_value(size, val):
    return [val for i in range(size)]

print(length_and_value(4, 7))
print(length_and_value(6, 2))