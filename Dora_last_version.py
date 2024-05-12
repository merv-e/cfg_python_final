import requests

def recipe_search_v2(ingredient, app_id, app_key, diet=None, calorie=None, nutrient=None):
    url = f"https://api.edamam.com/api/recipes/v2?type=public&q={ingredient}&app_id={app_id}&app_key={app_key}"
    if diet:
        url += f'&diet={diet}'
    if calorie:
        url += f'&calories={calorie}'
    if nutrient:
        url += f'&nutrient={nutrient}'

    result = requests.get(url)

    if result.status_code == 200:
        data = result.json()
        return data.get('hits', [])
    else:
        print(f"Failed to fetch recipes. Status code: {result.status_code}")
        return []

def display_recipes(results):
    if results:
        print("Recipes found:")
        print("===================")
        for index, result in enumerate(results, start=1):
            recipe = result['recipe']
            print(f"{index}. {recipe['label']}")
            print(f"   Link: {recipe['url']}")
            print()
    else:
        print("No recipes found.")

def print_recipe(recipe):
    print("Recipe:", recipe['label'])
    print("URL:", recipe['url'])
    print("Calories:", round(recipe['calories'], 2))
    print("Diet Labels:", ', '.join(recipe['dietLabels']))
    print()

def run():
    print("To get your Edamam API credentials, please register at https://developer.edamam.com/ and obtain your app ID and app key.")
    app_id = input('Enter your Edamam API app ID: ')
    app_key = input('Enter your Edamam API app key: ')
    ingredient = input('Enter an ingredient: ')
    results = recipe_search_v2(ingredient, app_id, app_key)

    if results:
        display_recipes(results)
    else:
        print("No recipes found.")

def save_recipe_to_favourites():
    liked_recipe = input("Is there any particular recipe that you liked among these recipes? "
                         "Please respond with 'y' or 'n': ")
    if liked_recipe.lower() == "y":
        recipe_name = input("What is the name of the recipe? Please respond with the label of the recipe: ")
        uri_of_the_fav_recipe = input("Please provide the uri of the recipe: ")
        with open('favourite_recipes.txt', "a") as fav_file:
            fav_file.write(f"{recipe_name}, {uri_of_the_fav_recipe}\n")
        print(f"{recipe_name} has been added to your favourite recipes.")


def is_allergic(results):
    allergy = input("What are you allergic to? Please specify it below: ").lower()
    filtered_results = []
    for result in results:
        recipe = result["recipe"]
        ingredients = [ing.lower() for ing in recipe["ingredientLines"]]
        if not any(allergy in ingredient for ingredient in ingredients):
            filtered_results.append(recipe)
    print("Number of original recipes:", len(results))
    print("Number of recipes after filtering:", len(filtered_results))
    print()
    for recipe in filtered_results:
        print_recipe(recipe)


def run():
    # run_recipe_search():
    app_id = input('Enter your Edamam API app ID: ')
    app_key = input('Enter your Edamam API app key: ')
    ingredient = input('Enter an ingredient: ')
    results = recipe_search_v2(ingredient, app_id, app_key)
    if results:
        has_allergy = input("Do you have any allergies? Please respond with 'y' or 'n': ")
        if has_allergy.lower() == "y":
            is_allergic(results)
        else:
            for result in results:
                print_recipe(result) ### This doesn't work
        save_recipe_to_favourites()
    else:
        print("Failed to fetch recipes!")

'''
def get_7_day_diet_recommendation():
    app_id = input('Enter your Edamam API app ID: ')
    app_key = input('Enter your Edamam API app key: ')
    print("7-Day Diet Recommendation:")
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days:
        print(f"\n{day}:")
        ingredient = input(f'Enter an ingredient for {day}: ')
        results = recipe_search_v2(ingredient, app_id, app_key)
        if results:
            print("Recommended Recipe:")
            print_recipe(results[0]['recipe'])
        else:
            print("No recipes found.")
'''

if __name__ == "__main__":
    run()
    # run_recipe_search()
    #   get_7_day_diet_recommendation()