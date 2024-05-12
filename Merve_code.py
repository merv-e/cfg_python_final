import requests
# import streamlit as str

# str run:
def recipe_search(ingredient):
    app_id = "9a01e4df"
    app_key = "f55aa716d20221d7c0b1a7bd7d721c8c"

    result = requests.get(f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}')

    if result.status_code == 200:
        data = result.json()
        return data['hits']
    elif result.status_code == 404:
        print("Failed to fetch recipes!! Status code:", result.status_code)
        return None
    elif result.status_code == 400:
        print("Something went wrong! Status code:", result.status_code)
        return None
    else:
        print("Status code:", result.status_code)


def save_recipe_to_favourites():
    # Ask if the user wants to save any recipe to favorites
    liked_recipe = input("Is there any particular recipe that you liked among these recipes? "
                         "Please respond with 'y' or 'n': ")

    if liked_recipe.lower() == "y":
        recipe_name = input("What is the name of the recipe? Please respond with the label of the recipe: ")

        uri_of_the_fav_recipe = input("Please provide the uri of the recipe: ")

        # Append the recipe name and URI to the file instead of rewriting the file each time the function runs
        with open('favourite_recipes.txt', "a") as fav_file:
            fav_file.write(f"{recipe_name}, {uri_of_the_fav_recipe}\n")

        print(f"{recipe_name} has been added to your favourite recipes.")


def  is_allergic(results):
    allergy = input("What are you allergic to? Please specify it below: ").lower()
    filtered_results = []

    for result in results:
        recipe = result["recipe"]
        ingredients = [ing.lower() for ing in recipe["ingredientLines"]]

        # Append the recipe to 'filtered_results' if none of the ingredients contain the specified allergen.
        # This ensures that only recipes safe for the user's dietary restrictions are selected.
        if not any(allergy in ingredient for ingredient in ingredients):
            filtered_results.append(recipe)

    # Show the recipes that are obtained from the API and also the recipes after being filtered.
    print("Number of original recipes:", len(results))
    print("Number of recipes after filtering:", len(filtered_results))
    print()

    for recipe in filtered_results:
        print("Recipe:", recipe["label"])
       # print("URL:", recipe["uri"])
       # print("Calories:", round(recipe["calories"], 2))
       # print("Diet Labels:", ', '.join(recipe["dietLabels"]))
       # print()

def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)

    # If recipe_search did not retrieve data successfully
    # (i.e., results is None due to non-200 status codes or other issues), exit the function.
    if results is None:
        return

    has_allergy = input("Do you have any allergies? Please respond with 'y' or 'n': ")

    if has_allergy.lower() == "y":
        is_allergic(results)

    else:
        for result in results:
            print("Recipe:", result["recipe"]["label"])
            print("URL:", result["recipe"]["uri"])
            print("Calories:", round(result["recipe"]["calories"], 2))
            print("Diet Labels:", ', '.join(result["recipe"]["dietLabels"]))
            print()

    # Ask after displaying all recipes
    save_recipe_to_favourites()


run()

