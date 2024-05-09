import requests

def recipe_search(ingredient):  # ,app_id, app_key
    app_id = "9a01e4df"
    app_key = "f55aa716d20221d7c0b1a7bd7d721c8c"

    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))

    if result.status_code == 200:
        data = result.json()
        # print(data['hits'])
        return data['hits']
    else:
        print("Something went wrong!")

def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)  # , app_id, app_key


    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['uri'])
        print()

run()

'''
    elif result.status_code == 404:
        print("Failed to fetch recipes. Status code:", result.status_code)
        return []
    elif result.status_code == 400:
        print("Something went wrong. Status code:", result.status_code)
        return []
'''




'''
def save_to_file(recipes):
    with open("recipes.txt", "w") as file:
        for recipe in recipes:
            file.write(recipe['recipe']['label'] + "\n")
            file.write(recipe['recipe']['url'] + "\n\n")



def run():
    # Prompt the user to register for Edamam API
    print(
        "To get your Edamam API credentials, please register at https://developer.edamam.com/ and "
        "obtain your app ID and app key.")
   # app_id = input('Enter your Edamam API app ID: ')
   # app_key = input('Enter your Edamam API app key: ')

    # Ask the user to enter an ingredient
    ingredient = input('Enter an ingredient: ')

    # Call the recipe search function with user-provided API credentials
    results = recipe_search(ingredient) # , app_id, app_key
    #

    # Save the recipes to a file
    if results:
        save_to_file(results)
        print("Recipes saved to 'recipes.txt' file.")
    else:
        print("No recipes found.")

# Run the program
# The block below ensures that the run() function is called only if the script is executed directly,
# not when it's imported as a module.

if __name__ == "__main__":
    run()

'''
