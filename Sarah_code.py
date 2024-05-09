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

    # Call the recipe search function with user-provided API credentials
    results = recipe_search(ingredient, app_id, app_key)
    #

    # Save the recipes to a file
    if results:
        save_to_file(results)
        print("Recipes saved to 'recipes.txt' file.")
    else:
        print("No recipes found.")

# Run the program
if __name__ == "__main__":
    run()