import requests


# Function to search for recipes based on an ingredient, diets, calories, and nutrient ranges
def recipe_search_v2(ingredient, app_id, app_key, diet=None, calorie=None, nutrient=None):
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


# Function to display recipes
def display_recipes(results):
    print("Recipes found:")
    print("===================")
    for index, result in enumerate(results, start=1):
        recipe = result['recipe']
        print(f"{index}. {recipe['label']}")
        print(f"   Link: {recipe['url']}")
        print()


# Main function to run the program
def run():
    # Edamam API credentials
    app_id = '62ffbe64'
    app_key = 'ba767d55cf10a5142fed519d82f6840c'

    # Ask the user to enter an ingredient
    ingredient = input('Enter an ingredient: ')

    # Optional: Ask for diet, calorie limit, and nutrient range
    diet = input('Enter diet (optional): ')
    calorie = input('Enter maximum calorie limit (optional): ')
    nutrient = input('Enter nutrient range (optional): ')

    # Call the recipe search function with API credentials
    results = recipe_search_v2(ingredient, app_id, app_key, diet, calorie, nutrient)

    # Display the recipes
    if results:
        display_recipes(results)
    else:
        print("No recipes found.")


# Run the program
if __name__ == "__main__":
    run()

