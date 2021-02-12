"""By Kay towner"""
import math
import numpy as np
import random

#2. LIST TYPE QUESTIONS:

#2.1: list operations:

#1.
trek = ['Deep Space Nine', '7', '19.97']
#2.
serieslength = ['7', '4', '7', '7'] 
#3.
total = trek + serieslength #combined the two lists. the second at the end of the first
#4.
total[0] #first
total[-1] #last
#5.
total[5] = 'targ' #(fictional klingon dog-thing)
total.sort() #it did nothing, because the items cannot be
#listed in decending order.

#2.2: list methods:

#1.
cass = ['3', '4', '1', '2', '5']
print(cass)
len(cass)
#2.
cass.sort()
#3.
cass.sort(reverse=True)
#4.
cass.pop(-1)#if you know the length of the list put in that index, or the
#pop from the 'negative' side
#5.
cass.insert(3, '0.03')

#2.3: indexing lists:

#1.
L = [12, 434, 24, 3463, 437]
M = [1, 0.5, 4, 2.3, 0.1]
#2.
M.index('4' [ ,start[,end]])
L[4]
#3.
M.index(M <= 1, [ ,start[,end]])
#4.
R = [1, 2, 0.5, 6, 4]
R.index('0.5' [ ,start[,end]])
#5.
#mass = 4, stellar ID = 24



#2.4: list comprehension:
#1.
myName = ["K", "A", "Y"]
print(myName)
#2.
randnumlist = random.sample(range(0, 10), 5)
print(randnumlist)
#3. 
multnums = random.sample(range(0, 10) * random.sample) #had trouble with this one?
#4.
odo = [1, -1, 3, -5, -6, 7]
newlist = []

for i in odo: #(I like using for loops)
    if i > 0:
        print(i)
        newlist.append(i)
        print(newlist)

#5.Create the following 3x3 matrixa = [[1, 1, 1],[2, 2, 2],[3, 3, 3]].
#Flatten it using one lineof code.  (i.e.  turn it from a list of lists into one list).
a = [[1, 1, 1],[2, 2, 2],[3, 3, 3]]

flattened_list = [y for x in a for y in x]



#3: DICTIONARY TYPE QUESTIONS:

#3.1 dictionary basics:

#1.
#lists and dicts are different in that dicts ar organized by keys whereas lists are
#organized by their position.

#2. 
#Dicts and lists are similar in that they are both sets of objects, but they are also
#both mutable objects, they can be changed. 

#3.What is a key and what is a value?4.  By using the following keys, show all
#A key is when. . . 


#4 
#1. creating dicts with literals:
cassdict = {"Dean" : 1
    "Sam" : 2
    "Mary" : 3
    "Bobby" : 4
    }
#2.Empty dicts:
emptydict = {}

#3. A dict with a list of tuples:
casslisttodict = [("Dean" : 1), ("Sam" : 2), ("Mary" : 3), ("Bobby" : 4)]
cassdict2 = dict(casslisttodict)

#4. Using a dict constructor:
cassdict3 = dict(Dean = 1
    Sam = 2
    Mary = 3
    Bobby = 4
    )

#5.
#Key order does not matter because, dict keys are for looking for a
#corrosponding value. position in the dict is not important, only the
#corrosponding value.


#3.2 creating dictionarys:

#1.
voyagerdict = { 'Janeway' : ["captain", "red"],
                'Neelix' : (1, 2, 3), 'Seven' : float(.001) }
#2.
values = voyagerdict.values()
voyager_list = list(values)

voyvalue = voyager_list(1)
print(voyvalue)
#3. 
voyagerdict['Kes'] = [(4, 5, 6)]
#4. printdict.values(),dict.keys(), anddict.items()and explain the difference.
dict.values()
#this prints out the values of the dict
dict.keys()
#prints out the keys
dict.items()
#prints out the keys and values as a list-type format
#5.
voyagerdict["Janeway"].append('4')

#3.3 dictionaries as databases:

#1. Create a dictionary with information about one of your favourite films.
##Include the following keys:  thename of the film as a sting,
##the year it was made as an integer,
##the amount of money it made as a
##floatand 5 of the key actors as a list of strings.
favefilmdict = {'Megamind' , 2009 , float(321.9) ,
                ("Will Ferrell", "Tina Fey", "David Cross", "Brad Pitt", "JK Simmons")}
#2.
print(favefilmdict)
#the print was out of order, this does not matter as only does the corrolation to a value
#3.  Print the first actors name in your list of actor names
for value in favefilmdict:
    print(value, favefilmdict[]) #had difficulty with this one

#4.
#I read that keys cannot be changed, so I tried just appending a new key.
favefilmdict['2009'] = '+2'
#5.
favefilmtwodict = {'Jurassic Park' , 1993 , float(1.033) ,
                ("Jeff Goldblume", "Sam Neill", "laura Dern", "Richard Attenborough", "BD Wong")}

database = favefilmdict + favefilmtwodict

#3.4 lets do another!

#1.
cardict = {'Vokswaen' : [], 'Bay Window' : 1974, 'green' : [], 'electric' : False}
#2.
secondcardict = {'Tesla' : [], 'Modelx' : 2020, 'black' : [], 'electric' : True}
cardict.append[] #again I had some trouble here
#3.
dict.values()
#4.
cardict(0) = 'Volkswagen'
#5.


#4: QUESTIONS:

##4.1 

##1.  
#a tuple is an ordered list of elements. 
##2.
#they are written with () brackets, they store multiple items in one veriable.
##3. 
#Tuples have fixed lenth and cannot be changed, unlike a list.

##4.  
#they both store data
##5.  
#tuples are best for grouping similar data i.e colors

##6.  When creating and opening a new file, what is the best mode to use to write to it?
#the 'w' mode


##What is the bestmode to use to append to it?
#the 'a' mode

##7.  If I opened a new file called ’data.txt’, where would this file be saved?
#wherever you have chosen txt to go, most likely in the file that holds the current .py file.

##8.
#this command reads out the lines of a file in one completed line.
##9.  
#use the direct path, I think it's called.

##10.  
#close()   <---( it's always important to close a file as it's good habit and uses less energy for your program. (I don't know how
#to say this, but too many open files can slow your program.)

##11.  
#.csv, zip, .txt, and json

##12.What are the four different ’modes’ and what do they do?
#'r' for reaadin a file
#'w' for writting to a file
#'a' appending to a file
#and 'r+' reading mode plus writing





















































