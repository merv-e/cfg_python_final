import requests

# Function to search for recipes based on an ingredient, diets, calories, and nutrient ranges
def recipe_search_v2(ingredient, app_id, app_key, diet=None, calorie=None, nutrient=None):

    # Dora's Code:

    # Constructing the API URL with the ingredient and mandatory parameters
    url = f"https://api.edamam.com/api/recipes/v2?type=public&q={ingredient}&app_id={app_id}&app_key={app_key}"

    # Adding optional parameters if provided
    if diet:
        url += f'&diet={diet}'
    if calorie:
        url += f'&calories={calorie}'
    if nutrient:
        url += f'&nutrient={nutrient}'

    # Make a request to the Edamam API
    result = requests.get(url)

    # Check if the response is successful
    if result.status_code == 200:
        # Extract recipe data from the response
        data = result.json()
        # Check if 'hits' key exists in the response
        if 'hits' in data:
            return data['hits']
        else:
            print("No recipes found.")
            return []
    else:
        print("Failed to fetch recipes. Status code:", result.status_code)
        return []
        # NOTE!! can be changed into None?!

# Dora's code
# Function to display recipes
def display_recipes(results):
    print("Recipes found:")
    print("===================")
    for index, result in enumerate(results, start=1):
        recipe = result['recipe']
        print(f"{index}. {recipe['label']}")
        print(f"   Link: {recipe['url']}")
        print()


# Sarah's Code:
def save_to_file(recipes):
    with open("recipes.txt", "w") as file:
        for recipe in recipes:
            file.write(recipe['recipe']['label'] + "\n")
            file.write(recipe['recipe']['url'] + "\n\n")


# Sarah's Code
def print_recipe(recipe):
    print("Recipe:", recipe['label'])
    print("URL:", recipe['url'])
    print("Calories:", round(recipe['calories'], 2))
    print("Diet Labels:", ', '.join(recipe['dietLabels']))
    print()

# Merve's code
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


# Merve's code
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

# Main function to run the program
def run():
# Dora's Code

    # Prompt the user to register for Edamam API
    print(
        "To get your Edamam API credentials, please register at https://developer.edamam.com/ and obtain your app ID and app key.")
    app_id = input('Enter your Edamam API app ID: ')
    app_key = input('Enter your Edamam API app key: ')

    # Ask the user to enter an ingredient
    ingredient = input('Enter an ingredient: ')

    # Optional: Ask for diet, calorie limit, and nutrient range
    diet = input('Enter diet (optional): ')
    calorie = input('Enter maximum calorie limit (optional): ')
    nutrient = input('Enter nutrient range (optional): ')


    # Call the recipe search function with API credentials
    results = recipe_search_v2(ingredient, app_id, app_key, diet, calorie, nutrient)

    # Merve's code
    # If recipe_search did not retrieve data successfully
    # (i.e., results is None due to non-200 status codes or other issues), exit the function.
    if results is None:
        return

    has_allergy = input("Do you have any allergies? Please respond with 'y' or 'n': ")

    if has_allergy.lower() == "y":
        is_allergic(results)

# Maybe printing can be different for everyone?

# Sarah's Code:
 # Save the recipes to a file
    if results:
        # Sorting recipes by diet and then by calories
        sorted_results = sorted(results, key=lambda x: (x['recipe']['dietLabels'], x['recipe']['calories']))

# Which one are we going to print?

        # Printing each recipe
        for result in sorted_results:
            print_recipe(result['recipe']) # Sarah's code
            display_recipes(results) # Dora's code

        # Save recipes to a file
        save_to_file(sorted_results)
        print("Recipes saved to 'recipes.txt' file.")
    else:
        print("No recipes found.")

# Merve's code
    # Ask after displaying all recipes
    save_recipe_to_favourites()

# Run the program
if __name__ == "__main__":
    run()

