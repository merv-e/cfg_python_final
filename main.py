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

    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['uri'])
        print()

run()




