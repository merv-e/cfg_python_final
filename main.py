import requests

def recipe_search(ingredient):  # ,app_id, app_key
    app_id = "9a01e4df"
    app_key = "f55aa716d20221d7c0b1a7bd7d721c8c"

    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))

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
        print("Something went wrong!")


def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)

    # Exit the function if the status code is something else than 200
    if results is None:
        return

    has_allergy = input("Do you have any allergies? Please respond with 'yes' (y) or 'no' (n): ")

    if has_allergy == "y":
        allergy = input("What are you allergic to? Please specify it below: ").lower()
        filtered_results = []

        for result in results:
            recipe = result["recipe"]

            # Flatten and convert all ingredients to lowercase for comparison
            ingredients = [ing.lower() for ing in recipe["ingredientLines"]]
            print("ingredients: ", ingredients)

            # Filter out recipes that contain the allergen
            if not any(allergy in ingredient for ingredient in ingredients):
                filtered_results.append(recipe)

        print("Number of original recipes:", len(results))
        print("Number of recipes after filtering:", len(filtered_results))
        print()

        for recipe in filtered_results:
            print("Recipe:", recipe["label"])
            print("URL:", recipe["uri"])
            print("Calories:", round(recipe["calories"], 2))
            print("Diet Labels:", ', '.join(recipe["dietLabels"]))
            print()

    else:
        for result in results:
            print("Recipe:", result["recipe"]["label"])
            print("URL:", result["recipe"]["uri"])
            print("Calories:", round(result["recipe"]["calories"], 2))
            print("Diet Labels:", ', '.join(result["recipe"]["dietLabels"]))
            print()

run()
