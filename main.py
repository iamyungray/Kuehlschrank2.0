import requests

api_key = "YOUR_API_KEY_HERE"

while True:
    ingredients = []

    while True:
        ingredient = input("Bitte geben Sie eine Zutat ein (oder 'fertig', wenn Sie fertig sind): ")
        if ingredient == "fertig":
            break
        ingredients.append(ingredient)

    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={','.join(ingredients)}&apiKey={api_key}&number=5"

    response = requests.get(url)

    if response.status_code == 200:
        recipes = response.json()
        if len(recipes) == 0:
            print("Keine passenden Rezepte gefunden. Bitte geben Sie andere Zutaten ein.")
        else:
            print("Hier sind einige Rezepte, die Sie mit den verfügbaren Zutaten machen können:")
            for recipe in recipes:
                print(recipe['title'])
    else:
        print("Fehler bei der Abfrage der API.")

    choice = input("Möchten Sie weitere Rezepte suchen? (j/n): ")
    if choice.lower() != "j":
        break
