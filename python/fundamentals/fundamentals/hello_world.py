# 1. TASK: print "Hello World"
print("Hello World")

# 2. print "Hello Jasper!" with the name in a variable
name = "Jasper"
print("Hello", name, "!")	# with a comma
print("Hello " + name + "!")	# with a +

# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", name, "!")	# with a comma
print("Hello " + str(name) + "!")	# with a +	-- this one should give us an error!

# 4. print "I love to eat pho and ramen." with the foods in variables
fave_food1 = "pho"
fave_food2 = "ramen"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

print(f"I love to eat {fave_food1.upper()} and {fave_food2.upper()}!")
print("the lord of the rings".title())
print("I LIKE TO WRITE IN ALL CAPS".lower())

rhyme = "Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked. If Peter Piper picked a peck of pickled peppers, where's the peck of pickled peppers Peter Piper picked?"

print(rhyme.count("peck"))
print(rhyme.split("peppers"))
print(rhyme.find("Peter"))
print("12345abcde".isalnum())
print("ABCDE".isalpha())
print("9900".isdigit())
print("python".islower())
print("JAVASCRIPT".isupper())

new_list = ["foo", "foo", "foo", "foo", "foo"]
print(new_list)
print("bar ".join(new_list))

print(rhyme.endswith("picked?"))