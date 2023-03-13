num1 = 42                           # variable declaration, number (integer)
num2 = 2.3                          # variable declaration, number (float)
boolean = True                      # variable declaration, Boolean
string = 'Hello World'              # variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana')     # variable declaration, initialize tuple
print(type(fruit))                  # log statement, type check, tuple
print(pizza_toppings[1])            # log statement, access value (by index number), list
pizza_toppings.append('Mushrooms')  # add value, list
print(person['name'])               # log statement, access value (by key), dictionary
person['name'] = 'George'           # change value (by key), dictionary
person['eye_color'] = 'blue'        # add value (by key: index), dictionary
print(fruit[2])                     # log statement, access value (by index number), tuple

if num1 > 45:                       # conditional, if
    print("It's greater")           # log statement, string
else:                               # conditional, else
    print("It's lower")             # log statement, string

if len(string) < 5:                 # conditional, if, length check
    print("It's a short word!")     # log statement, string
elif len(string) > 15:              # conditional, else if, length check
    print("It's a long word!")      # log statement, string
else:                               # conditional, else
    print("Just right!")            # log statement, string

for x in range(5):                  # for loop, sequence, initialize variable (number, integer)
    print(x)                        # log statement, variable (number, integer)
for x in range(2,5):                # for loop, sequence (start, stop), initialize variable (number, integer)
    print(x)                        # log statement, variable (number, integer)
for x in range(2,10,3):             # for loop, sequence (start, stop, increment), initialize variable (number, integer)
    print(x)                        # log statement, variable (number, integer)
x = 0                               # initialize variable, number (integer)
while(x < 5):                       # while loop, start, stop
    print(x)                        # log statement, variable (number, integer)
    x += 1                          # increment variable (integer)

pizza_toppings.pop()                # delete value, list
pizza_toppings.pop(1)               # delete value, list (by index number)

print(person)                       # log statement, variable (dictionary)
person.pop('eye_color')             # delete value, dictionary (by key)
print(person)                       # log statement, variable (dictionary)

for topping in pizza_toppings:      # for loop, sequence, initialize variable (string)
    if topping == 'Pepperoni':      # conditional, if
        continue                    # for loop, continue
    print('After 1st if statement') # log statement, string
    if topping == 'Olives':         # conditional, if
        break                       # for loop, break

def print_hello_ten_times():        # function declaration
    for num in range(10):           # for loop, sequence, initialize variable (number, integer)
        print('Hello')              # log statement, string

print_hello_ten_times()             # function, return

def print_hello_x_times(x):         # function declaration, parameter
    for num in range(x):            # for loop, sequence (parameter)
        print('Hello')              # log statement, string

print_hello_x_times(4)              # function, return, argument (number, integer)

def print_hello_x_or_ten_times(x = 10): # function declaration, initialize parameter, argument (number, integer)
    for num in range(x):                # for loop, sequence (parameter)
        print('Hello')                  # log statement, string

print_hello_x_or_ten_times()            # function, return, default argument (number, integer)
print_hello_x_or_ten_times(4)           # function, return, argument (number, integer)


# Bonus section

# print(num3)                           # NameError: name <variable name> is not defined
# num3 = 72                             # variable declaration, number (integer)
# fruit[0] = 'cranberry'                # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])        # KeyError: 'favorite_team'
# print(pizza_toppings[7])              # IndexError: list index out of range
#   print(boolean)                      # IndentationError: unexpected indent
# fruit.append('raspberry')             # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)                          # AttributeError: 'tuple' object has no attribute 'pop'
