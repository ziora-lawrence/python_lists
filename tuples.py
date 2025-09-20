#thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
#print(thistuple)
#mytuple = ("apple", "banana", "cherry")
#print(type(mytuple))
#this_tuple = ("apple", "banana", "cherry")
#print(len(this_tuple))
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
#thistuple = ("apple")

# print(type(thistuple))
# daniels_tuple = ("games" "eggs" "milks")
# print(type(daniels_tuple))
# tuple requires commas to separate values
#  daniels_tuple = ("games", "eggs", "milks")
# print(type(daniels_tuple))


# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])


# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)
#so to change a tuple, you must convert it to a list, make your changes, and convert it back to a tuple.

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)
#you can add items using the same method as changing a tuple (convert to list, add item, convert back to tuple)by using append.


# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)
#you can remove items using the same method as changing a tuple (convert to list, remove item, convert back to tuple) by using remove.



#assigning a tuple to a variable is called "unpacking"
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)