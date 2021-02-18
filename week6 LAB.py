"""Written by Kay Towner"""
"""2/17/21"""

##2
##1.  What is a compound statement in Python, and
##what does the syntax of a compound statement looklike?
##
#compound statements are groups of statements, for, if, else ect.
#they general are formated with indentations and sepereated
#by colons on each line.

##2. What does it mean to indent code,
##and what is the best way to do this?
##
#indented code is best done by hitting tab or four spaces
#to inded is to put a statement within a statement (nested)

##3.  How do you end a line in Python?
##
#python lines can end in '\n' (can be used with print statements)

##4.  What are the four variable name patterns you should NOT use?
##
#if, else, def, while

##5.  What is the only way to write multiple Python
##statement on one line and what type of statementscannot be written this way?
#for this you should use a colon ;, and typicaly only print statements.


#2.2
##1.  Define X and Y, and write a Booleanandstatement that returns X.
##Now redefine your variables, andwrite a Booleanandstatement that returns Y.
#
x = 1
y = 3

x and y
y and x


##2.  What is a possible value for A, that returnsnot A == False?
##what aboutTrue?  Why is this thecase?
#
A = 2
B = 3

2 > 3

2 < 3
#this works because 2 is less than 3????

##3.  What is the printed return for the following expression:  100<500, and why?
#True - because 100 is less than 500

##4.  Are the following objectsTrueorFalse?
##(a)  5
# true
##(b)  [ ]
#false
##(c)  None
#false
##(d)  0
#false
##(e)  ’no
#true
##5.  What is the printed return for the following expression, and why?2 or 400
#it read out 2, because 2 is the first item.


##2.3
##1.  In the following assignment, what doesteaequal? mug = tea = ‘yum’
# teas is equal to yum

##2.  In the following assignment, what doescequal?a, b, c, d, e, f = ‘coffee’
# 'f'

##3.  In the following assignment, what doesbequal?
##What aboutc?a, *b, c = ‘coffee’
# 'e'

##4.  In the following assignment, what does a equal?
##*a, b = ‘coffee’
# it equals: ['c', 'o', 'f', 'f', 'e']

##5.  The format of Extended Sequence Unpacking was new in Python 3.X,
##what is it?
# It's made into a list.


#2.4

##1. Set X = 0. Add 1 to X,
##using an augmented assignment, and then -5 using another.
##
X = 0
X + 1
X - 5
#= -5

##2. Now set X to a string, your choice.
##Again use an augmented assignment to add 1. What is the difference
##in the result, why?
##
bashir = X = 0
garak = bashir + 1
garak - 5
#= -4, it's off by one, because it was starting 'fresh' befor with the original
#X equal to 0. When using strings, it stayed changed.

##3. Again, set X to a string, your choice. Now add another string using an augmented assignment. This
##time the code should work? Why, what is the difference?
## It works this time because strings can be multiple different veriable names
odo = 5
garak + odo
# ---> 6

##4. Now set X = 10. Perform the operation X *= 2. What is the result and why?
##
garak = 10
garak *= 2
# 20, this works because the second operation is an opperatiion, not reassigning the veriable.

##5. Perform the operation X **= 2
##on your new value of X from above. What is your new result? Why?
##
garak **=2
#400, it squared the previouse veriable value.


#2.5

##1. Set four strings of your choice equal to the variables a, b, c and d.
##
d = 'dean'
c = 'cas'
a = 'adam'
b = 'bobby' #(always with the supernatural characters lol)

##2. Print a, b, c, and d manually as normal. Now separate them with a comma and print. Now concatenate
##them together within the print command using the separator.
##
print(a,b,c,d, sep=',')

print(a,',',b,',',c,',',d, ',', a,b,c,d )

##3. Now repeat part b, saving the results into a file called ’log.txt’.
##
print(a,',',b,',',c,',',d, ',', a,b,c,d, file=sys.stdout)
import sys
sys.stdout = open('abcdfile.txt', 'a')
sys.stdout.close()

##4. Repeat part b, one more time, printing out to the terminal, but adding an ellipse to the end of the
##print statement.
##
print(a,',',b,',',c,',',d, ',', a,b,c,d )

##5. What syntax do the keyword arguments in the print statement have to follow.
#the syntax the keyword arguments use is the name = value syntax



#3

#3.1

##1. Open the file called week 6 data.txt.
##Inside you will find fictional stellar ID’s, masses (in solar masses)
##and radii (in solar radii). Turn each of these columns into a list.
##Name them appropriately
##
import pandas as pd

f = open('week_6_data.txt', 'r')
lines = f.readlines()

starColmn = pd.DataFrame(f, columns=['id', 'mass', 'radius'])
print(starList)

