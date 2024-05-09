import requests
def recipe_search(ingredient, app_id, app_key):
    # Fetching data from Edamam API
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    # Parsing the JSON response
    data = result.json()
    return data['hits']

def save_to_file(recipes):
    with open(".venv/recipes.txt", "w") as file:
        for recipe in recipes:
            file.write(recipe['recipe']['label'] + "\n")
            file.write(recipe['recipe']['url'] + "\n\n")

def run():
    # Prompt the user to register for Edamam API
    print(
        "To get your Edamam API credentials, please register at https://developer.edamam.com/ and "
        "obtain your app ID and app key.")
    app_id = input('Enter your Edamam API app ID: ')
    app_key = input('Enter your Edamam API app key: ')

    # Ask the user to enter an ingredient
    ingredient = input('Enter an ingredient: ')

    meal_type_necessary = input("Is the meal type important to you? y or n:")
    if meal_type_necessary == "y":
        meal_type = input("Please choose between the options of breakfast, lunch or dinner: ")
      #  if results["mealType"] == meal_type


    # Call the recipe search function with user-provided API credentials
   # else:
        results = recipe_search(ingredient, app_id, app_key)

    # Save the recipes to a file
    if results:
        print(results[1]) # + "\n"
        save_to_file(results["recipe"]["calories"])
        print("Recipes saved to 'recipes.txt' file.")
    else:
        print("No recipes found.")

# Run the program
if __name__ == "__main__":
    run()