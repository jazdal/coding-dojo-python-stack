# 01 - Update Values in Dictionaries and Lists

x = [[5, 2, 3], [10, 8, 9]]

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'}, 
    {'first_name': 'John', 'last_name': 'Rosales'}
]

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'], 
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}

z = [{'x': 10, 'y': 20}]

# 01A - Change the value 10 in x to 15. Once you're done, x should now be [[5, 2, 3], [15, 8, 9]]

print(x)
x[1][0] = 15
print(x)

# 01B - Change the last_name of the first student from 'Jordan' to 'Bryant'

print(students)
students[0]['last_name'] = 'Bryant'
print(students)

# 01C - In the sports_directory, change 'Messi' to 'Andres'

print(sports_directory)
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

#01D - Change the value 20 in z to 30

print(z)
z[0]['y'] = 30
print(z)

# 02 - Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'}, 
    {'first_name': 'John', 'last_name': 'Rosales'}, 
    {'first_name': 'Mark', 'last_name': 'Guillen'}, 
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

# iterateDictionary(students)
# should output
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary(some_list):
    for dict in some_list:
        output = ''
        for k, v in dict.items():
            output += f'{k} - {v}, '
        print(output[0:-2])

iterateDictionary(students)

# 03 - Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB

# And iterateDictionary2('last_name', students) should output:
# Jordan
# Rosales
# Guillen
# Tonel

def iterateDictionary2(key_name, some_list):
    [print(dict[key_name]) for dict in some_list]

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# 04 - Iterate Through a Dictionary With List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'], 
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

def printInfo(some_dict):
    for key, values in some_dict.items():
        print()
        print(len(values), key.upper())
        [print(name) for name in values]

printInfo(dojo)