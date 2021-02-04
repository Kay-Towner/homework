#2.1 BASIC NUMERIC TYPE INFORMATION:

#1. int, float, bools
#2.
import math

a = 3*8.7
print(a)

#3. 
26.099999999999998 #this type is a number

#4.
b = int(5.67)
print(b)

#5.
#PEMDAS
#A*B then it will subtract C


#2.2 ALL ABOUT DIVISION

#1. floor division rounds "down"
#2. round down
#3. 5
#4. a) is A to the (B/C) where as b) is A to the power of B divided by C

#2.3 COMPARISONS

#1. 4 less than 5, output: True
#2. 4 not equal to 4, ouput: False
#3. 2 is equal to 2, output: True
#4. 1 less than 3 less than 5.0, output: True
#5. 1 less than 2 and also 2 greater than 1, output: True

#2.4 VARIABLES

#1. once it is assinged value
#2. any word or number
#3. b - a
#4. yes.

#3 STRING TYPE QUESTIONS

#3.1

#1. Characters and bytes

#2.
string = 'Kay'
print(string)

#3. Nothing, it's just formating "" are usually used for comments

#4. for dealing with appostrophis cat's for example.

#5.
str(5)


#3.2 ESCAPE SEQUENCES

#1. it can represent white spaces
#2. \t
#3. \n
#4. 
colors = 'yellow\n', 'pink\n', 'green'
print(colors, '\n')
#5.
fruit = 'blueberry', 'cherry', 'grape'
print(fruit, '\t')

#3.3 RAW STRINGS AND TRIPLE QUOTES

#1. making a raw string is by: putting a \n between two words
#2. 1. for when we want to keep the \ inside a string 2. we don't want
#the \ used as an escape character.
#3. put the slash inside the ''
#4. Can be for multi line comments or for creating strings
#5. join() and using +

#3.4 INDEXING AND SLICING

#1.
orko = 'cat'
#2
print(orko[0])
#3.
print(orko[-1])
#4.
print(orko[:2])
#5.
print(orko[1:2])

#4 DYNAMICAL TYPED QUESTIONS

#4.1

#1. dynamical typing is when the veriabel types can change if desired
#2. means that methods in the "child class" have the same name as methods
#in the parent class
#3. a new object is created, python inernally caches and reuses certain kinds of
#unchangeable objects.
#4. variables: enteries in a system table with spaces for links to objects
# objects: pieces of allocated memory
#references: automatically followed pointers from variables to objects
#5. what happens when a variable is reassigned.
#6. yes
#7. a = lamp
#8. mutiple can be changed and altered vs immutable which cannot be changed
#9. int, float, bool
#10.
import sys
this = sys.getrefcount(5)
print(this)
#printed out 84

#11. means the code isn't used anywhere else within python
#12. Polymorphism means that the code can be done in a dynamic way,
#meaning that there is less to type in the end.























