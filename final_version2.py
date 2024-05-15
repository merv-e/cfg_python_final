import requests

# Global variables for storing app ID and key
app_id = None
app_key = None


def recipe_search_v2(ingredient, diet=None, calorie=None, nutrient=None):
    global app_id, app_key

    if not app_id or not app_key:
        print("Please provide your Edamam API app ID and app key.")
        return []

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


def save_recipe_to_favourites(recipe):
    with open('favourite_recipes.txt', "a") as fav_file:
        fav_file.write(f"{recipe['label']}, {recipe['url']}\n")
    print(f"{recipe['label']} has been added to your favourite recipes.")


def print_recipe(recipe):
    print("Recipe:", recipe['label'])
    print("URL:", recipe['url'])
    print("Calories:", round(recipe['calories'], 2))
    print("Diet Labels:", ', '.join(recipe['dietLabels']))
    print()


def run():
    global app_id, app_key

    print(
        "To get your Edamam API credentials, please register at https://developer.edamam.com/ and obtain your app ID and app key.")
    app_id = input('Enter your Edamam API app ID: ')
    app_key = input('Enter your Edamam API app key: ')

    ingredient = input('Enter an ingredient: ')
    allergy = input("Do you have any allergies? Please respond with 'y' or 'n': ")

    if allergy.lower() == "y":
        allergy_ingredient = input("What are you allergic to? Please specify it below: ").lower()
    else:
        allergy_ingredient = None

    calorie = input('Enter maximum calorie limit (optional): ')

    results = recipe_search_v2(ingredient, nutrient=allergy_ingredient, calorie=calorie)

    if results:
        display_recipes(results)
        save = input("Would you like to save any of these recipes to your favorites? (y/n): ")
        if save.lower() == "y":
            recipe_number = input("Enter the number of the recipe you want to save: ")
            try:
                recipe_index = int(recipe_number) - 1
                if 0 <= recipe_index < len(results):
                    save_recipe_to_favourites(results[recipe_index]['recipe'])
                else:
                    print("Invalid recipe number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        print("No recipes found.")


def get_7_day_diet_recommendation():
    global app_id, app_key

    if not app_id or not app_key:
        print("Please provide your Edamam API app ID and app key.")
        return

    print("7-Day Diet Recommendation:")
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days:
        print(f"\n{day}:")
        ingredient = input(f'Enter an ingredient for {day}: ')
        results = recipe_search_v2(ingredient)
        if results:
            print("Recommended Recipe:")
            print_recipe(results[0]['recipe'])
        else:
            print("No recipes found.")


if __name__ == "__main__":
    run()
    get_7_day_diet_recommendation()