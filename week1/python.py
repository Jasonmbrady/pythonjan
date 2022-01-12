# booleans
a = True
b = False
# numbers
c = 5
d = 12
# print(type(c))
# strings
e = "this is a string"
# print(len(e))
# COLLECTIONS:
# lists
fruit = ["apple", "orange", "banana", "tomato"]
fruit.append("watermelon")
# print(fruit)
# print(fruit.pop())
# dictionaries
g = { 
    "oblique": "neither parallel nor at a right angle to a specified or implied line; slanting.",

    }
# print(g["oblique"])
# conditionals
# if/else
h = 0
i = 10
if h > i:
    print("yup!")
elif i > h:
    print("nope!")
else:
    print("whoa!")
# Loops
users = [{"name": "Jason", "password":"password"}, {"name": "Caden", "password":"Gu3$$Thys!!"}]
for user in users:
    print(user["name"])

#functions

def add_nums(j, k):
    return j+k
print(add_nums(5, 7))

def hello_world():
    print("Hello, World!")


