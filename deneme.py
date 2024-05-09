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