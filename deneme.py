'''
TODOS :
     1- ask if the user has allergies and if so, exclude ingredients/recipes from the list.
        ["recipe"]["ingredientLines"]
     2- sort the results
     3- add pandas and other libraries for better data visualisation
     4 - add some recipes to favourites (save the file...)
'''


# Learning the index method or function or whatever :D
'''
people = ["Merve", "Orhan", "Mualla", "Orkun", "Willy"]

guess = input("Guess if the name exists!" + "\n" + "Write a name: ")

try:
    print(people.index(guess))
except ValueError:
    print("That item does not exist")

# print(people.index("P"))
'''


# filter function
'''
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)
'''

'''
countries={"Ghana": "Accra", "China": "Beijing"}
# using the del keyword
del countries["China"]
print(countries)
'''



# for loop in a variable
''' 
randomNum = [1, 2, 5, 85, 43, 0, 101]
people = ["Merve", "Orhan", "Mualla", "Orkun", "Willy"]

# lower the cases and loops through the people list :)
flattened = [flattenedNames.lower() for flattenedNames in people]

# compare the loops (the one above and the one below) 

for flattenedNames in people:
    flattenedNames.lower()
    # print(flattenedNames) # when we call flattenedNames in the left line it doesn't lower the cases for some reason.
    print(flattenedNames.lower())  # this way it works and it lowers the cases.

# print(flattened)
'''


# learn "any" W3Schools: https://www.w3schools.com/python/ref_func_any.asp

# if any