starID = starColmn =['id'].to_list()
starMass = starColmn =['mass'].to_list()
starRad = starColmn =['radius'].to_list()

##2. Create an if test which cycles through each of the stellar masses
##and saves those which are greater than
##or equal to 1.0 in a new list.
##
for line in f:
    if starMass <= 1.0:
        starMass = newMassList 


##3. Create a second if test which cycles through each of the stellar radii
##and saves those which are less
##than 0.6 as a new list, and those between 0.6 and 1 in a second list.
##Ignore the others.
##
for line in f: #i'm not so sure about this code here
    if starRad > 0.6:
        starRad = newRadList
    else:
        starRad = newRadListSecond


##4. Now, consider the original lists. Test each star with an if test, to determine the ID numbers of those
##stars with a mass less than 1 and a radius greater than 1. Save these ID numbers in a new list. (HINT:
##This will require the use of indices as opposed to values, think range(len(L))). Do NOT use zip in this
##instance.
##

for line in starID:
    if starID == starMass:
        if starMass < 1 and starRad > 1:
        print() #had trouble here
        else:
            continue
f.close()

##5. Write the following loop as a if/else ternary expression:
##if Y:
##A = 0
##else:
##continue

if Y and A == 0:
    else:
        continue




#3.2

##1. Define two variables, a = 10 and b = 0 b
##
a = 10
b = 0

##2. Create a while loop that will continue to cycle as long as the condition a > b is met.
##
while a > b:
    
##3. Within your loop, print True and the value of a and b
##
while a > b:
    print(True, a, b)

##4. After your print statements, add 2 to the value of b.
##
while a > b:
    print(True, a, b)
    b + 2
    
##5. Run your code, how many iterations of the cycle are printed? Why? If you add 2 to a as well, what
##happens and why?
#it went on infinently.
while a > b:
    print(True, a, b)
    newb = b + 2
    newa = a + 2
    print(newa)
    print(newb)
    


#3.3

##1. Again we will be using the lists that can be taken from the star file
##
import pandas as pd

f = open('week_6_data.txt', 'r')
lines = f.readlines()

starColmn = pd.DataFrame(f, columns=['id', 'mass', 'radius'])
print(starList)

starID = starColmn =['id'].to_list()
starMass = starColmn =['mass'].to_list()
starRad = starColmn =['radius'].to_list()
f.close()

##2. First we want to know the masses of the stars in kg.
##The mass of the Sun in kg is 1.989e+30 [kg]. Use
##a for loop to create a new list of the stellar masses in kg.
##

for mass in starMass:
    sunkg = 1.989e**30
    Massinkg = sunkg * line
    print(Massinkg)

##3. Now we want to know the radii of the stars in m.
##The radius of the Sun in m is 6.96e8 [m] Use a for
##loop to create a new list of stellar radii in m.
##

for line in starID:
    sunrad = 6.9e**8
    radsinm = sunrad * line
    print(rasinm)

##4. Initialize an empty list. Assuming the star is a sphere,
##use a list to determine the density of each star,
##using the standard density equation ρ = M/V .
##

DensityList = []

for line in f:
    density = M/V
    #what to do here?
    DensityList.append(density)

    
##5. Order the stellar IDs in ascending order in terms of value of the stellar density.
##i.e. from the star with
##the lowes density to the star with the highest density.

for line in starID:
    starID.sort()


#3.4

##1. What is thedifference between the break and continue statements?
#Break is used to terminate a loop, but continue is used for skipping over code.
    
##2. What does the pass statement do, and when should it be used?
#The pass statement is for when you want to run that part of the code
#later, but not yet.

##3. What does the else statement do, and what kind of loops and tests can it be used in?
#Else can be used/read like "otherwise". it can be used for true or false 
  
##4. In the case of an if test, say you have two tests to perform,
##what would the three headers of your
##compound statement look like?
#if, if, else?

##5. What is a nested loop?
#A nested loop is when you have loops within loops like:
##if I in team:
##    if a in team:
##        if and so on:

#3.5

##1. Create a range of numbers from -5 to 0 with a step size of 2. Print the result
##
print(range(-5, 0[,2]))

##2. Create a range of numbers from 5 to -6 with a step size of 4. Print the result.
##
print(range(5, -6[,4]))

##3. Create a string of length 5. Using a for loop and len(range(S)),
##print each of the values in the string
##and the index created.
##
jupiter = [5]

for i in jupiter:
    print(i, len(range(jupiter))

##4. Do the same as in part a but with the enumerate tool.
##
mars = [5]
for (offset, item) in enumerate(mars):
          print(offset, item)

##5. What does the zip tool do, and where might it be useful in astronomy?
#the zip tool "allows a loop to visit multiple sequences in parallel", this is goo
#in astro because it's useful for coordinate systems.



          








