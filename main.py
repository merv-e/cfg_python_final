import requests

def recipe_search(ingredient):  # ,app_id, app_key
    app_id = "9a01e4df"
    app_key = "f55aa716d20221d7c0b1a7bd7d721c8c"

    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))

    if result.status_code == 200:
        data = result.json()
        return data['hits']
    else:
        print("Something went wrong!")
    '''
        elif result.status_code == 404:
            print("Failed to fetch recipes. Status code:", result.status_code)
            return []
        elif result.status_code == 400:
            print("Something went wrong. Status code:", result.status_code)
            return []
    '''

def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)

    has_allergy = input("Do you have any allergies? Please answer with a 'yes' with 'y' or 'no' with 'n': ")

    if has_allergy == "y":
        allergy = input("What are you allergic of? Please write down: ")
        for result in results:
           recipe = result["recipe"]
           try:
               if recipe["ingredientLines"].index(allergy):
                   # TODO-1: filter the recipes that the user is not allergic of.
                   print("index of the allergen:", recipe["ingredientLines"].index(ingredient))
                   index_of = recipe["ingredientLines"].index(ingredient)
                   recipe["ingredientLines"].index(ingredient).pop(index_of)
                   print(index_of)

                   # TODO-2: save it to a file for future use.
           except ValueError:
                #  print("Good to go! That allergen is not listed!")
                # print(recipe)
                print("Todo bien!")

    else:
        for result in results:
            print(result["recipe"]["label"])
            print(result["recipe"]["uri"])


    # def add_recipe_to_favourites(recipe):


run()

'''
# and filter(filter_recipes_by_allergy, allergy)

def filter_recipes_by_allergy(al):
    if al:
        return False
    else:
        return True
'''
