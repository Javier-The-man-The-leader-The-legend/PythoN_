#region Trick 1
x_coords = [45, 92, 20, 71, 53]
y_coords = [24, 21, 68, 47, 19]
#You have to give all the coordinates in order with tne one below them
for i in range(len(x_coords)): 
    print(x_coords[i],",",y_coords[i])
# Code in line three is the same as:
# for i in range(len(x_coords)):
#   print(x_coords[i],",",y_coords[i]
for x, y in zip(x_coords, y_coords): 
    print(x,",", y) #This code is preferable than line 5,6
#endregion
#region Trick 2
#Print each item in order
shopping_list = ["bread", "cereal", "rice", "pasta", "eggs", "orange juice"]
for i in range(len(shopping_list)):
     print("item",i,":",shopping_list[i])
#endregion
#region Shortcut 1
#Swap a and b
a = 10
b = 20
a,b = b,a
print(a,b)
#endregion
#region Important thing to know
#We want to inspect a variable, object, module, class, etc... (defect doesnt print data)
# import math
# print(dir(math))
shapes = {"square": 4, "triangle": 3, "Hexagon": 6}
print(shapes.items())#,dir(shapes),
#endregion
#region Really difficult
#We have to categorise a sentance of words
from pprint import pprint
sentence = "Rock music visits Japan in the winter in white and black."
words = sentence.split(" ")
results = {}
for word in sorted(words):
    first_letter = word[0]
    if first_letter in results:
        results[first_letter].append(word)
    else:
        results[first_letter] = [word]
pprint(results)
# endregion
#region Tip 1
#We want to inicialise a list with a number of starting values
a = []
for _ in range(0,1): 
    a.append("Lorenzo the wolf")
pprint(a)
#endregion
#region
# Making comparisons more concise
#Check if a value is with a range
age = int(input())
if 5 <= age < 18:
    print("Yes")
else:
    print("No")